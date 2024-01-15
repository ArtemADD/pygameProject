from sprits_object import *


class Weapon(AnimatedSprite):
    def __init__(self, game, damage, attack_range, path='res/sprite/weapon/bow/bow0.png', scale=1,
                 animation_time=300, sounds=False, type_w='bow'):
        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        self.reloading = False
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = damage
        self.range = attack_range
        self.sound = sounds
        self.type = type_w

    def animate_shot(self):
        if self.reloading:
            self.game.player.shot = False
            if self.animation_trigger:
                self.images.rotate(-1)
                self.image = self.images[0]
                self.frame_counter += 1
                if self.type == 'bow':
                    if self.frame_counter == 1:
                        self.game.sound.bowstring.play()
                    if self.frame_counter == 4:
                        self.game.sound.shot_bow.play()
                # elif self.type:
                #
                if self.frame_counter == self.num_images:
                    self.reloading = False
                    self.frame_counter = 0

    def draw(self):
        self.game.screen.blit(self.images[0], self.weapon_pos)

    def update(self):
       self.check_animation_time()
       self.animate_shot()
