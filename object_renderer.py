import pygame as pg
from map import *
from setting import *


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_offset = 0
        self.bg_1 = self.get_texture('res/background/bg_1.png', (WIDTH, HALF_HEIGHT))
        self.bg_2 = self.get_texture('res/background/bg_2_2.png', (WIDTH, HALF_HEIGHT))
        self.flor1 = self.get_texture('res/background/flor1.png', (WIDTH, HALF_HEIGHT))
        self.blood_screen = self.get_texture('res/damage/blood_screen.png', RES)

    def draw(self):
        self.draw_background()
        self.render_game_objects()

    def player_damage(self):
        self.screen.blit(self.blood_screen, (0, 0))

    def draw_background(self):
        # self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % WIDTH
        # self.screen.blit(self.wall_textures[2], (-self.sky_offset, 0))
        # self.screen.blit(self.wall_textures[2], (-self.sky_offset + WIDTH, 0))
        # pg.draw.rect(self.screen, '#6a5f31', (0, 0, WIDTH, HALF_HEIGHT))
        # pg.draw.rect(self.screen, '#6a5f31', (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))
        if self.game.map.m == 2:
            bg = self.bg_2
            fl = self.flor1
        else:
            bg = self.bg_1
            fl = self.flor1
        self.screen.blit(bg, (0, 0))
        self.screen.blit(fl, (0, HALF_HEIGHT))
        # self.screen.fill('black')

    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            # image.set_alpha(int(255 / (0.1 + depth ** 5 * 0.00002)))
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
                1: self.get_texture('res/textures/wall1.png'),
                2: self.get_texture('res/textures/stone wall 6.png'),
        }
