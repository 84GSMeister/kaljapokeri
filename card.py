import random, pygame

class PlayerCard(pygame.sprite.Sprite):
    selected = False
    type = 0
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("card_mushroom.png")
        self.changeCard(random.randint(0,6))
        self.rect = self.image.get_rect()
        self.rect.center = (Variables.playerCardPositionX, 440)
        Variables.playerCardPositionX += 60
 
    def draw(self, surface):
        if self.selected:
            rect = (self.rect.x, self.rect.y - 30)
            surface.blit(self.image, rect)
        else:
            surface.blit(self.image, self.rect)

    def changeCard(self, type):
        self.type = type
        match type:
            case 0: self.image = pygame.image.load("card_cloud.png")
            case 1: self.image = pygame.image.load("card_mushroom.png")
            case 2: self.image = pygame.image.load("card_flower.png")
            case 3: self.image = pygame.image.load("card_luigi.png")
            case 4: self.image = pygame.image.load("card_mario.png")
            case 5: self.image = pygame.image.load("card_star.png")

class EnemyCard(pygame.sprite.Sprite):
    selected = False
    type = 0
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("card_back.png")
        self.rect = self.image.get_rect()
        self.rect.center = (Variables.enemyCardPositionX, 140)
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
            case 0: self.image = pygame.image.load("card_cloud.png")
            case 1: self.image = pygame.image.load("card_mushroom.png")
            case 2: self.image = pygame.image.load("card_flower.png")
            case 3: self.image = pygame.image.load("card_luigi.png")
            case 4: self.image = pygame.image.load("card_mario.png")
            case 5: self.image = pygame.image.load("card_star.png")

    def show(self):
        match self.type:
            case 0: self.image = pygame.image.load("card_cloud.png")
            case 1: self.image = pygame.image.load("card_mushroom.png")
            case 2: self.image = pygame.image.load("card_flower.png")
            case 3: self.image = pygame.image.load("card_luigi.png")
            case 4: self.image = pygame.image.load("card_mario.png")
            case 5: self.image = pygame.image.load("card_star.png")

    def hide(self):
        self.image = pygame.image.load("card_back.png")


class Variables:
    playerCardPositionX = 80
    enemyCardPositionX = 80