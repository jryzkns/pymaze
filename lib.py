import pygame as pg
import random

def where_0(m):
    locs = []
    for i in range(len(m[0])):
        for j in range(len(m)):
            if m[j][i] == 0:
                locs.append((i,j))
    return locs

def init_level(lvl_path, n_diamonds = 10):
    with open(lvl_path, 'r') as level_file:
        tilemap = level_file.read()
        tilemap = tilemap.split('\n')
        for i in range(len(tilemap)):
            tilemap[i] = [int(val) for val in tilemap[i].split(',')]

    player_x, player_y = 1, 1
    for i in range(len(tilemap[0])):
        for j in range(len(tilemap)):
            if tilemap[j][i] == 2:
                player_x, player_y = i, j

    for loc in random.sample(where_0(tilemap), n_diamonds):
        a, b = loc
        tilemap[b][a] = 3

    return tilemap, player_x, player_y

def overlay_tile(top_path, bottom_path):
    tile = pg.image.load(bottom_path)
    obj = pg.image.load(top_path)
    tile.blit(obj,(0,0))
    return tile