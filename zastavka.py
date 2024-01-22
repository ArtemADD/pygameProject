# import pygame_textinput
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
        image = pygame.image.load('res/background/fon.jpg')
        self.fon = pygame.transform.scale(image, (1600, 900))
        image = pygame.image.load('res/icon/name.png')
        self.name = pygame.transform.scale(image, (600, 100))
        self.flag2 = True
        self.zvuc = 0.1
        self.but()

    def terminate(self):
        pygame.quit()
        sys.exit()

    def gamee(self, mini_map):
        pg.mixer.music.stop()
        self.game.run(mini_map)

    def runsc(self):
        pg.mixer.music.load('res/music/fon.mp3')
        pg.mixer.music.play(-1)
        pg.mixer.music.set_volume(self.zvuc)
        clock = pygame.time.Clock()
        mus = True
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminate()
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if self.pustn.is_hovered and self.login != '':
                        self.pustn.mus.stop()
                        pg.mouse.set_visible(False)
                        return self.gamee(1)
                    elif self.zamok.is_hovered and self.login != '':
                        self.zamok.mus.stop()
                        pg.mouse.set_visible(False)
                        return self.gamee(2)
                    if self.login != '':
                        if self.acaunt.is_hovered:
                            return self.Avatar()
                    if self.ex.is_hovered:
                        self.terminate()
                    if self.record.is_hovered:
                        self.recordy()
                    if self.vhod.is_hovered:
                        return self.runav()
                    if self.gromcoste.is_hovered:
                        self.gromcost.image = pg.transform.scale(pg.image.load('res/icon/reg.png').convert_alpha(), (event.pos[0] - 1250, 50))
                        self.zvuc = (event.pos[0] - 1250) // 3 / 1000
                        if self.zvuc > 0.001:
                            self.vc.image_do = pg.transform.scale(pg.image.load('res/icon/vc.png').convert_alpha(),
                                                                  (50, 50))
                            self.vc.image_posle = pg.transform.scale(pg.image.load('res/icon/vcn.png').convert_alpha(),
                                                                     (50, 50))
                            mus = True
                        else:
                            self.vc.image_do = pg.transform.scale(pg.image.load('res/icon/vcl.png').convert_alpha(),
                                                                  (50, 50))
                            self.vc.image_posle = pg.transform.scale(pg.image.load('res/icon/vcl2.png').convert_alpha(),
                                                                     (50, 50))
                            mus = False
                        pg.mixer.music.set_volume(self.zvuc)
                        for item in Buttons:
                            item.grm(self.zvuc + 0.2)
                    if self.vc.is_hovered:
                        if mus:
                            self.vc.image_do = pg.transform.scale(pg.image.load('res/icon/vcl.png').convert_alpha(), (50, 50))
                            self.vc.image_posle = pg.transform.scale(pg.image.load('res/icon/vcl2.png').convert_alpha(), (50, 50))
                            self.gromcost.image = pg.transform.scale(pg.image.load('res/icon/reg.png').convert_alpha(),
                                                                     (0, 50))
                            pg.mixer.music.set_volume(0)
                            self.zvuc = 0
                            for item in Buttons:
                                item.grm(0)
                        else:
                            self.vc.image_do = pg.transform.scale(pg.image.load('res/icon/vc.png').convert_alpha(), (50, 50))
                            self.vc.image_posle = pg.transform.scale(pg.image.load('res/icon/vcn.png').convert_alpha(),
                                                                     (50, 50))
                            self.gromcost.image = pg.transform.scale(pg.image.load('res/icon/reg.png').convert_alpha(),
                                                                     (300, 50))
                            self.zvuc = 0.1
                            pg.mixer.music.set_volume(self.zvuc)
                            for item in Buttons:
                                item.grm(self.zvuc + 0.2)
                        mus = not mus
                if event.type == pygame.MOUSEMOTION:
                    self.clic(event)
            self.game.screen.blit(self.fon, (0, 0))
            self.game.screen.blit(self.name, (500, 170))
            all_sprites.draw(self.game.screen)
            all_sprites.update(self.game.screen)
            pygame.display.flip()
            clock.tick(60)

    def but(self):
        self.login = ''
        self.pustn = Button(100, 100, 400, 100, 'Египетские пирамиды', 'res/icon/cnopcado.png',
                            'res/icon/cnopcapos.png',
                            'res/music/vhod.mp3')
        self.zamok = Button(1100, 100, 400, 100, 'Заброшенный замок', 'res/icon/cnopcado.png',
                            'res/icon/cnopcapos.png',
                            'res/music/vhod.mp3')
        self.ex = Button(600, 600, 400, 80, 'Выход', 'res/icon/menuvhod.png', 'res/icon/menuvhod2.png',
                         'res/music/vhod.mp3')
        self.record = Button(600, 400, 400, 80, 'Рекорды', 'res/icon/menuvhod.png', 'res/icon/menuvhod2.png',
                             'res/music/vhod.mp3')
        self.vhod = Button(600, 500, 400, 80, 'Вход', 'res/icon/menuvhod.png', 'res/icon/menuvhod2.png',
                           'res/music/vhod.mp3')
        self.gromcoste = Button(1250, 800, 300, 50, '', 'res/icon/gromcost.png', 'res/icon/gromcost.png',
                                'res/music/vhod.mp3')
        self.vc = Button(1190, 803, 50, 50, '', 'res/icon/vc.png', 'res/icon/vcn.png', 'res/music/vhod.mp3')
        self.gromcost = Gromcost(self.game.screen, 300)
        self.exe = Button(600, 650, 400, 80, 'Вернуться', 'res/icon/menuvhod.png', 'res/icon/menuvhod2.png',
                          'res/music/vhod.mp3', avt)

        self.save = Button(600, 550, 400, 80, 'Войти', 'res/icon/menuvhod.png', 'res/icon/menuvhod2.png',
                           'res/music/vhod.mp3', avt)

        self.vvodlo = Button(300, 350, 400, 80, '', 'res/icon/vvodlog.png', 'res/icon/vvodlog.png', 'res/music/vhod.mp3',
                             avt)
        self.vvodpar = Button(900, 350, 400, 80, '', 'res/icon/vvodlog.png', 'res/icon/vvodlog.png',
                              'res/music/vhod.mp3', avt)
        self.font = pygame.font.SysFont('arial', 50)
        self.rama = Button(165, 155, 310, 310, '', 'res/icon/scinplaer.png', 'res/icon/scinplaer.png',
                           'res/music/vhod.mp3', scin)

    def clic(self, event):
        self.zamok.check_hover(event.pos)
        self.pustn.check_hover(event.pos)
        self.ex.check_hover(event.pos)
        self.record.check_hover(event.pos)
        self.vhod.check_hover(event.pos)
        self.gromcoste.check_hover(event.pos)
        if self.login != '':
            self.acaunt.check_hover(event.pos)
            self.acaunt.music(event)
        self.vhod.music(event)
        self.record.music(event)
        self.zamok.music(event)
        self.ex.music(event)
        self.pustn.music(event)
        self.vc.check_hover(event.pos)
    # запуск окна входа в аккаунт

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
                            if self.login == '':
                                self.login = login
                                self.acaunt = Button(600, 300, 400, 80, self.login, 'res/icon/login.png', 'res/icon/login2.png',
                                                   'res/music/vhod.mp3')
                                self.scinplaer = Button(170, 150, 300, 300, '', scina()[0], scina()[0], scina()[1], scin)
                            else:
                                self.login = login
                                self.acaunt.text = self.login
                                self.scinplaer.up(scina()[0], scina()[0], scina()[1], self.zvuc)
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
                    self.exe.check_hover(event.pos)
                    self.exe.music(event)
                    self.save.check_hover(event.pos)
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

    def butscin(self):

        self.exee = Button(170, 600, 300, 80, 'Вернуться', 'res/icon/menuvhod.png', 'res/icon/menuvhod2.png',
                           'res/music/vhod.mp3',
                           scin)
        self.savee = Button(170, 500, 300, 80, 'Сохранить', 'res/icon/menuvhod.png', 'res/icon/menuvhod2.png',
                            'res/music/vhod.mp3', scin)

        self.rama2 = Button(490, 155, 990, 660, '', 'res/icon/opisanie.png', 'res/icon/opisanie.png',
                            'res/music/vhod.mp3', scin)
        self.scin1 = Button(500, 165, 300, 300, '', 'res/icon/FlareFemaleHero1.png', 'res/icon/FlareFemaleHero1.png',
                            'res/music/женский голос больно.mp3', scin)
        self.scin2 = Button(820, 165, 300, 300, '', 'res/icon/FlareFemaleHero2.png', 'res/icon/FlareFemaleHero2.png',
                            'res/music/ДевушкаЭльф.mp3', scin)
        self.scin3 = Button(1140, 165, 300, 300, '', 'res/icon/FlareFemaleHero3.png', 'res/icon/FlareFemaleHero3.png',
                            'res/music/женские лучшие.mp3', scin)
        self.scin4 = Button(500, 485, 300, 300, '', 'res/icon/FlareMaleHero1.png', 'res/icon/FlareMaleHero1.png',
                            'res/music/Мужской вставай.mp3', scin)
        self.scin5 = Button(820, 485, 300, 300, '', 'res/icon/FlareMaleHero2.png', 'res/icon/FlareMaleHero2.png',
                            'res/music/Грозный мужчина.mp3', scin)
        self.scin6 = Button(1140, 485, 300, 300, '', 'res/icon/FlareMaleHero3.png', 'res/icon/FlareMaleHero3.png',
                            'res/music/Муж голос добыча.mp3', scin)

    def scinif(self, event):
        if self.exee.is_hovered:
            return self.runsc()
        if self.savee.is_hovered:
            update(self.scinplaer.image_scin, self.scinplaer.mus_scin)
            return self.runsc()
        if self.scinplaer.is_hovered:
            self.scinplaer.music(event)
            self.scinplaer.t = 0
        if self.scin1.is_hovered:
            self.scin1.music(event)
            self.scin1.t = 0
            self.scinplaer.image_scin, self.scinplaer.mus_scin = self.scin1.image_scin, self.scin1.mus_scin
            self.scinplaer.image_do, self.scinplaer.image_posle, self.scinplaer.mus = \
                self.scin1.image_do, self.scin1.image_posle, self.scin1.mus
        if self.scin2.is_hovered:
            self.scin2.music(event)
            self.scin2.t = 0
            self.scinplaer.image_scin, self.scinplaer.mus_scin = self.scin2.image_scin, self.scin2.mus_scin
            self.scinplaer.image_do, self.scinplaer.image_posle, self.scinplaer.mus = \
                self.scin2.image_do, self.scin2.image_posle, self.scin2.mus
        if self.scin3.is_hovered:
            self.scin3.music(event)
            self.scin3.t = 0
            self.scinplaer.image_scin, self.scinplaer.mus_scin = self.scin3.image_scin, self.scin3.mus_scin
            self.scinplaer.image_do, self.scinplaer.image_posle, self.scinplaer.mus = \
                self.scin3.image_do, self.scin3.image_posle, self.scin3.mus
        if self.scin4.is_hovered:
            self.scin4.music(event)
            self.scin4.t = 0
            self.scinplaer.image_scin, self.scinplaer.mus = self.scin4.image_scin, self.scin4.mus_scin
            self.scinplaer.image_do, self.scinplaer.image_posle, self.scinplaer.mus = \
                self.scin4.image_do, self.scin4.image_posle, self.scin4.mus
        if self.scin5.is_hovered:
            self.scin5.music(event)
            self.scin5.t = 0
            self.scinplaer.image_scin, self.scinplaer.mus_scin = self.scin5.image_scin, self.scin5.mus_scin
            self.scinplaer.image_do, self.scinplaer.image_posle, self.scinplaer.mus = \
                self.scin5.image_do, self.scin5.image_posle, self.scin5.mus
        if self.scin6.is_hovered:
            self.scin6.music(event)
            self.scin6.t = 0
            self.scinplaer.image_scin, self.scinplaer.mus_scin = self.scin6.image_scin, self.scin6.mus_scin
            self.scinplaer.image_do, self.scinplaer.image_posle, self.scinplaer.mus = \
                self.scin6.image_do, self.scin6.image_posle, self.scin6.mus

    def scinmaus(self, event):
        self.scin1.check_hover(event.pos)
        self.scin2.check_hover(event.pos)
        self.scin3.check_hover(event.pos)
        self.scin4.check_hover(event.pos)
        self.scin5.check_hover(event.pos)
        self.scin6.check_hover(event.pos)
        self.scinplaer.check_hover(event.pos)
        self.exee.check_hover(event.pos)
        self.savee.check_hover(event.pos)
        self.exee.music(event)
        self.savee.music(event)

    def Avatar(self):
        if self.flag2:
            self.butscin()
            self.flag2 = False
        clock = pg.time.Clock()
        pg.mixer.music.load('res/music/fonscin.mp3')
        pg.mixer.music.play(-1)
        pg.mixer.music.set_volume(self.zvuc)
        image2 = pygame.image.load('res/background/fon2.jpg')
        self.fon2 = pygame.transform.scale(image2, (1600, 900))
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.terminate()
                if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                    self.scinif(event)
                if event.type == pygame.MOUSEMOTION:
                    self.scinmaus(event)
            self.game.screen.blit(self.fon2, (0, 0))
            scin.draw(self.game.screen)
            scin.update(self.game.screen)
            pg.display.flip()
            clock.tick(60)

    def recordy(self):
        clock = pg.time.Clock()
        self.exeee = Button(170, 600, 300, 80, 'Вернуться', 'res/icon/menuvhod.png', 'res/icon/menuvhod2.png',
                           'res/music/vhod.mp3',
                           record)
        pg.mixer.music.load('res/music/fonscin.mp3')
        pg.mixer.music.play(-1)
        pg.mixer.music.set_volume(self.zvuc)
        image2 = pygame.image.load('res/background/fon2.jpg')
        self.fon2 = pygame.transform.scale(image2, (1600, 900))
        self.recorde()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.terminate()
                if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                    if self.exeee.is_hovered:
                        return self.runsc()
                if event.type == pygame.MOUSEMOTION:
                    self.exeee.check_hover(event.pos)
                    self.exeee.music(event)
            self.game.screen.blit(self.fon2, (0, 0))
            record.draw(self.game.screen)
            record.update(self.game.screen)
            pg.display.flip()
            clock.tick(60)

    def recorde(self):
        t = recorda()
        t.sort(key=lambda i: i[1], reverse=True)
        for i in range(5):
            Button(600, 100+120*i, 400, 100, 'Игрок:' + str(t[i][0])+' Рекорд: '+str(t[i][1]), 'res/icon/cnopcapos.png',
                            'res/icon/cnopcado.png',
                            'res/music/vhod.mp3', record)
