# PYGAME BOILERPLATE CODE
# JRYZKNS 2019

# TODO: package our game into exe file
# TODO: add feature to reset the game

import pygame as pg

from game_context import *
from lib import *
from cutscenes import StartScreen, EndScreen

pg.init()
game_win = pg.display.set_mode(res)

start_screen = StartScreen()
end_screen = EndScreen()

STATES = ("START", "PLAY", "END")
CURRENT_STATE = "START"

running = True

while running:

    # CALLBACKS
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if CURRENT_STATE == "START":
                    if start_screen.box.collidepoint(event.pos):
                        CURRENT_STATE = "PLAY"
                if CURRENT_STATE == "END":
                    CURRENT_STATE = "PLAY"
                    current_level = 1
                    tilemap, player_x, player_y = init_level(LVL_PATHS[current_level - 1], n_diamonds)
        elif event.type == pg.KEYDOWN:
            
            tilemap[player_y][player_x] = 0

            dx, dy = 0, 0

            if   event.key == pg.K_s:
                dy = 1
            elif event.key == pg.K_a:
                dx = -1
            elif event.key == pg.K_w:
                dy = -1
            elif event.key == pg.K_d:
                dx = 1

            if tilemap[player_y + dy][player_x + dx] == 1:
                dx, dy = 0, 0

            if not ((0 <= player_y + dy < tiles_high) 
                        and (0 <= player_x + dx < tiles_wide)):
                dx, dy = 0, 0

            player_x += dx
            player_y += dy

            if tilemap[player_y][player_x] == 3:
                diamonds_taken += 1
                if diamonds_taken == n_diamonds:
                    i, j = random.choice(where_0(tilemap))
                    tilemap[j][i] = 4
            elif tilemap[player_y][player_x] == 4:
                n_diamonds += 5
                diamonds_taken = 0
                current_level += 1
                if current_level > ttl_levels:
                    CURRENT_STATE = "END"
                    break
                tilemap, player_x, player_y = init_level(LVL_PATHS[current_level - 1], n_diamonds)

            tilemap[player_y][player_x] = 2

    game_win.fill((0,0,0))

    if CURRENT_STATE == "START":
        start_screen.draw(game_win)
    elif CURRENT_STATE == "PLAY":
        for i in range(res[0]//tile_length):
            for j in range(res[1]//tile_length):
                loc = (i * tile_length, j * tile_length)
                game_win.blit(tiles[tilemap[j][i]], loc)
    elif CURRENT_STATE == "END":
        end_screen.draw(game_win)
    else:
        print("Unknown State!")
        running = False

    pg.display.flip()