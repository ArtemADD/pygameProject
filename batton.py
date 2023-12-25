import pygame as pg

all_sprites = pg.sprite.Group()
avt = pg.sprite.Group()


class Button(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, text, image_do, image_posle, mus, group=all_sprites):
        super().__init__(group)
        self.x, self.y, self.width, self.height, self.text = x, y, width, height, text
        self.image_do, self.image_posle = (pg.image.load(image_do).convert_alpha(),
                                           pg.image.load(image_posle).convert_alpha())
        self.image_do, self.image_posle = pg.transform.scale(self.image_do, (width, height)), \
            pg.transform.scale(self.image_posle, (width, height))
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
        if event.type == pg.MOUSEMOTION and self.is_hovered and self.t == 0:
            self.t += 1
            self.channel.play(self.mus)

