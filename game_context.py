import pygame as pg
from lib import *
import os

res = (600, 300)

FLOOR_ID   = 0
WALL_ID    = 1
PLAYER_ID  = 2
DIAMOND_ID = 3
PORTAL_ID  = 4

tiles = {
    FLOOR_ID   : pg.image.load(os.path.join("res", "floor.png")),
    WALL_ID    : pg.image.load(os.path.join("res", "wall.png")),
    PLAYER_ID  : overlay_tile(os.path.join("res", "player.png"), os.path.join("res", "floor.png")),
    DIAMOND_ID : overlay_tile(os.path.join("res", "diamond.png"), os.path.join("res", "floor.png")),
    PORTAL_ID  : overlay_tile(os.path.join("res", "portal.png"), os.path.join("res", "floor.png"))
}

tile_length = 30

tiles_wide, tiles_high = 20, 10

LVL_PATHS = (   'lvl1.mazelevel',
                'lvl2.mazelevel')
current_level = 1
ttl_levels = len(LVL_PATHS)

n_diamonds, diamonds_taken = 10, 0
tilemap, player_x, player_y = init_level(LVL_PATHS[current_level - 1],n_diamonds)
