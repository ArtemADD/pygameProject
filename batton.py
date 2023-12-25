import pygame as pg

all_sprites = pg.sprite.Group()
avt = pg.sprite.Group()
ckins = pg.sprite.Group()
Buttons = pg.sprite.Group()
scin = pg.sprite.Group()
hiro = pg.sprite.Group()

class Button(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, text, image_do, image_posle, mus, group=all_sprites):
        super().__init__(group, Buttons)
        self.x, self.y, self.width, self.height, self.text = x, y, width, height, text
        self.image_scin, self.mus_scin = image_do, mus
        self.image_do, self.image_posle = (pg.image.load(image_do).convert_alpha(),
                                           pg.image.load(image_posle).convert_alpha())
        self.image_do, self.image_posle = pg.transform.scale(self.image_do, (width, height)), \
            pg.transform.scale(self.image_posle, (width, height))
        self.image = self.image_do
        self.t = 0
        self.channel = pg.mixer.Channel(0)
        self.mus = pg.mixer.Sound(mus)
        self.mus.set_volume(0.5)
        self.rect = self.image_do.get_rect(topleft=(x, y))
        self.is_hovered = False

    def update(self, sc):
        image_con = self.image_posle if self.is_hovered else self.image_do
        self.image = image_con
        font = pg.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text = text_surface.get_rect(center=self.rect.center)
        sc.blit(text_surface, text)

    #  наведение мыши
    def check_hover(self, pos_mous):
        if self.x <= pos_mous[0] <= self.x + self.width and self.y <= pos_mous[1] <= self.y + self.height:
            self.is_hovered = True
        else:
            self.is_hovered = False
            self.t = 0

    #  музыка
    def music(self, event):
        if self.t == 0 and self.is_hovered:
            self.t += 1
            self.channel.play(self.mus)

    def grm(self, grom):
        self.mus.set_volume(grom)

    def up(self, image, image2, song, gr):
        self.image_do, self.image_posle = (pg.image.load(image).convert_alpha(),
                                           pg.image.load(image2).convert_alpha())
        self.image_do, self.image_posle = pg.transform.scale(self.image_do, (self.width, self.height)), \
            pg.transform.scale(self.image_posle, (self.width, self.height))
        self.image = self.image_do
        self.mus = pg.mixer.Sound(song)
        self.mus.set_volume(gr + 0.2)


