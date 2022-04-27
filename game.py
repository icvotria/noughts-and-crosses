import pygame as pg,sys
from pygame.locals import *
import time

player = 'x'
winner = None
draw = False
width = 400
height = 400
white = (255, 255, 255)
line_color = (10,10,10)

board = [[None]*3,[None]*3,[None]*3]