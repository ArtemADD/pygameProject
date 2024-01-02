import math
import os
from collections import deque
import pygame as pg
from setting import *

class SpritObject:
    def __init__(self, game, path='res/sprite/table.png', pos=(10.5, 9.5), scale=0.5, shift=0.7):
        self.game = game
        self.player = game.player
        self.x, self.y = pos
        self.image = pg.image.load(path).convert_alpha()
        self.IMAGE_WIDTH = self.image.get_width()
        self.IMAGE_HALF_WIDHT = self.image.get_width() // 2
        self.IMAGE_RATIO = self.IMAGE_WIDTH / self.image.get_height()
        self.dx, self.dy, self.theta, self.screen_x, self.dist, self.norm_dist = 0, 0, 0, 0, 1, 1
        self.sprite_half_widht = 0
        self.SPRITE_HIDHT_SHIFT = shift
        self.SPRITE_SCALE = scale

    def get_sprite_projection(self):
        proj = SCREEN_DIST / self.norm_dist * self.SPRITE_SCALE
        proj_widht, proj_heigth = proj * self.IMAGE_RATIO, proj

        image = pg.transform.scale(self.image, (proj_widht, proj_heigth))

        self.sprite_half_widht = proj_widht // 2
        hidth_shift = proj_heigth * self.SPRITE_HIDHT_SHIFT
        pos = self.screen_x - self.sprite_half_widht, HALF_HEIGHT - proj_heigth // 2 + hidth_shift

        self.game.raycasting.objects_to_render.append((self.norm_dist, image, pos))

    def get_sprite(self):
        dx = self.x - self.player.x
        dy = self.y - self.player.y
        self.dx, self.dy = dx, dy
        self.theta = math.atan2(dy, dx)

        delta = self.theta - self.player.angle
        if (dx > 0 and self.player.angle > math.pi) or (dx < 0 and dy < 0):
            delta += math.tau
        delta_rays = delta / DELTA_ANGLE
        self.screen_x = (HALF_NUM_RAYS + delta_rays) * SCALE

        self.dist = math.hypot(dx, dy)
        self.norm_dist = self.dist * math.cos(delta)
        if -self.IMAGE_HALF_WIDHT < self.screen_x < (WIDTH + self.IMAGE_HALF_WIDHT) and self.norm_dist > 0.5:
            self.get_sprite_projection()

    def update(self):
        self.get_sprite()


class AnimatedSprite(SpritObject):
    def __init__(self, game, path='res/sprite/animation_sprit/0.png', pos=(10.5, 9.5), scale=0.5, shift=0.7, animation_time=120):
        super().__init__(game, path, pos, scale, shift)
        self.animation_time = animation_time
        self.path = path.rsplit('/', 1)[0]
        self.images = self.get_images(self.path)
        self.animation_time_prev = pg.time.get_ticks()
        self.animation_triger = False

    def update(self):
        super().update()
        self.check_animation_time()
        self.animate(self.images)

    def animate(self, images):
        if self.animation_triger:
            images.rotate(-1)
            self.image = images[0]

    def check_animation_time(self):
        self.animation_triger = False
        time_now = pg.time.get_ticks()
        if time_now - self.animation_time_prev > self.animation_time:
            self.animation_time_prev = time_now
            self.animation_triger = True

    def get_images(self, path):
        images = deque()
        for file_name in os.listdir(path):
            if os.path.isfile(os.path.join(path, file_name)):
                img = pg.image.load(path + '/' + file_name).convert_alpha()
                images.append(img)
        return images