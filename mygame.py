import pygame
import os

from os import path
from pygame.locals import *

# import resource
game_folder = os.path.dirname(__file__)
dirt = pygame.transform.scale(pygame.image.load(os.path.join('img', 'dirt.png')), (170, 40))
whack1 = pygame.transform.scale(pygame.image.load(os.path.join('img', 'whack1.png')), (50, 70))
whack2 = pygame.transform.scale(pygame.image.load(os.path.join('img', 'whack2.png')), (70, 50))
zb = pygame.transform.scale(pygame.image.load(os.path.join('img', 'std_zombie.png')), (100, 100))
bg = pygame.transform.scale(pygame.image.load(os.path.join('img', 'lawn.png')), (800, 600))

WIDTH = 800
HEIGHT = 600
FPS = 60
BG = (17, 166, 41)
COL = 3
ROW = 3
mouse_pos = (0, 0)
cursor = whack1

def zombie_generator():
    

def draw_dirt():
    x,y = 0,0
    for row in range(ROW):
        x = 0
        for cal in range(COL):
            screen.blit(zb, (x * 200 + 150, y * 200 + 35))
            screen.blit(dirt, (x * 200 + 115, y * 200 + 120))
            x += 1
        y += 1


pygame.init()

# settings
pygame.display.set_caption("Whack-a-zombie")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

run = True
while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == MOUSEBUTTONDOWN: cursor = whack2
        else: cursor = whack1

        mouse_pos = pygame.mouse.get_pos()

    pygame.display.flip()

    screen.blit(bg, (0, 0))
    draw_dirt()
    screen.blit(cursor, (mouse_pos[0] - 25, mouse_pos[1] - 25))

pygame.quit()