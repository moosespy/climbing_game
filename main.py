import pygame as py
import sys
import random
py.init()
width = 500
height = 600

screen = py.display.set_mode((width, height))
clock = py.time.Clock()
level_height = 1200

blue = [0, 0, 255]
white = [255, 255, 255]
black = [0, 0, 0]
gray = [128, 128, 128]
sky_blue = [135, 206, 235]

gravity = 1 * 60

def draw_gradient(w, h, c_top, c_bottom):
    bg_surf = py.Surface((1, 2))
    bg_surf.set_at((0, 0), c_top)
    bg_surf.set_at((0, 1), c_bottom)
    grad_surf = py.transform.smoothscale(bg_surf, (w, h))
    return grad_surf.convert()

def draw_platform():
    global platform_surf
    platform_points = [(0, 0), (20, 0), (20, 10), (0, 10)]
    platform_surf = py.Surface((20, 10)).convert()
    py.draw.polygon(platform_surf, gray, platform_points)
draw_platform()
platforms = []
for i in range(100):
    platforms.append(platform_surf.get_rect(center = (250 - 2 * i, level_height - i * 100)))

class Player:
    def __init__(self, x, y, color, controls):
        self.x, self.y = float(x), float(y)
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
            self.vel_x = -1 * 60
        if keys[self.controls['right']]:
            self.vel_x = 1 * 60
        if keys[self.controls['jump']] and self.on_platform:
            self.vel_y = -14 * 60
            self.on_platform = False
    def update(self, platforms):
        self.key_input()
        self.vel_y += gravity
        if self.vel_y > 10 * 60:
            self.vel_y = 10 * 60
        
        self.x += self.vel_x * dt
        self.rect.x = round(self.x)
        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.rect.right >= platform.right:
                    self.rect.left = platform.right
                if self.rect.left <= platform.left:                        
                    self.rect.right = platform.left
                self.x = float(self.rect.x)
        
        self.y += self.vel_y * dt
        self.rect.y = round(self.y)
        hit_indices = self.rect.collidelistall(platforms)
        for index in hit_indices:
            platform = platforms[index]
            if self.vel_y > 0:
                self.rect.bottom = platform.top
                self.y = float(self.rect.y)
                self.vel_y = 0
                self.on_platform = True

    def draw(self, surface, scroll_y):
        py.draw.rect(surface, self.color, (self.rect.x, round(self.rect.y - scroll_y), self.rect.width, self.rect.height))

controls = {'left': py.K_LEFT, 'right': py.K_RIGHT, 'jump': py.K_UP}
player = Player(250, 1200, blue, controls)
scroll_y = 0

bg = draw_gradient(width, height, sky_blue, black)
gamestate = 'playing'

run = True
while run:
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
    
    dt = min(clock.tick(45) / 1000, 0.05)
    
    if gamestate == 'playing':
        player.update(platforms)
        
        if player.y > level_height + 500:
            gamestate == 'win'
        if player.y < 0:
            gamestate == 'lose'

        target_scroll_y = player.rect.y - (height // 2)
        scroll_y += (target_scroll_y - scroll_y) // 10
        if scroll_y < 0:
            scroll_y = 0
        if scroll_y > level_height:
            scroll_y = level_height
    
    if gamestate == 'win':
        run = False
    if gamestate == 'lose':
        run = False

    screen.blit(bg, (0, 0))
    for platform in platforms:
        screen.blit(platform_surf, (platform.x, platform.y - scroll_y))
    player.draw(screen, scroll_y)
    py.display.update()

py.quit()
sys.exit()