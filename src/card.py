import random, pygame

class CardAnim:
    cardAnimOffset = 0

    def resetAnimOffset():
        CardAnim.cardAnimOffset = 0

    def useAnimOffset():
        CardAnim.cardAnimOffset += 10
        return CardAnim.cardAnimOffset

class PlayerCard(pygame.sprite.Sprite):
    selected = False
    type = 0
    moveType = ""
    movingFrames = 0
    movingDirection = "Up"
    initialCenter = (0,0)
    def __init__(self):
        super().__init__()
        self.changeCard(random.randint(0,5))
        self.rect = self.image.get_rect()
        self.rect.center = (Variables.playerCardPositionX, 560)
        self.initialCenter = (Variables.playerCardPositionX, 560)
        self.moveType = "Idle"
        Variables.playerCardPositionX += 60
 
    def draw(self, surface):
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
        self.movingFrames = 30 + CardAnim.useAnimOffset()

    def returnCard(self):
        self.moveType = "Return"
        self.movingDirection = "Down"
        self.movingFrames = 31 + CardAnim.useAnimOffset()

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
            case 0: self.image = pygame.image.load("kuvat/kaljat/rainbow_lager.png")
            case 1: self.image = pygame.image.load("kuvat/kaljat/olut_olut.png")
            case 2: self.image = pygame.image.load("kuvat/kaljat/karjala.png")
            case 3: self.image = pygame.image.load("kuvat/kaljat/lapin_kulta.png")
            case 4: self.image = pygame.image.load("kuvat/kaljat/ale_coq.png")
            case 5: self.image = pygame.image.load("kuvat/kaljat/karhu.png")
            case 6: self.image = pygame.image.load("kuvat/kaljat/olvi.png")
            case 7: self.image = pygame.image.load("kuvat/kaljat/sandels.png")

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
        self.image = pygame.image.load("kuvat/kortti_selkä.png")
        self.originalImage = self.image
        self.rect = self.image.get_rect()
        self.rect.center = (Variables.enemyCardPositionX, 340)
        self.initialCenter = (Variables.enemyCardPositionX, 340)
        self.moveType = "Idle"
        Variables.enemyCardPositionX += 60
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def changeCard(self, type):
        self.type = type

    def select(self):
        self.selected = not self.selected

    def throwAway(self):
        self.moveType = "Throw"
        self.movingDirection = "Up"
        self.movingFrames = 30 + CardAnim.useAnimOffset()

    def returnCard(self):
        self.moveType = "Return"
        self.movingDirection = "Down"
        self.movingFrames = 30 + CardAnim.useAnimOffset()

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
                            #self.image = pygame.image.load("kortti_selkä.png")
                            self.image = pygame.transform.scale(self.image, (int(self.image.get_size()[0] - 2), int(self.image.get_size()[1])))
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
            case 0: self.image = pygame.image.load("kuvat/kaljat/rainbow_lager.png")
            case 1: self.image = pygame.image.load("kuvat/kaljat/olut_olut.png")
            case 2: self.image = pygame.image.load("kuvat/kaljat/karjala.png")
            case 3: self.image = pygame.image.load("kuvat/kaljat/lapin_kulta.png")
            case 4: self.image = pygame.image.load("kuvat/kaljat/ale_coq.png")
            case 5: self.image = pygame.image.load("kuvat/kaljat/karhu.png")
            case 6: self.image = pygame.image.load("kuvat/kaljat/olvi.png")
            case 7: self.image = pygame.image.load("kuvat/kaljat/sandels.png")

    def flip2(self):
        self.image = pygame.transform.smoothscale(self.image, (int(self.image.get_size()[0] - 30), int(self.image.get_size()[1])))
        self.moveType = "Flip"
        self.movingDirection = "Wide"
        self.movingFrames = 15

    def resetImage(self):
        self.image = self.originalImage

    def hide(self):
        self.image = pygame.image.load("kuvat/kortti_selkä.png")

    def resetPos(self):
        self.rect.center = self.initialCenter


class Variables:
    playerCardPositionX = 80
    enemyCardPositionX = 80