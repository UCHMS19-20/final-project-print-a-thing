Import sys
Import pygame

Win = False
Screen_width = 800
Screen_height = 800

White = (255, 255, 255)
Black = (0, 0, 0)
Grade = 5

Class Player (pygame.sprite.Sprite):
	def __init__(self, x, y):
        super().__init__()
		self.image = (character image(mouse))
		self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.platforms = false

        self.change_y = 0
        self.change_x = 0

    def changespeed(self, y):
        self.changey += y

    def update(self):
        self.rect.x += self.change_x
        self.rect.y += self.change_y
        self.level = None
    
        Hit_list = pygame.sprite.spritecollide(self, self.level.platforms, False)
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

        if self.rect.y >= screen_height - self.rect.height and self.change_y >= 0:
            Grade -= 1
            self.change.y = 0
            self.change.x =0
            self.rect.x = x
 			self.rect.y = y

    def ymove(self):
        self.rect.y += 2
        Hit_list = pygame.sprite.spritecollide(self, self.platforms, False)
 		self.rect.y -= 2

        if Len Hit_list > 0:
 			self.change.y = - 8

    def Rmove(self):
        self.change.x = 6

    def Lmove(self):
        self.change.x = -6

    def Stop(self):
        self.change.x = 0

Class Platform(pygame.sprite.Sprite):
    def __init__(self, wide, tall):
        super().__init__()
        self.image = pygame.Surface([wide, tall])
        self.image.fill(white)
        self.rect = self.image.get_rect

Class layout(object):
    def __init__(self, player):
		self.platform_list = pygame.sprite.Group
		self.player = player
		self.background = (Bkg image)

    level = [[210, 70, 500, 500],
        [210, 70, 200, 400],
        [210, 70, 600, 300],
        ]

    for platform in level:
  			P = Platform(platform[0], platform[1])
			P.rect.x = platform[2]
			P.rect.y = platform[3]
			P.player = self.player
			self.platform_list.add(p)

	def update(self):
		self.platform_list.update

	def draw(self, screen):
		self.background.draw(screen)
		self.platform_list.draw(screen)

Class finalpaper(pygame.sprite.Sprite):
	def __init__(self, x, y):
        super().__init__()
		self.image = (paper image)
		self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def maingame():
	pygame.init()
	pygame.font.init()
	screen_size = [Screen_width, Screen_height]
	Screen = pygame.display.set_mode(screen_size)
	Player = Player()
	Paper = finalpaper()
	
	Grademessage = "Sample"

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

	Font = pygame.font.Font("timesnewroman.ttf", 12)
	Text = Font.render(Grademessage, True, Black, White)
	Textrect = text.get_rect
	Textrect.center = (Screen_width/2, Screen_height/3)

    Sprites_list = pygame.sprite.Group()
    Player.level = Layout()

    Player.rect.x = 340
    Player.rect.y = 100
    Paper.rect.x = 240
    Paper.rect.y = 100

    Sprites_list.add(Player)
    Sprites_list.add(Paper)

    Won = False

    while not Won:
	    for event in pygame.event.get():
		    if event.type == pygame.QUIT:
			    sys.exit

		    if event.type == pygame.KEY_DOWN:
			    if event.key == pygame.K_Left
				    Player.Lmove()
                if event.key == pygame.K_Right
				    Player.Rmove()
                if event.key == pygame.K_Up
				    Player.ymove()

           		if event.type == pygame.KEYUP:
                	if event.key == pygame.K_LEFT and player.change_x < 0:
                    		Player.stop()
                	if event.key == pygame.K_RIGHT and player.change_x > 0:
                    		Player.stop()

	    if Player.rect.colliderect(Paper.rect):
		    Won = True

	    if Grade == 0:
		    Won = True
		
	    Sprites_list.update()
	    Layout.update()
	    Screen.blit(Text, Textrect)

	    if player.rect.x > Screen_width:
		    Player.rect.right = Screen_width
	    if player.rect.x < 0:
		    Player.rect.left = 0

	    Layout.draw(Screen)
	    Sprites_list.draw(Screen)
	
        clock.tick(60)
	    pygame.display.flip

    if Grade > 5
	    Screen.fill(white)
	    Text = Font.render("You won! You handed the paper in on time!", True, black, white)
		Textrect = text.get_rect
		Textrect.center = (screen_width/2, screen_height/3)

	else:
		Screen.fill(white)
	    Text = Font.render("You lost. You couldn’t get the paper to print. You shouldn’t have waited until the last day huh", True, black, white)
		Textrect = text.get_rect
		Textrect.center = (screen_width/2, screen_height/3)

maingame()


