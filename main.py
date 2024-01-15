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
from pathfinding import *
from sound import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        pg.mouse.set_visible(False)
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 1000)
        self.num = None
        self.start = False

    def new_game(self, m):
        self.start = True
        self.map = Map(self, m)
        self.player = Player(self)
        self.sound = Sound(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self, self.num)
        self.pathfinding = PathFinding(self)
        self.object_handler = ObjectHandler(self)
        self.weapon_bow = Weapon(self, 30, 20, scale=2.4,
                                 sounds=[self.sound.bowstring, self.sound.shot_bow])
        self.weapon_sword = Weapon(self, 70, 3, path='res/sprite/weapon/sword/sword_0.png', scale=0.75,
                                   type_w='sword')
        self.weapon = self.weapon_sword

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
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
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.start = False
                    # pg.mouse.set_visible(True)
                    # return ocno.runsc()
                    pg.quit()
                    sys.exit()
                elif event.key == pg.K_1 and self.start:
                    self.weapon = self.weapon_sword
                elif event.key == pg.K_2 and self.start:
                    self.weapon = self.weapon_bow
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
