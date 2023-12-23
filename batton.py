import pygame as pg

all_sprites = pg.sprite.Group()

class Button(pg.sprite.Sprite):
    def __init__(self, x, y, weght, hight, text, image_do, image_posle, mus):
        super().__init__(all_sprites)
        self.x, self.y, self.weght, self.hight, self.text = x, y, weght, hight, text
        self.image_do, self.image_posle = pg.image.load(image_do).convert_alpha(), pg.image.load(image_posle).convert_alpha()
        self.image_do, self.image_posle = pg.transform.scale(self.image_do, (weght, hight)), \
            pg.transform.scale(self.image_posle, (weght, hight))
        self.image = self.image_do
        self.t = 0
        self.channel = pg.mixer.Channel(0)
        self.mus = pg.mixer.Sound(mus)
        self.rect = self.image_do.get_rect(topleft=(x, y))
        self.is_hovered = False

    def update(self, sc):
        image_con = self.image_posle if self.is_hovered else self.image_do
        self.image = image_con
        font = pg.font.Font(None, 36)
        text_surfase = font.render(self.text, True, (255, 255, 255))
        text = text_surfase.get_rect(center=self.rect.center)
        sc.blit(text_surfase, text)

    #наведение мышы
    def chec_hover(self, pos_mous):
        if self.x <= pos_mous[0] <= self.x + self.weght and self.y <= pos_mous[1] <= self.y + self.hight:
            self.is_hovered = True
        else:
            self.is_hovered = False
            self.t = 0

    #музыка
    def music(self, event):
        if event.type == pg.MOUSEMOTION and self.is_hovered and self.t == 0:
            self.t += 1
            self.channel.play(self.mus)

