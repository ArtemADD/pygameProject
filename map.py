import pygame as pg
from setting import *


def load_map(path):
    result = []
    with open(f'res/map/{path}', 'rt') as f:
        data = f.read().split('\n')
    for row in data:
        result_row = list()
        for col in row:
            if col == '_':
                result_row.append(False)
            else:
                result_row.append(int(col))
        result.append(result_row)
    return result


_ = False
mini_map1 = load_map('map1.txt')
mini_map2 = load_map('map2.txt')
m_m3 = load_map('map3.txt')
map_sprites = {}


class Map:
    def __init__(self, game, m):
        self.game = game
        self.m = m
        if m == 3:
            self.mini_map = m_m3
        elif m == 2:
            self.mini_map = mini_map2
        else:
            self.mini_map = mini_map1
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, val in enumerate(row):
                if val == 1 or val == 2:
                    self.world_map[(i, j)] = val
                elif val:
                    map_sprites[(i + 0.5, j + 0.5)] = val

    def draw(self):
        [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
         for pos in self.world_map]
