import pygame as py
import sys
import random
import math
py.init()
width = 500
height = 600

screen = py.display.set_mode((width, height))
clock = py.time.Clock()
level_height = 1200
level = 1
score = 400
font = py.font.SysFont(None, 35)

blue = [0, 0, 255]
white = [255, 255, 255]
black = [0, 0, 0]
platf = [235, 224, 210]
gold = [232, 178, 84]
red = [255, 0, 0]
rust = [186, 78, 72]
misty = [218, 229, 232]
lower_sky = [154, 189, 207]
upper_sky = [91, 134, 166]
summit = [43, 66, 94]

gravity = 1 * 60

def draw_gradient(w, h, c_1, c_2, c_3, c_4):
    bg_surf = py.Surface((1, 3))
    bg_surf.set_at((0, 0), c_1)
    bg_surf.set_at((0, 1), c_2)
    bg_surf.set_at((0, 2), c_3)
    bg_surf.set_at((0, 3), c_4)
    grad_surf = py.transform.smoothscale(bg_surf, (w, h))
    return grad_surf.convert()

def draw_platform():
    global platform_surf
    platform_points = [(0, 0), (20, 0), (20, 10), (0, 10)]
    platform_surf = py.Surface((20, 10)).convert()
    py.draw.polygon(platform_surf, platf, platform_points)
draw_platform()
lvl1_platforms = []
lvl2_platforms = [
    platform_surf.get_rect(center = (250, 1150)),
    platform_surf.get_rect(center = (250, 1075)),
    platform_surf.get_rect(center = (250, 1000)),
    platform_surf.get_rect(center = (200, 950)),
    platform_surf.get_rect(center = (180, 950)),
    platform_surf.get_rect(center = (160, 950)),
    platform_surf.get_rect(center = (300, 950)),
    platform_surf.get_rect(center = (320, 950)),
    platform_surf.get_rect(center = (340, 950)),
    platform_surf.get_rect(center = (100, 900)),
    platform_surf.get_rect(center = (140, 900)),
    platform_surf.get_rect(center = (360, 900)),
    platform_surf.get_rect(center = (400, 900)),
    platform_surf.get_rect(center = (50, 850)),
    platform_surf.get_rect(center = (450, 850)),
    
    platform_surf.get_rect(center = (400, 800)),
    platform_surf.get_rect(center = (350, 750)),
    platform_surf.get_rect(center = (425, 700)),
    platform_surf.get_rect(center = (450, 650)),
    platform_surf.get_rect(center = (400, 600)),
    platform_surf.get_rect(center = (350, 550)),

]
for i in range(25):
    lvl1_platforms.append(platform_surf.get_rect(center = (250, level_height - i * 110)))
    lvl1_platforms.append(platform_surf.get_rect(center = (200, level_height - i * 110 + 50)))
    lvl1_platforms.append(platform_surf.get_rect(center = (300, level_height - i * 110 + 50)))
for i in range(25):
    lvl2_platforms.append(platform_surf.get_rect(center = (i * 20 + 10, 475)))
for i in range(6):
    lvl2_platforms.append(platform_surf.get_rect(center = (250, 400 - 75 * i)))
    lvl2_platforms.append(platform_surf.get_rect(center = (150, 400 - 75 * i)))
    lvl2_platforms.append(platform_surf.get_rect(center = (350, 400 - 75 * i)))
all_platforms = []
all_platforms.append(lvl1_platforms)
all_platforms.append(lvl2_platforms)

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
            self.vel_x = -2 * 60
        if keys[self.controls['right']]:
            self.vel_x = 2 * 60
        if keys[self.controls['jump']] and self.on_platform:
            self.vel_y = -11 * 60
            self.on_platform = False
    def update(self, platforms, snowballs):
        self.key_input()
        self.vel_y += gravity
        if self.vel_y > 10 * 60:
            self.vel_y = 10 * 60
        
        self.x += self.vel_x * dt
        self.rect.x = round(self.x)
        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.rect.right >= platform.right and self.vel_x < 0:
                    self.rect.left = platform.right
                if self.rect.left <= platform.left and self.vel_x > 0:                        
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
class Snowball:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.size = 10
        self.color = white
        self.vel_y = random.uniform(100, 200)
    def update(self, dt):
        self.y += self.vel_y * dt
    def draw(self, surface):
        py.draw.circle(surface, self.color, (round(self.x), round(self.y - scroll_y)), round(self.size))

class Particle:
    def __init__(self, center_x, center_y, color):
        self.x = float(center_x)
        self.y = float(center_y)
        self.size = random.randint(5, 10)
        self.color = color
        self.vel_x = random.uniform(-250, 250)
        self.vel_y = random.uniform(-250, 250)
        self.shrink_rate = random.uniform(6, 12)
    def update(self, dt):
        self.vel_y += 600 * dt
        self.x += self.vel_x * dt
        self.y += self.vel_y * dt
        self.size -= self.shrink_rate * dt
    def draw(self, surface):
        if self.size > 0:
            py.draw.rect(surface, self.color, (round(self.x), round(self.y), round(self.size), round(self.size)))

def explode(x, y, color):
    particles = []
    for _ in range(25):
        particles.append(Particle(x, y, color))
    return particles

def reset_game():
    x, y, state, scroll, count = 235, 1100, 'playing', 0, 0
    snowball = []
    return x, y, state, scroll, count, snowball
controls = {'left': py.K_LEFT, 'right': py.K_RIGHT, 'jump': py.K_UP}
player = Player(235, 1100, blue, controls)
player.x, player.y, gamestate, scroll_y, counter, snowballs = reset_game()

particles = []
bg = draw_gradient(width, height, summit, upper_sky, lower_sky, misty)
gamestate = 'playing'

run = True
while run:
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
    
    dt = min(clock.tick(45) / 1000, 0.05)
    
    if gamestate == 'playing':
        counter += 1
        if counter % 50 == 1:
            snowballs.append(Snowball(random.randint(50, width - 50), 0 - scroll_y))
        if counter % 6 == 0 and score != 0:
            score -= 1
        player.update(all_platforms[level - 1], snowballs)
        for s in snowballs:
            s.update(dt)
            closest_x = max(player.rect.left, min(s.x, player.rect.right))
            closest_y = max(player.rect.top, min(s.y, player.rect.bottom))
            distance_x = s.x - closest_x
            distance_y = s.y - closest_y
            distance = (distance_x ** 2) + (distance_y ** 2)
            if distance <= (s.size ** 2):
                gamestate = 'lose'
                particles = explode(player.rect.centerx, player.rect.centery - scroll_y, player.color)
        if player.y > level_height + 200:
            gamestate = 'lose'
            particles = explode(player.rect.centerx, player.rect.centery - scroll_y, player.color)
        if player.y < 0:
            gamestate = 'win'
            particles = explode(random.randint(0, width), random.randint(0, 100) - scroll_y, red)
        target_scroll_y = player.rect.y - (height // 2)
        scroll_y += (target_scroll_y - scroll_y) // 10
        if scroll_y < 0:
            scroll_y = 0
        if scroll_y > level_height:
            scroll_y = level_height
        if score == 0:
            gamestate = 'lose'
            particles = explode(player.rect.centerx, player.rect.centery - scroll_y, player.color)
    if gamestate == 'win':
        if level < len(all_platforms):
            game_over_text = font.render("Press space to move on!", True, black)
        else:
            game_over_text = font.render("You won the game!", True, black)
        for p in particles:
            p.update(dt)
        particles = [p for p in particles if p.size > 0]
        keys = py.key.get_pressed()
        if keys[py.K_SPACE] and level < len(all_platforms):
            player.x, player.y, gamestate, scroll_y, counter, snowballs = reset_game()
            level += 1                
    if gamestate == 'lose':
        score = 0
        game_over_text = font.render("You lost. Press 'r' to restart.", True, black)
        player.vel_y = 0
        for p in particles:
            p.update(dt)
        particles = [p for p in particles if p.size > 0]
        keys = py.key.get_pressed()
        if keys[py.K_r]:
            player.x, player.y, gamestate, scroll_y, counter, snowballs = reset_game()
            score = 400
            level = 1
    screen.blit(bg, (0, 0))
    for platform in all_platforms[level - 1]:
        screen.blit(platform_surf, (platform.x, platform.y - scroll_y))
    if gamestate == 'playing':
        player.draw(screen, scroll_y)
        for s in snowballs:
            s.draw(screen)
    if gamestate == 'lose' or gamestate == 'win':
        game_over_rect = game_over_text.get_rect(topleft=(10, 10))
        if gamestate == 'win':
            py.draw.rect(screen, gold, game_over_rect)
        else:
            py.draw.rect(screen, rust, game_over_rect)
        screen.blit(game_over_text, game_over_rect)
        for p in particles:
            p.draw(screen)
    score_text = font.render(f"Score: {score}", True, black)
    score_rect = score_text.get_rect(bottomright=(width-10, height-10))

    screen.blit(score_text, score_rect)
    py.display.update()

py.quit()
sys.exit()