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
from gromcost import HP


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
        self.end = False

    def new_game(self, m):
        self.start = True
        self.map = Map(self, m)
        self.player = Player(self)
        self.sound = Sound(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self, self.num)
        self.pathfinding = PathFinding(self)
        self.object_handler = ObjectHandler(self)
        # оружие
        self.weapon_bow = Weapon(self, 35, 20, scale=2.4,
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
                # end()
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1 and self.start:
                    self.cinzhal.is_hovered = True
                    self.lyc.is_hovered = False
                    self.weapon = self.weapon_sword
                elif event.key == pg.K_2 and self.start:
                    self.cinzhal.is_hovered = False
                    self.lyc.is_hovered = True
                    self.weapon = self.weapon_bow
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                pg.mouse.set_visible(True)
                return self.paus()
            if self.end:
                pg.mouse.set_visible(True)
                self.rezultat()
                self.player.health = PLAYER_MAX_HEALTH
                self.end = False
                self.player.rezult = 0
                return ocno.runsc()
                # sys.exit()
            self.player.single_fire_event(event)
        ocnova.update(self.screen)
        ocnova.draw(self.screen)

    def element(self):
        self.cinzhal = Button(700, 800, 100, 100, '', 'res/icon/кинжал.png', 'res/icon/кинжал2.png', 'res/music/vhod.mp3', ocnova)
        self.lyc = Button(800, 800, 100, 100, '', 'res/icon/лук.png', 'res/icon/лук2.png', 'res/music/vhod.mp3', ocnova)
        self.cinzhal.is_hovered = True
        self.lyc.is_hovered = False
        self.gromcoste = Button(1250, 800, 300, 50, '', 'res/icon/gromcost.png', 'res/icon/gromcost.png',
                                'res/music/vhod.mp3', ocnova)
        self.gromcost = HP(self.screen, 300)

    def run(self, m=1):
        self.new_game(m)
        self.element()
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
                    ende()
                    pg.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
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
        self.ex = Button(600, 300, 400, 100, 'Выйти в главное меню', 'res/icon/cnopcado.png',
                            'res/icon/cnopcapos.png',
                            'res/music/vhod.mp3', hiro)
        self.restarte = Button(600, 450, 400, 100, 'Вернуться к игре', 'res/icon/cnopcado.png',
                         'res/icon/cnopcapos.png',
                         'res/music/vhod.mp3', hiro)

    def rezultat(self):
        pg.mixer.music.load('res/music/shvatca.mp3')
        pg.mixer.music.play(-1)
        self.endlement()
        self.restartet.text = str(self.player.rezult * 100)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ende()
                    pg.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if self.exet.is_hovered:
                        for i in rezalt:
                            i.kill()
                            rezul(self.player.rezult * 100)
                        return True
                if event.type == pygame.MOUSEMOTION:
                    self.exet.check_hover(event.pos)
                    self.exet.music(event)
            self.screen.blit(self.fon, (0, 0))
            rezalt.draw(self.screen)
            rezalt.update(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

    def endlement(self):
        image = pygame.image.load('res/background/fonpaus.jpg')
        self.fon = pygame.transform.scale(image, (1600, 900))
        self.exet = Button(600, 450, 400, 100, 'Выйти в главное меню', 'res/icon/cnopcado.png',
                            'res/icon/cnopcapos.png',
                            'res/music/vhod.mp3', rezalt)
        self.restartet = Button(600, 300, 400, 100, '', 'res/icon/cnopcado.png',
                         'res/icon/cnopcapos.png',
                         'res/music/vhod.mp3', rezalt)


if __name__ == '__main__':
    game = Game()
    # game.run()
    ocno = Open(game)
    ocno.runsc()
