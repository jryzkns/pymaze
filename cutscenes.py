import pygame as pg
import os

class StartScreen:
    def __init__(self):
        self.splash = pg.image.load(os.path.join("res","start_splash.png"))
        self.box = pg.Rect(0,0,600,300)

    def draw(self, surf):
        surf.blit(self.splash, (0,0))

class EndScreen:
    def __init__(self):
        self.splash = pg.image.load(os.path.join("res","end_splash.png"))

    def draw(self, surf):
        surf.blit(self.splash, (0,0))