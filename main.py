import pygame as py
import sys
py.init()
width = 500
height = 600
screen = py.display.set_mode((width, height), py.DOUBLEBUF)
clock = py.time.Clock()

player_surf = py.Surface((width, height/2))

blue = [0, 0, 255]
white = [255, 255, 255]
black = [0, 0, 0]
gray = [128, 128, 128]

gravity = 1

def draw_platform():
    global platform_surf
    platform_points = [(0, 0), (20, 0), (20, 10), (0, 10)]
    platform_surf = py.Surface((20, 10)).convert()
    py.draw.polygon(platform_surf, gray, platform_points)
draw_platform()
platforms = [
    platform_surf.get_rect(center = (225, 240))
]
class Player:
    def __init__(self, x, y, color, controls):
        self.rect = py.Rect(x, y, 18, 18)
        self.vel_x = 0
        self.vel_y = 0
        self.color = color
        self.on_platform = False
        self.controls = controls
    def key_input(self):
        keys = py.key.get_pressed()
        self.vel_x = 0
        if keys[self.controls['left']]:
            self.vel_x = -1
        if keys[self.controls['right']]:
            self.vel_x = 1
        if keys[self.controls['jump']] and self.on_platform():
            self.vel_y = -5
            self.on_platform = False
    def update(self, platforms):
        self.key_input()
        self.vel_y += gravity
        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.vel_x > 0:
                    self.rect.right = platform.left
                if self.vel_x < 0:                        
                    self.rect.left = platform.right
        self.rect.y += self.vel_y
        hit_indices = self.rect.collidelistall(platforms)
        for index in hit_indices:
            platform = platforms[index]
            if self.vel_y > 0:
                self.rect.bottom = platform.top
                self.vel_y = 0
                self.on_ground = True
    def draw(self, surface):
        py.draw.rect(surface, self.color, (round(self.rect.x), self.rect.y, self.rect.width, self.rect.height))

controls = {'left': py.K_LEFT, 'right': py.K_RIGHT, 'jump': py.K_UP}
player = Player(220, 0, blue, controls)

run = True
while run:
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
    
    py.display.flip()