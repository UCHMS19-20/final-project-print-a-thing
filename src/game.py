import sys
import pygame

#http://programarcadegames.com/python_examples/show_file.php?file=platform_jumper.py

pygame.init()

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