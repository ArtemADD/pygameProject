import pygame as pg
from sprits_object import *
from random import randint, random, choice


class NPC(AnimatedSprite):
    def __init__(self, game, path='res/sprite/enemy/mummy/0.png', pos=(9, 24),
                 scale=0.8, shift=0.2, animation_time=500):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.walk_images = self.get_images(self.path + '/walk')
        self.idle_images = self.get_images(self.path + '/idle')
        self.pain_images = self.get_images(self.path + '/pain')

        self.attack_dist = randint(3, 6)
        self.speed = 0.03
        self.size = 10
        self.health = 100
        self.attack_damage = 10
        self.alive = True
        self.pain = False
        self.ray_cast_value = False

    def update(self):
        self.check_animation_time()
        self.get_sprite()
        self.run_logic()

    def animate_pain(self):
        self.animate(self.pain_images)
        print('ok')
        if self.animation_trigger:
            self.pain = False

    def check_hit_in_npc(self):
        if self.ray_cast_value and self.game.player.shot:
            if HALF_WIDTH - self.sprite_half_width < self.screen_x < HALF_WIDTH + self.sprite_half_width:
                self.game.player.shot = False
                self.pain = True

    def run_logic(self):
        if self.alive:
            self.ray_cast_value = self.ray_cast_player_npc()
            self.check_hit_in_npc()
            if self.pain:
                self.animate_pain()
            else:
                self.animate(self.idle_images)

    @property
    def map_pos(self):
        return int(self.x), int(self.y)

    def ray_cast_player_npc(self):
        if self.game.player.map_pos == self.map_pos:
            return True

        wall_dist_v, wall_dist_h = 0, 0
        player_dist_v, player_dist_h = 0, 0

        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        ray_angle = self.theta + 0.00001
        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)

        #  Горизонтальное пересечение луча со стеной
        y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

        depth_hor = (y_hor - oy) / sin_a
        x_hor = ox + depth_hor * cos_a

        delta_depth = dy / sin_a
        dx = delta_depth * cos_a

        for i in range(MAX_DEPTH):
            title_hor = int(x_hor), int(y_hor)
            if title_hor == self.map_pos:
                player_dist_h = depth_hor
                break
            if title_hor in self.game.map.world_map:
                wall_dist_h = depth_hor
                break
            x_hor += dx
            y_hor += dy
            depth_hor += delta_depth

        #  Вертикальное пересечение луча со стеной
        x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

        depth_vert = (x_vert - ox) / cos_a
        y_vert = oy + depth_vert * sin_a

        delta_depth = dx / cos_a
        dy = delta_depth * sin_a

        for i in range(MAX_DEPTH):
            title_vert = int(x_vert), int(y_vert)
            if title_vert == self.map_pos:
                player_dist_v = depth_vert
                break
            if title_vert in self.game.map.world_map:
                wall_dist_v = depth_vert
                break
            x_vert += dx
            y_vert += dy
            depth_vert += delta_depth

        player_dist = max(player_dist_v, player_dist_h)
        wall_dist = max(wall_dist_v, wall_dist_h)

        if 0 < player_dist < wall_dist or not wall_dist:
            return True
        return False




