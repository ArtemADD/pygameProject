import pygame as pg
from batton import all_sprites, ocnova


class Gromcost(pg.sprite.Sprite):
    def __init__(self, sc, x):
        super().__init__(all_sprites)
        self.sc = sc
        self.image = pg.image.load('res/icon/reg.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (x, 50))
        self.rect = self.image.get_rect().move(1250, 800)

class HP(pg.sprite.Sprite):
    def __init__(self, sc, x):
        super().__init__(ocnova)
        self.sc = sc
        self.image = pg.image.load('res/icon/hp.png').convert_alpha()
        self.image = pg.transform.scale(self.image, (x, 50))
        self.rect = self.image.get_rect().move(1250, 800)
