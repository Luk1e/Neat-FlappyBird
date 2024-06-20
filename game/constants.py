import os

import pygame

pygame.font.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
FLOOR = 730
STAT_FONT = pygame.font.Font('./static/fonts/Tiny5-Regular.ttf', 50)
END_FONT = pygame.font.Font('./static/fonts/Tiny5-Regular.ttf', 70)
DRAW_LINES = False

WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Flappy Bird")

pipe_img = pygame.transform.scale2x(pygame.image.load(os.path.join("./static/imgs", "pipe.png")).convert_alpha())
bg_img = pygame.transform.scale(pygame.image.load(os.path.join("./static/imgs", "sky.png")).convert_alpha(), (600, 900))
base_img = pygame.transform.scale2x(pygame.image.load(os.path.join("./static/imgs", "base.png")).convert_alpha())

gen = 0

def load_images(index):
    return  [pygame.transform.scale2x(pygame.image.load(os.path.join("./static/imgs/img" + str(index) + "/", "bird" + str(x) + ".png"))) for x in range(1, 4)]
