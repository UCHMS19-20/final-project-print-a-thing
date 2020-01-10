import sys
import pygame

#http://programarcadegames.com/python_examples/show_file.php?file=platform_jumper.py

pygame.init()

Fail = False

display_height = 600
display_width = 800

black = (0, 0, 0)
white = (255, 255, 255)
bloo = (50, 50, 150)

screen = pygame.display.set_mode((display_width, display_height))

class Player(Pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("src/mouse.jpg")
        self.rect = self.image.get_rect()

        self.change_x = 0
        self.change_y = 0

        self.level = None
    
    def update(self):
        self.calc_grav()

        self.rect.x += self.change_x

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
             if self.change_x < 0:
                self.rect.left = block.rect.right
        
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
             if self.change_y < 0:
                self.rect.top = block.rect.bottom

            self.change_y = 0

    def calc_grav(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y = .35
        if self.rect.y >= display_height - self.rect.height and self.change_y >= 0:
            Fail = True

    def jump(self):
        self.change_y = -10
    def left(self):
        self.change_x = -6
    def right(self):
        self.change_x = 6
    def stop(self):
        self.change_x = 0

class Platform(pygame.sprite.Sprite):

    def __init__(self, width, height, color):
        super().__init__()
        self.image = pygame.Surface([width. height)])
        self.image.fill(color)
        self.rect = self.image.get_rect()

class Level(object):
    def __init__(self, player):

class enemy(pygame.sprite.Sprite):


xp =  (display_width * 0.45)
yp = (display_height * 0.35)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                yp 
            if event.key == pygame.K_LEFT:
                xp -= 8
            if event.key == pygame.K_RIGHT:
                xp += 8
    screen.fill(bloo)            
    
    charpl(xp, yp)

    pygame.display.flip()