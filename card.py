import random, pygame

class PlayerCard(pygame.sprite.Sprite):
    selected = False
    type = 0
    moveType = ""
    movingFrames = 0
    movingDirection = "Up"
    initialCenter = (0,0)
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("card_mushroom.png")
        self.changeCard(random.randint(0,5))
        self.rect = self.image.get_rect()
        self.rect.center = (Variables.playerCardPositionX, 440)
        self.initialCenter = (Variables.playerCardPositionX, 440)
        self.moveType = "Idle"
        Variables.playerCardPositionX += 60
 
    def draw(self, surface):
        #if self.selected:
        #    rect = (self.rect.x, self.rect.y - 30)
        #    surface.blit(self.image, rect)
        #else:
            surface.blit(self.image, self.rect)
    
    def select(self):
        self.moveType = "Select"
        if self.selected:
            self.movingDirection = "Down"
        else:
            self.movingDirection = "Up"
        self.selected = not self.selected
        self.movingFrames = 10

    def throwAway(self):
        self.moveType = "Throw"
        self.movingDirection = "Up"
        self.movingFrames = 30

    def returnCard(self):
        self.moveType = "Return"
        self.movingDirection = "Down"
        self.movingFrames = 30

    def moveInOrder(self, moveIndices):
        self.moveType = "Order"
        if moveIndices < 0:
            self.movingDirection = "Left"
            self.movingFrames = 15 * -moveIndices
        elif moveIndices > 0:
            self.movingDirection = "Right"
            self.movingFrames = 15 * moveIndices

    def move(self):
        match self.moveType:
            case "Select":
                try:
                    match self.movingDirection:
                        case "Up":
                            self.rect.y -= 2
                        case "Down":
                            self.rect.y += 2
                    self.movingFrames -= 1
                except:
                    print("can't move rect")
                    print("moving:", self.movingFrames)
                    self.movingFrames -= 1
            case "Throw":
                try:
                    match self.movingDirection:
                        case "Up":
                            self.rect.y -= 20
                    self.movingFrames -= 1
                except:
                    print("can't move rect")
                    print("moving:", self.movingFrames)
                    self.movingFrames -= 1
            case "Return":
                try:
                    match self.movingDirection:
                        case "Down":
                            self.rect.y += 20
                    self.movingFrames -= 1
                except:
                    print("can't move rect")
                    print("moving:", self.movingFrames)
                    self.movingFrames -= 1
            case "Order":
                try:
                    match self.movingDirection:
                        case "Left":
                            self.rect.x -= 4
                        case "Right":
                            self.rect.x += 4
                    self.movingFrames -= 1
                except:
                    print("can't move rect")
                    print("moving:", self.movingFrames)
                    self.movingFrames -= 1

    def resetPos(self):
        self.rect.center = self.initialCenter

    def changeCard(self, type):
        self.type = type
        match type:
            #case 0: self.image = pygame.image.load("card_cloud.png")
            #case 1: self.image = pygame.image.load("card_mushroom.png")
            #case 2: self.image = pygame.image.load("card_flower.png")
            #case 3: self.image = pygame.image.load("card_luigi.png")
            #case 4: self.image = pygame.image.load("card_mario.png")
            #case 5: self.image = pygame.image.load("card_star.png")
            case 0: self.image = pygame.image.load("kaljat/rainbow_lager.png")
            case 1: self.image = pygame.image.load("kaljat/olut_olut.png")
            case 2: self.image = pygame.image.load("kaljat/karjala.png")
            case 3: self.image = pygame.image.load("kaljat/lapin_kulta.png")
            case 4: self.image = pygame.image.load("kaljat/ale_coq.png")
            case 5: self.image = pygame.image.load("kaljat/sandels.png")

class EnemyCard(pygame.sprite.Sprite):
    selected = False
    type = 0
    moveType = ""
    movingFrames = 0
    movingDirection = "Up"
    initialCenter = (0,0)
    originalImage = ""
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("card_back.png")
        self.originalImage = self.image
        self.rect = self.image.get_rect()
        self.rect.center = (Variables.enemyCardPositionX, 140)
        self.initialCenter = (Variables.enemyCardPositionX, 140)
        self.moveType = "Idle"
        Variables.enemyCardPositionX += 60
 
    def draw(self, surface):
        if self.selected:
            rect = (self.rect.x, self.rect.y - 30)
            surface.blit(self.image, rect)
        else:
            surface.blit(self.image, self.rect)

    def changeCard(self, type):
        self.type = type
        match type:
            #case 0: self.image = pygame.image.load("card_cloud.png")
            #case 1: self.image = pygame.image.load("card_mushroom.png")
            #case 2: self.image = pygame.image.load("card_flower.png")
            #case 3: self.image = pygame.image.load("card_luigi.png")
            #case 4: self.image = pygame.image.load("card_mario.png")
            #case 5: self.image = pygame.image.load("card_star.png")
            case 0: self.image = pygame.image.load("kaljat/rainbow_lager.png")
            case 1: self.image = pygame.image.load("kaljat/olut_olut.png")
            case 2: self.image = pygame.image.load("kaljat/karjala.png")
            case 3: self.image = pygame.image.load("kaljat/lapin_kulta.png")
            case 4: self.image = pygame.image.load("kaljat/ale_coq.png")
            case 5: self.image = pygame.image.load("kaljat/sandels.png")

    def moveInOrder(self, moveIndices):
        print(self, moveIndices)
        self.moveType = "Order"
        if moveIndices < 0:
            self.movingDirection = "Left"
            self.movingFrames = 15 * -moveIndices
        elif moveIndices > 0:
            self.movingDirection = "Right"
            self.movingFrames = 15 * moveIndices

    def move(self):
        match self.moveType:
            case "Select":
                try:
                    match self.movingDirection:
                        case "Up":
                            self.rect.y -= 2
                        case "Down":
                            self.rect.y += 2
                    self.movingFrames -= 1
                except:
                    print("can't move rect")
                    print("moving:", self.movingFrames)
                    self.movingFrames -= 1
            case "Throw":
                try:
                    match self.movingDirection:
                        case "Up":
                            self.rect.y -= 20
                    self.movingFrames -= 1
                except:
                    print("can't move rect")
                    print("moving:", self.movingFrames)
                    self.movingFrames -= 1
            case "Return":
                try:
                    match self.movingDirection:
                        case "Down":
                            self.rect.y += 20
                    self.movingFrames -= 1
                except:
                    print("can't move rect")
                    print("moving:", self.movingFrames)
                    self.movingFrames -= 1
            case "Order":
                try:
                    match self.movingDirection:
                        case "Left":
                            self.rect.x -= 4
                        case "Right":
                            self.rect.x += 4
                    self.movingFrames -= 1
                except:
                    print("can't move rect")
                    print("moving:", self.movingFrames)
                    self.movingFrames -= 1
            case "Flip":
                try:
                    match self.movingDirection:
                        case "Narrow":
                            self.image = pygame.transform.smoothscale(self.image, (int(self.image.get_size()[0] - 2), int(self.image.get_size()[1])))
                            self.rect.x += 1
                        case "Wide":
                            self.image = pygame.transform.smoothscale(self.image, (int(self.image.get_size()[0] + 2), int(self.image.get_size()[1])))
                            self.rect.x -= 1
                    self.movingFrames -= 1
                except:
                    print("can't move rect")
                    print("moving:", self.movingFrames)
                    self.movingFrames -= 1

    def flip1(self):
        self.moveType = "Flip"
        self.movingDirection = "Narrow"
        self.movingFrames = 15

    def show(self):
        match self.type:
            #case 0: self.image = pygame.image.load("card_cloud.png")
            #case 1: self.image = pygame.image.load("card_mushroom.png")
            #case 2: self.image = pygame.image.load("card_flower.png")
            #case 3: self.image = pygame.image.load("card_luigi.png")
            #case 4: self.image = pygame.image.load("card_mario.png")
            #case 5: self.image = pygame.image.load("card_star.png")
            case 0: self.image = pygame.image.load("kaljat/rainbow_lager.png")
            case 1: self.image = pygame.image.load("kaljat/olut_olut.png")
            case 2: self.image = pygame.image.load("kaljat/karjala.png")
            case 3: self.image = pygame.image.load("kaljat/lapin_kulta.png")
            case 4: self.image = pygame.image.load("kaljat/ale_coq.png")
            case 5: self.image = pygame.image.load("kaljat/sandels.png")

    def flip2(self):
        self.image = pygame.transform.smoothscale(self.image, (int(self.image.get_size()[0] - 30), int(self.image.get_size()[1])))
        self.moveType = "Flip"
        self.movingDirection = "Wide"
        self.movingFrames = 15

    def resetImage(self):
        self.image = self.originalImage

    def hide(self):
        self.image = pygame.image.load("card_back.png")

    def resetPos(self):
        self.rect.center = self.initialCenter


class Variables:
    playerCardPositionX = 80
    enemyCardPositionX = 80