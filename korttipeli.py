import sys, pygame, random
from pygame.locals import *
from card import PlayerCard, EnemyCard
from hand_types import HandTypes
from player import Player

pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()
 
# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Korttipeli")
pygame.display.set_icon(pygame.image.load("card_luigi.png"))

class Game:
    gameover = False
 
class DrawButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("draw_button.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 320)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class AgainButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("again_button.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 540)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class WinnerText(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("text_win.png")
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.center = (200, 240)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)

def dealCards(onlySelected):
    if onlySelected:
        if pCard1.selected:
            pCard1.changeCard(random.randint(0,5))
        if pCard2.selected:
            pCard2.changeCard(random.randint(0,5))
        if pCard3.selected:
            pCard3.changeCard(random.randint(0,5))
        if pCard4.selected:
            pCard4.changeCard(random.randint(0,5))
        if pCard5.selected:
            pCard5.changeCard(random.randint(0,5))
    else:
        pCard1.changeCard(random.randint(0,5))
        pCard2.changeCard(random.randint(0,5))
        pCard3.changeCard(random.randint(0,5))
        pCard4.changeCard(random.randint(0,5))
        pCard5.changeCard(random.randint(0,5))
    pCard1.selected = False
    pCard2.selected = False
    pCard3.selected = False
    pCard4.selected = False
    pCard5.selected = False

def showEnemyCards():
    eCard1.changeCard(random.randint(0,5))
    eCard2.changeCard(random.randint(0,5))
    eCard3.changeCard(random.randint(0,5))
    eCard4.changeCard(random.randint(0,5))
    eCard5.changeCard(random.randint(0,5))
    Game.gameover = True

def initGame():
    Game.gameover = False
    winnerText.image.set_alpha(0)
    eCard1.hide()
    eCard2.hide()
    eCard3.hide()
    eCard4.hide()
    eCard5.hide()
    dealCards(False)

def checkWinner():
    if HandTypes.countScore(pCard1, pCard2, pCard3, pCard4, pCard5) > HandTypes.countScore(eCard1, eCard2, eCard3, eCard4, eCard5):
        print("pelaaja voitti")
        winnerText.image = pygame.image.load("text_win.png")
        winnerText.image.set_alpha(255)
    elif HandTypes.countScore(pCard1, pCard2, pCard3, pCard4, pCard5) < HandTypes.countScore(eCard1, eCard2, eCard3, eCard4, eCard5):
        print("vihollinen voitti")
        winnerText.image = pygame.image.load("text_lose.png")
        winnerText.image.set_alpha(255)
    else:
        print("tasapeli")
        winnerText.image = pygame.image.load("text_draw.png")
        winnerText.image.set_alpha(255)

pCard1 = PlayerCard()
pCard2 = PlayerCard()
pCard3 = PlayerCard()
pCard4 = PlayerCard()
pCard5 = PlayerCard()

eCard1 = EnemyCard()
eCard2 = EnemyCard()
eCard3 = EnemyCard()
eCard4 = EnemyCard()
eCard5 = EnemyCard()

drawButton = DrawButton()
againButton = AgainButton()
winnerText = WinnerText()
 
while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and not Game.gameover:
            if event.type == MOUSEBUTTONDOWN:
                if pCard1.rect.collidepoint(pygame.mouse.get_pos()):
                    pCard1.selected = not pCard1.selected
                elif pCard2.rect.collidepoint(pygame.mouse.get_pos()):
                    pCard2.selected = not pCard2.selected
                elif pCard3.rect.collidepoint(pygame.mouse.get_pos()):
                    pCard3.selected = not pCard3.selected
                elif pCard4.rect.collidepoint(pygame.mouse.get_pos()):
                    pCard4.selected = not pCard4.selected
                elif pCard5.rect.collidepoint(pygame.mouse.get_pos()):
                    pCard5.selected = not pCard5.selected
                elif drawButton.rect.collidepoint(pygame.mouse.get_pos()):
                    dealCards(True)
                    showEnemyCards()
                    checkWinner()
                elif againButton.rect.collidepoint(pygame.mouse.get_pos()):
                    initGame()
        elif event.type == MOUSEBUTTONDOWN:
            if againButton.rect.collidepoint(pygame.mouse.get_pos()):
                initGame()
     
    DISPLAYSURF.fill(WHITE)
    pCard1.draw(DISPLAYSURF)
    pCard2.draw(DISPLAYSURF)
    pCard3.draw(DISPLAYSURF)
    pCard4.draw(DISPLAYSURF)
    pCard5.draw(DISPLAYSURF)
    eCard1.draw(DISPLAYSURF)
    eCard2.draw(DISPLAYSURF)
    eCard3.draw(DISPLAYSURF)
    eCard4.draw(DISPLAYSURF)
    eCard5.draw(DISPLAYSURF)
    drawButton.draw(DISPLAYSURF)
    againButton.draw(DISPLAYSURF)
    winnerText.draw(DISPLAYSURF)
         
    pygame.display.update()
    FramePerSec.tick(FPS)