import pygame
from main import *
import sys
import os
from batton import *
from object_renderer import *
from gromcost import Gromcost

class Open:
    def __init__(self, game):
        self.game = game
        pg.mouse.set_visible(True)
        image = pygame.image.load('res/fon.jpg')
        self.fon = pygame.transform.scale(image, (1600, 900))
        pg.mixer.music.load('res/fon.mp3')
        pg.mixer.music.play(-1)
        self.but()

    def terminate(self):
        pygame.quit()
        sys.exit()

    def gamee(self):
        pg.mixer.music.stop()
        self.game.run()

    def runsc(self):
        clock = pygame.time.Clock()
        mus = True
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if self.pustn.is_hovered:
                        self.pustn.mus.stop()
                        pg.mouse.set_visible(False)
                        return self.gamee()
                    elif self.zamok.is_hovered:
                        self.zamok.mus.stop()
                        pg.mouse.set_visible(False)
                        return self.gamee()
                    if self.ex.is_hovered:
                        self.terminate()
                    if self.record.is_hovered:
                        pass
                    if self.vhod.is_hovered:
                        pass
                    if self.gromcoste.is_hovered:
                        self.gromcost.image = pg.transform.scale(pg.image.load('res/reg.png').convert_alpha(), (event.pos[0] - 1250, 50))
                        pg.mixer.music.set_volume((event.pos[0] - 1250) // 3 / 100)
                    if self.vc.is_hovered:
                        if mus:
                            self.vc.image_do = pg.transform.scale(pg.image.load('res/vcl.png').convert_alpha(), (50, 50))
                            self.vc.image_posle = pg.transform.scale(pg.image.load('res/vcl2.png').convert_alpha(), (50, 50))
                            self.gromcost.image = pg.transform.scale(pg.image.load('res/reg.png').convert_alpha(),
                                                                     (0, 50))
                            pg.mixer.music.set_volume(0)
                        else:
                            self.vc.image_do = pg.transform.scale(pg.image.load('res/vc.png').convert_alpha(), (50, 50))
                            self.vc.image_posle = pg.transform.scale(pg.image.load('res/vcn.png').convert_alpha(),
                                                                     (50, 50))
                            self.gromcost.image = pg.transform.scale(pg.image.load('res/reg.png').convert_alpha(),
                                                                     (300, 50))
                            pg.mixer.music.set_volume(1)
                        mus = not mus
                if event.type == pygame.MOUSEMOTION:
                    self.clic(event)
            self.game.screen.blit(self.fon, (0, 0))
            all_sprites.draw(self.game.screen)
            all_sprites.update(self.game.screen)
            pygame.display.flip()
            clock.tick(60)

    def but(self):
        self.pustn = Button(100, 100, 400, 100, 'Египетские пиромиды', 'res/cnopcado.png', 'res/cnopcapos.png',
                            'res/vhod.mp3')
        self.zamok = Button(1100, 100, 400, 100, 'Заброшеный замок', 'res/cnopcado.png', 'res/cnopcapos.png',
                            'res/vhod.mp3')
        self.ex = Button(600, 600, 400, 80, 'Выход', 'res/menuvhod.png', 'res/menuvhod2.png', 'res/vhod.mp3')
        self.record = Button(600, 400, 400, 80, 'Рекорды', 'res/menuvhod.png', 'res/menuvhod2.png', 'res/vhod.mp3')
        self.vhod = Button(600, 500, 400, 80, 'Вход', 'res/menuvhod.png', 'res/menuvhod2.png', 'res/vhod.mp3')
        self.gromcoste = Button(1250, 800, 300, 50, '', 'res/gromcost.png', 'res/gromcost.png', 'res/vhod.mp3')
        self.vc = Button(1190, 803, 50, 50, '', 'res/vc.png', 'res/vcn.png', 'res/vhod.mp3')
        self.gromcost = Gromcost(self.game.screen, 300)

    def clic(self, event):
        self.zamok.chec_hover(event.pos)
        self.pustn.chec_hover(event.pos)
        self.ex.chec_hover(event.pos)
        self.record.chec_hover(event.pos)
        self.vhod.chec_hover(event.pos)
        self.gromcoste.chec_hover(event.pos)
        self.vhod.music(event)
        self.record.music(event)
        self.zamok.music(event)
        self.ex.music(event)
        self.pustn.music(event)
        self.vc.chec_hover(event.pos)



