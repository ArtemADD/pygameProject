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
                end()
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                pg.mouse.set_visible(True)
                return self.paus()
                # pg.quit()
                # sys.exit()
            self.player.single_fire_event(event)

    def run(self, m=1):
        self.new_game(m)
        pg.mixer.music.load('res/music/shvatca.mp3')
        pg.mixer.music.play(-1)
        while True:
            self.check_events()
            self.update()
            self.draw()

    def paus(self):
        pg.mixer.music.load('res/music/shvatca.mp3')
        pg.mixer.music.play(-1)
        self.pauselement()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end()
                    pg.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if self.ex.is_hovered:
                        return ocno.runsc()
                    if self.restarte.is_hovered:
                        pg.mouse.set_visible(False)
                        return True
                if event.type == pygame.MOUSEMOTION:
                    self.ex.check_hover(event.pos)
                    self.ex.music(event)
                    self.restarte.check_hover(event.pos)
                    self.restarte.music(event)
            self.screen.blit(self.fon, (0, 0))
            hiro.draw(self.screen)
            hiro.update(self.screen)
            pygame.display.flip()
            self.clock.tick(60)


    def pauselement(self):
        image = pygame.image.load('res/background/fonpaus.jpg')
        self.fon = pygame.transform.scale(image, (1600, 900))
        self.ex = Button(550, 300, 400, 100, 'Выйти в главное меню', 'res/icon/cnopcado.png',
                            'res/icon/cnopcapos.png',
                            'res/music/vhod.mp3', hiro)
        self.restarte = Button(550, 450, 400, 100, 'Вернуться к игре', 'res/icon/cnopcado.png',
                         'res/icon/cnopcapos.png',
                         'res/music/vhod.mp3', hiro)



if __name__ == '__main__':
    game = Game()
    # game.run()
    ocno = Open(game)
    ocno.runsc()
