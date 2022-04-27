import pygame as pg,sys
from pygame.locals import *
import time

def game():
    player = 'x'
    winner = None
    draw = False
    width = 400
    height = 400
    white = (255, 255, 255)
    line_color = (10,10,10)

    board = [[None]*3,[None]*3,[None]*3]

    pg.init()
    fps = 30
    clock = pg.time.Clock()
    screen = pg.display.set_mode((width, height+100),0,32)
    pg.display.set_caption("Noughts & Crosses")
    
    opening = pg.image.load('opening.png')
    x_img = pg.image.load('x.png')
    o_img = pg.image.load('o.png')

    x_img = pg.transform.scale(x_img, (80,80))
    o_img = pg.transform.scale(o_img, (80,80))
    opening = pg.transform.scale(opening, (width, height+100))