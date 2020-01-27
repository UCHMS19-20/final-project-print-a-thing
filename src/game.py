import sys
import pygame

pygame.font.init

Screen_width = 800
Screen_height = 800

White = (255, 255, 255)
Black = (0, 0, 0)
Grade = 5

Font = pygame.font.Font("timesnewroman.ttf", 12)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("src/mouse.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_y = 0
        self.change_x = 0

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        self.level = []
    
        Hit_list = pygame.sprite.spritecollide(self, self.level, False)
        for P in Hit_list:
            if self.change_x > 0:
                self.rect.right = P.rect.left
            if self.change_x < 0:
                self.rect.left = P.rect.right
        for P in Hit_list:
            if self.change_y > 0:
                self.rect.bottom = P.rect.top
            if self.change_y < 0:
                self.rect.top = P.rect.bottom
                self.change_y = 0

    def fall(self):
        if self.change.y == 0:
            self.change.y = .5
        else:
            self.change.y += .5

        if self.rect.y >= Screen_height - self.rect.height and self.change_y >= 0:
            Grade -= 1
            self.change.y = 0
            self.change.x =0
            self.rect.x = x
            self.rect.y = y

    def ymove(self):
        self.rect.y += 2
        Hit_list = pygame.sprite.spritecollide(self, self.level, False)
        self.rect.y -= 2

        if len(Hit_list) > 0:
            self.change.y = - 8

    def Rmove(self):
        self.change.x = 6

    def Lmove(self):
        self.change.x = -6

    def Stop(self):
        self.change.x = 0

class Platform(pygame.sprite.Sprite):
    def __init__(self, wide, tall, x, y):
        pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.image = pygame.Surface([wide, tall])
        self.image.fill(White)
        self.rect1 = self.image.get_rect()
        self.rect1.x = x
        self.rect1.y = y

class layout(object):
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group
        self.player = player
        self.background = pygame.image.load("src/background.jpg")

        level = [[210, 70, 500, 500],
            [210, 70, 200, 400],
            [210, 70, 600, 300],
            ]

        for platform in level:
            P = Platform(platform[0], platform[1], platform[2], platform[3])
            P.player = self.player
            self.platform_list.add(P)

    def update(self):
        self.platform_list.update

    def draw(self, Screen):
        self.background.draw(Screen)
        self.platform_list.draw(Screen)

class finalpaper(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("src/paper.jpeg")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def maingame():
    pygame.init()
    pygame.font.init()
    screen_size = [Screen_width, Screen_height]
    Screen = pygame.display.set_mode(screen_size)
    player1 = Player(340, 100)
    Paper = finalpaper(200, 100)
    Grademessage = "Sample"

    def grading():
        if Grade == 5:
	        Grademessage = "If turned in now you will get an A"
        elif Grade == 4:
	        Grademessage = "If turned in now you will get a B"
        elif Grade == 3:
            Grademessage = "If turned in now you will get a C"
        elif Grade == 2:
            Grademessage = "If turned in now you will get a D"
        elif Grade == 1:
            Grademessage = "If turned in now you will get an F"
        else:
            Grademessage = "You couldn’t turn it in and got a 0"

        Text = Font.render(Grademessage, True, Black, White)
        Textrect = Text.get_rect
        Textrect.center = (Screen_width/2, Screen_height/3)
        Screen.blit(Text, Textrect)

    Sprites_list = pygame.sprite.Group()
    player1.level = layout(player1)

    Sprites_list.add(player1)
    Sprites_list.add(Paper)

    Won = False

    while not Won:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_Left:
                    player1.Lmove()
                if event.key == pygame.K_Right:
                    player1.Rmove()
                if event.key == pygame.K_Up:
                    player1.ymove()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT and player1.change_x < 0:
                        player1.stop()
                    if event.key == pygame.K_RIGHT and player1.change_x > 0:
                        player1.stop()

        if player1.rect.colliderect(Paper.rect):
            Won = True

        if Grade < 0:
            Won = True
		
        if player1.rect.x > Screen_width:
            player1.rect.right = Screen_width
        if player1.rect.x < 0:
            player1.rect.left = 0

        Sprites_list.update()
        layout.update()

        layout.draw(Screen)
        Sprites_list.draw(Screen)
        grading()

        clock.tick(60)
        pygame.display.flip

    if Grade > 0:
        Screen.fill(White)
        Text = Font.render("You won! You handed the paper in on time!", True, black, white)
        Textrect = Text.get_rect
        Textrect.center = (Screen_width/2, Screen_height/3)

    else:
        Screen.fill(White)
        Text = Font.render("You lost. You couldn’t get the paper to print.", True, black, white)
        Textrect = Text.get_rect
        Textrect.center = (Screen_width/2, Screen_height/3)

maingame()
