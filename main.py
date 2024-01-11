import pygame as pg
import sys
from map import *
from raycasting import *
from player import *
from setting import *
from object_renderer import *
from zastavka import *
from sprits_object import *
from object_handler import *
from weapon import *
from sound import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        pg.mouse.set_visible(False)
        self.delta_time = 1
        self.num = None

    def new_game(self, m):
        self.map = Map(self, m)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self, self.num)
        self.object_hender = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.sound = Sound(self)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_hender.update()
        self.weapon.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        # self.screen.fill('black')
        self.object_renderer.draw()
        self.weapon.draw()
        pg.draw.circle(self.screen, 'white', (HALF_WIDTH, HALF_HEIGHT), 1)
        # self.map.draw()
        # self.player.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                # pg.mouse.set_visible(True)
                # return ocno.runsc()
                pg.quit()
                sys.exit()
            self.player.single_fire_event(event)

    def run(self, m=1):
        self.new_game(m)
        # pg.mixer.music.load('res/shvatca.mp3')
        # pg.mixer.music.play(-1)
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
    # ocno = Open(game)
    # ocno.runsc()
