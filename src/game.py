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

class Player(pygame.sprite.Sprite):

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
        self.image = pygame.Surface([width. height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

class Level(object):
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

        self.background = pygame.image.load("src/Yeehaw.jpg")

    def update(self):

        self.platform_list.update()
        self.enemy_list.update()
 
    def draw(self, screen):
        screen.fill(bloo)

        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

class Level_1(level):
    def __init__(self,player):

        Level.__init__(self, player)
        level = [[100, 20, 300, 400]]

        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                jump()
            if event.key == pygame.K_LEFT:
                left()
            if event.key == pygame.K_RIGHT:
                right()
    screen.fill(bloo)            
   

    pygame.display.flip()