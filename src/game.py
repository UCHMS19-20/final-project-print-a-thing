import sys
import pygame

pygame.init()

display_height = 400
display_width = 400

black = (0, 0, 0)
white = (255, 255, 255)
greeen = (100, 200, 0)

screen = pygame.display.set_mode((display_width, display_height))

char = pygame.image.load("src/AAAH.jpg")

def charpl(x, y):
    screen.blit(char, (x,y))

xp =  (display_width * 0.45)
yp = (display_height * 0.6)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(greeen)

    charpl(xp, yp)

    pygame.display.flip()