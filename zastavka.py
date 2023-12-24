import pygame_textinput
import pygame
from main import *
import sys
import os
from batton import *
from object_renderer import *
from gromcost import Gromcost
from avtorizastia import *
from map import *

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

    def gamee(self, mini_map):
        pg.mixer.music.stop()
        self.game.run(mini_map)

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
                        return self.gamee(mini_map1)
                    elif self.zamok.is_hovered:
                        self.zamok.mus.stop()
                        pg.mouse.set_visible(False)
                        return self.gamee(mini_map2)
                    if self.ex.is_hovered:
                        self.terminate()
                    if self.record.is_hovered:
                        pass
                    if self.vhod.is_hovered:
                        return self.runav()
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
        self.login = ''
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
        self.exe = Button(600, 650, 400, 80, 'Вернуться', 'res/menuvhod.png', 'res/menuvhod2.png', 'res/vhod.mp3', avt)
        self.save = Button(600, 550, 400, 80, 'Войти', 'res/menuvhod.png', 'res/menuvhod2.png', 'res/vhod.mp3', avt)
        self.vvodlo = Button(300, 350, 400, 80, '', 'res/vvodlog.png', 'res/vvodlog.png', 'res/vhod.mp3', avt)
        self.vvodpar = Button(900, 350, 400, 80, '', 'res/vvodlog.png', 'res/vvodlog.png', 'res/vhod.mp3', avt)
        self.font = pygame.font.SysFont('arial', 50)



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
#запуск окна входа в акаунт
    def runav(self):
        clock = pg.time.Clock()
        flag = False
        active, active1 = False, False
        font = pygame.font.SysFont('arial', 50)
        self.text()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.terminate()
                if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                    if self.exe.is_hovered:
                        return self.runsc()
                    if self.vvodlo.is_hovered:
                        flag = not flag
                    if self.save.is_hovered:
                        rezalt, login = vhodifadm(self.vvodlo.text, self.vvodpar.text)
                        if rezalt:
                            self.login = login
                            self.vhod = Button(600, 300, 400, 80, self.login, 'res/login.png', 'res/login2.png',
                                               'res/vhod.mp3')
                            return self.runsc()
                        else:
                            self.resal = font.render(login, 10, (255, 0, 0))
                    if self.vvodlo.rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
                        self.user_text = ''
                    if self.vvodpar.rect.collidepoint(event.pos):
                        active1 = True
                    else:
                        active1 = False
                        self.user_text = ''
                if event.type == pg.MOUSEMOTION:
                    self.exe.chec_hover(event.pos)
                    self.exe.music(event)
                    self.save.chec_hover(event.pos)
                    self.save.music(event)
                if event.type == pygame.KEYDOWN and (active or active1):
                    if event.key == pygame.K_BACKSPACE:
                        self.user_text = self.user_text[:-1]
                    else:
                        self.user_text += event.unicode
            self.avto(active, active1)
            pg.display.flip()
            clock.tick(60)

    def text(self):
        self.base_font = pygame.font.Font(None, 32)
        self.user_text = ''
        font = pygame.font.SysFont('arial', 50)
        self.string_rendered = font.render('Пароль:', 10, (255, 0, 0))
        self.string_rendered1 = font.render('Логин:', 10, (255, 0, 0))
        self.resal = font.render('', 10, (255, 0, 0))
        self.intro_rect = self.string_rendered.get_rect().move(900, 300)
        self.intro_rect1 = self.string_rendered1.get_rect().move(300, 300)
        self.intro_rect2 = self.string_rendered1.get_rect().move(300, 100)


    def avto(self, active, active1):
        if active and self.vvodlo.text != self.user_text:
            self.vvodlo.text = self.user_text
        if active1 and self.vvodpar.text != self.user_text:
            self.vvodpar.text = self.user_text
        self.game.screen.blit(self.fon, (0, 0))
        self.game.screen.blit(self.string_rendered, self.intro_rect)
        self.game.screen.blit(self.string_rendered1, self.intro_rect1)
        self.game.screen.blit(self.resal, self.intro_rect2)
        avt.draw(self.game.screen)
        avt.update(self.game.screen)



