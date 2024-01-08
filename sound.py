import pygame as pg


class Sound:
    def __init__(self, game):
        self.game = game
        self.path = 'res/music/'
        self.shot_bow = pg.mixer.Sound(self.path + 'shot_bow.mp3')
        self.bowstring = pg.mixer.Sound(self.path + 'bowstring.mp3')
