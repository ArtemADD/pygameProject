import pygame as pg
from setting import *
import math


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS_MAP1 if self.game.map.m == 1 else PLAYER_POS_MAP2
        self.angle = PLAYER_ANGLE_MAP1 if self.game.map.m == 1 else PLAYER_ANGLE_MAP2
        self.rel = pg.mouse.get_rel()[0]
        self.shot = False
        self.rezult = 0
        # здоровье
        self.health = PLAYER_MAX_HEALTH
        self.health_recovery_delay = 700
        self.time_prev = pg.time.get_ticks()

    def check_game_over(self):
        if self.health < 1:
            self.game.end = True
            # self.game.object_renderer.game_over()

    def recover_health(self):
        if self.check_health_recovery_delay() and PLAYER_MAX_HEALTH > self.health > 0:
            self.health += 1
            print(self.health)
            if self.health > 1:
                self.game.hp.image = pg.transform.scale(pg.image.load('res/icon/hp.png').convert_alpha(),
                                                        (self.health * 3, 50))

    def check_health_recovery_delay(self):
        time_now = pg.time.get_ticks()
        if time_now - self.time_prev > self.health_recovery_delay:
            self.time_prev = time_now
            return True

    def get_damage(self, damage):
        self.health -= damage
        if self.health > 1:
            self.game.hp.image = pg.transform.scale(pg.image.load('res/icon/hp.png').convert_alpha(),
                                                    (self.health * 3, 50))
        self.game.object_renderer.player_damage()
        self.check_game_over()

    def single_fire_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.shot and not self.game.weapon.reloading:
                self.shot = True
                self.game.weapon.reloading = True

    def movement(self):
        keys = pg.key.get_pressed()
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time * 1.5 if keys[pg.K_LSHIFT] else PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.check_wall_collision(dx, dy)
        self.angle %= math.tau

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def draw(self):
        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)

    def mouse_control(self):
        # pass
        mx, my = pg.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSITIVITY * self.game.delta_time

    def update(self):
        self.movement()
        self.mouse_control()
        self.recover_health()
        # print(self.pos)

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)
