import pygame as pg
from setting import *


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_offset = 0
        self.background = self.get_texture('res/bc_4.png', (WIDTH, HALF_HEIGHT))

    def draw(self):
        self.draw_background()
        self.render_game_objects()

    def draw_background(self):
        # self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % WIDTH
        # self.screen.blit(self.wall_textures[2], (-self.sky_offset, 0))
        # self.screen.blit(self.wall_textures[2], (-self.sky_offset + WIDTH, 0))
        # pg.draw.rect(self.screen, '#6a5f31', (0, 0, WIDTH, HALF_HEIGHT))
        # pg.draw.rect(self.screen, '#6a5f31', (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))
        self.screen.blit(self.background, (0, 0))
        bc = pg.transform.flip(self.background, flip_y=True, flip_x=False)
        self.screen.blit(bc, (0, HALF_HEIGHT))

    def render_game_objects(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            image.set_alpha(int(255 / (0.1 + depth ** 5 * 0.00002)))
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
                1: self.get_texture('res/wall1.png'),
                2: self.get_texture('res/stone wall 6.png'),
                3: self.get_texture('res/wall3.png')
        }
