import pygame
import sys
import random
pygame.init()
pygame.font.init()
# Importing and initializing^
 
# Colors, didn't end up needing red
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
 
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Some values and variables that are needed later in the code
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
        self.image = pygame.image.load("src/img/mouse.jpg")
 
        # Create rect for the image
        self.rect = self.image.get_rect()
 
        # Set speed vector of player to initial 0
        self.change_x = 0
        self.change_y = 0
 
        # List of sprites we can bump against (currently none)
        self.level = None
 
    def update(self):
        """ Move the player. """
        # Globals needed for this bit
        global font
        global Grade
        global Text
        global Textrect
        #need gravity for y movement(calc grav is defined after this function)
        self.calc_grav()
 
        # Move left/right
        self.rect.x += self.change_x
 
        # See if we hit any platforms
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # If moving right, set right side to left side of platform hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite
                self.rect.left = block.rect.right
 
        # Move up and down
        self.rect.y += self.change_y
 
        # Check and see if player hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
 
            # If player hits the top of a platform, set position back to top of that platform, same for bottom
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement when hit a platform
            self.change_y = 0

        #Create messages at the top of the screen to communicate what grade the player has(how many lives left)
        #This is here because this is where the grade function gets its value changed
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
        #Acceleration of gravity within the game
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
 
        # See if we are on the ground, if so reduce grade and put the player back at start
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height
            Grade -= 1
            self.rect.y = 300
            self.rect.x = 50

 
    def jump(self):
        """ Called when user hits 'jump' button, makes player jump up only if there is a platform """
 
        # move down a bit and see if there is a platform below us.
        # if there is then it's good to jump
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2
 
        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10
 
    # horizontal movement and stopping, less physics here
    def go_left(self):
        """ Change velocity leftward """
        self.change_x = -6
 
    def go_right(self):
        """ Change velocity rightward """
        self.change_x = 6
 
    def stop(self):
        """ stops the player's x movement """
        self.change_x = 0
 
 
class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """
 
    def __init__(self, width, height):
        """ Platform constructor. In order to construct thede there needs to be input of values """
        super().__init__()
        #Platforms are surfaces with rectangles assigned for collision
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
 
        self.rect = self.image.get_rect()

class Paper(pygame.sprite.Sprite):
    """ Paper that is the objective """
 
    def __init__(self, x, y):
        """ Constructor. Needs location for different layouts """
        super().__init__()
        #Paper is an image with a rect assigned for location and collision
        self.image = pygame.image.load("src/img/paper.jpeg")
 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
class Level(object):
    """ This is a generic super-class used to define a level.
        Create a child class for each level """
 
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. """
        #platform list for platform sprites & player for interactions
        self.platform_list = pygame.sprite.Group()
        self.player = player
         
        # Background image, doesn't exist here
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
    """ level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
        # Array with width, height, and location of platforms
        level = [[150, 50, 300, 270],
                 [150, 50, 60, 400],
                 [150, 50, 600, 130],
                 ]
 
        # Go through the array above and add platforms to platform list (draw later)
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platform_list.add(block)
 
 
def main():
    """ Main Program """
    #Wina and Lose variables for determining outcome
    global Win
    global Lose
    # Set the screen and screen caption
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Platform to print")
 
    # Create the player and paper, paper location varies slightly
    player = Player()
    papel = Paper(random.randint(400, 550), 90)
 
    # Create the level and add to the list
    level_list = []
    level_list.append( Level_01(player) )
 
    # Set the current level from list
    current_level_no = 0
    current_level = level_list[current_level_no]
 
    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    #Place player and add to list for functions
    player.rect.x = 50
    player.rect.y = 100
    active_sprite_list.add(player)
 
    # Loop until the window is closed, the player wins, or the player loses
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    # Main while loop
    while not done:
        for event in pygame.event.get():
            #Exit
            if event.type == pygame.QUIT:
                sys.exit

            #Movement linked to keys
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

            #If the player hits the paper, acheives win condition
            fin = pygame.sprite.collide_rect(papel, player)
            if fin > 0:
                Win = True

        # Update the player
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

        #If the player has fallen 5 times, fulfill lose condition
        if Grade == 0:
            Lose = True
        
 
        #set to 60 fps
        clock.tick(60)
 
        # update screen
        pygame.display.flip()

        # Exit loop if the player has won or lost
        if Win == True:
            done = True
        if Lose == True:
            done = True
    
    #Display the victory screen if player has won
    while Win == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Win = False
                sys.exit()
        screen.fill(WHITE)
        pic = pygame.image.load("src/img/Success.jpg")
        screen.blit(pic, (0, 0))
        pygame.display.flip()
 
#Play the game
if __name__ == "__main__":
    main()