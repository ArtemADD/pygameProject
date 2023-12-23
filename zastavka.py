import pygame
from main import *
import sys
import os
from batton import *
from object_renderer import *

class Open:
    def __init__(self, game):
        self.game = game
        pg.mouse.set_visible(True)
        image = pygame.image.load('res/fon.jpg')
        fon = pygame.transform.scale(image, (1600, 900))
        self.game.screen.blit(fon, (0, 0))
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
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
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
                if event.type == pygame.MOUSEMOTION:
                    self.clic(event)
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

    def clic(self, event):
        self.zamok.chec_hover(event.pos)
        self.pustn.chec_hover(event.pos)
        self.ex.chec_hover(event.pos)
        self.record.chec_hover(event.pos)
        self.vhod.chec_hover(event.pos)
        self.vhod.music(event)
        self.record.music(event)
        self.zamok.music(event)
        self.ex.music(event)
        self.pustn.music(event)

