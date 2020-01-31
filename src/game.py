import pygame
import sys
import random
pygame.init()
pygame.font.init()
# Global constants
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

Grade = 5
font = pygame.font.Font("freesansbold.ttf", 22)
Win = False
Lose = False
 
class Player(pygame.sprite.Sprite):
    """ This class represents mouse cursor that the player controls """
    global Grade
    # -- Methods
    def __init__(self):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Load image of the mouse
        self.image = pygame.image.load("src/mouse.jpg")
 
        # Set a referance to the image rect.
        self.rect = self.image.get_rect()
 
        # Set speed vector of player
        self.change_x = 0
        self.change_y = 0
 
        # List of sprites we can bump against
        self.level = None
 
    def update(self):
        """ Move the player. """
        # Globls needed for this bit
        global font
        global Grade
        global Text
        global Textrect
        #need gravity for y movement
        self.calc_grav()
 
        # Move left/right
        self.rect.x += self.change_x
 
        # See if we hit any platforms
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
        if Grade == 5:
            Text = font.render("Go for it, get that A!", True, BLACK, WHITE)
            Textrect = Text.get_rect()
            Textrect.center = (400, 100)
        elif Grade == 4:
            Text = font.render("Keep going, a B's pretty good!", True, BLACK, WHITE)
            Textrect = Text.get_rect()
            Textrect.center = (400, 100)
        elif Grade == 3:
            Text = font.render("Hurry up! A C could be worse!", True, BLACK, WHITE)
            Textrect = Text.get_rect()
            Textrect.center = (400, 100)
        elif Grade == 2:
            Text = font.render("Oof, a D. At least you aren't failing", True, BLACK, WHITE)
            Textrect = Text.get_rect()
            Textrect.center = (400, 100)
        elif Grade == 1:
            Text = font.render("Hurry up! Hurry up! You may have an F but it's better than a 0!", True, BLACK, WHITE)
            Textrect = Text.get_rect()
            Textrect.center = (400, 100)
 
    def calc_grav(self):
        """ Calculate effect of gravity. """
        global Grade
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
 
        # See if we are on the ground.
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
            Grade -= 1
            print(Grade)
            self.rect.y = 300
            self.rect.x = 50

 
    def jump(self):
        """ Called when user hits 'jump' button. """
 
        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down
        # 1 when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
 
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10
 
    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
 
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
 
 
class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, width, height):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
 
        self.rect = self.image.get_rect()

class Paper(pygame.sprite.Sprite):
    """ Paper that is the objective """
 
    def __init__(self, x, y):
        """ Constructor. Needs location for different layouts """
        super().__init__()
 
        self.image = pygame.image.load("src/paper.jpeg")
 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
class Level(object):
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """
 
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. """
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player
         
        # Background image
        self.background = None
 
    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
 
    def draw(self, screen):
        """ Draw everything on this level. """
 
        # Draw the background
        screen.fill(BLUE)
 
        # Draw all the sprite lists that we have
        self.platform_list.draw(screen)
 
 
# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        # Array with width, height, x, and y of platform
        level = [[150, 50, 300, 270],
                 [150, 50, 60, 400],
                 [150, 50, 600, 130],
                 ]
 
        # Go through the array above and add platforms
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
 
 
def main():
    """ Main Program """
    pygame.init()
    global Win
    global Lose
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Platformer Jumper")
 
    # Create the player
    player = Player()
    papel = Paper(random.randint(200, 500), 90)
 
    # Create all the levels
    level_list = []
    level_list.append( Level_01(player) )
 
    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level
 
    player.rect.x = 50
    player.rect.y = 100
    active_sprite_list.add(player)
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()
            fin = pygame.sprite.collide_rect(papel, player)
            if fin > 0:
                Win = True
        # Update the player.
        print(Grade)
        active_sprite_list.update()

        # Update platforms in the level
        current_level.update()

        # If the player gets near the right side, stop them
        if player.rect.right > SCREEN_WIDTH:
            player.rect.right = SCREEN_WIDTH
 
        # If the player gets near the left side, stop them
        if player.rect.left < 0:
            player.rect.left = 0
 
        # draw all the objects on screen
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        screen.blit(papel.image, (papel.rect.x, papel.rect.y))
        screen.blit(Text, Textrect)

        if Grade == 0:
            Lose = True
        
 
        # Limit to 60 frames per second
        clock.tick(60)
 
        # update screen
        pygame.display.flip()

        if Win == True:
            done = True
        if Lose == True:
            done = True
    
    while Win == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit
        screen.fill(WHITE)
        pic = pygame.image.load("src/Success.jpg")
        screen.blit(pic, (0, 50))
        pygame.display.flip()
 
if __name__ == "__main__":
    main()