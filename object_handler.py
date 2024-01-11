from sprits_object import *
from npc import *
from map import *


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.static_sprit_path = 'res/sprite/'
        self.anim_sprit_path = 'res/sprite/animation_sprit/'
        # self.sprites = self.load_sprites()
        self.map_sprit()

    def map_sprit(self):
        add_sprite = self.add_sprite
        add_npc = self.add_npc

        # добавление спрайтов с карты
        for pos in map_sprites.keys():
            if map_sprites[pos] == 3:
                sp = AnimatedSprite(self.game, pos=pos, scale=1.25, shift=-0.0002)
            add_sprite(sp)

        # добавление врагов
        add_npc(NPC(self.game))

    def update(self):
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def clear_sprite(self):
        self.sprite_list = []
