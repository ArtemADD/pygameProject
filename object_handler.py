from sprits_object import *


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.static_sprit_path = 'res/sprite/'
        self.anim_sprit_path = 'res/sprite/animation_sprit/'
        self.map_sprit()

    def map_sprit(self):
        add_sprite = self.add_sprite
        # add_sprite(AnimatedSprite(self.game, pos=(9.75, 4.5), scale=1.25, shift=0.002))
        # add_sprite(AnimatedSprite(self.game, pos=(9.75, 7.5), scale=1.25, shift=0.002))
        # add_sprite(AnimatedSprite(self.game, pos=(8.75, 8.5), scale=1.25, shift=0.002))
        # add_sprite(AnimatedSprite(self.game, pos=(8.75, 3.5), scale=1.25, shift=0.002))
        add_sprite(AnimatedSprite(self.game, path='res/sprite/камин/fireplace0.png',
                                  pos=(12.5, 10.5), scale=0.75, shift=0.2))

    def update(self):
        [sprite.update() for sprite in self.sprite_list]

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
