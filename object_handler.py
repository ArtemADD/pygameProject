from sprits_object import *
from npc import *
from map import *
from math import *


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.static_sprit_path = 'res/sprite/'
        self.anim_sprit_path = 'res/sprite/animation_sprit/'
        self.npc_positions = {}
        self.spawn_zone = [(6, 6), (6, 23), (6, 40), (23, 6), (23, 40), (40, 6), (40, 23), (40, 40)]
        # self.sprites = self.load_sprites()
        self.map_sprit()

    def map_sprit(self):
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}

        # добавление спрайтов с карты
        for pos in map_sprites.keys():
            if map_sprites[pos] == 3:
                sp = AnimatedSprite(self.game, pos=pos, scale=1.25, shift=-0.05)
            add_sprite(sp)

        # добавление врагов
        self.spawn_npc()

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        if all(list(map(lambda x: not x.alive, self.npc_list))):
            print(all(list(map(lambda x: not x.alive, self.npc_list))))
            self.npc_list.clear()
            self.spawn_npc()

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def spawn_npc(self):
        pl_x, pl_y = self.game.player.map_pos
        dists = {int(sqrt((x - pl_x) ** 2 + (y - pl_y) ** 2)): (x, y) for x, y in self.spawn_zone}
        s_x, s_y = dists[min(dists)]
        self.add_npc(NPC(self.game, pos=(s_x, s_y)))
        self.add_npc(NPC(self.game, pos=(s_x - 1, s_y)))
        self.add_npc(NPC(self.game, pos=(s_x + 1, s_y)))
        self.add_npc(NPC(self.game, pos=(s_x, s_y - 1)))
        self.add_npc(NPC(self.game, pos=(s_x, s_y + 1)))

    def clear_sprite(self):
        self.sprite_list.clear()
