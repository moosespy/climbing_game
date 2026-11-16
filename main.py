import pygame as py
import sys
py.init()
width = 500
height = 600
screen = py.display.set_mode((width, height), py.DOUBLEBUF)
clock = py.time.Clock()

run = True
while run:
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
    
    py.display.flip()