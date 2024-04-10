import sys, pygame, random
import numpy
from typing import List
from pygame.locals import *
from collections import Counter

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
pygame.display.set_caption("Kaljapokeri")
pygame.display.set_icon(pygame.image.load("kaljat/rainbow_lager.png"))
gameState = "Idle"

handTypes = ["5Kind", "4Kind", "FullHouse", "3Kind", "2Pairs", "1Pair", "Junk"]

class Game:
    gameover = False
    playerHandText = ""
    enemyHandText = ""
 
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
        self.image = pygame.image.load("teksti_voitto.png")
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.center = (200, 240)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)

#class PlayerHandText(pygame.sprite.Sprite):

def dealCards():
    pCard1.changeCard(random.randint(0,5))
    pCard2.changeCard(random.randint(0,5))
    pCard3.changeCard(random.randint(0,5))
    pCard4.changeCard(random.randint(0,5))
    pCard5.changeCard(random.randint(0,5))
    eCard1.changeCard(random.randint(0,5))
    eCard2.changeCard(random.randint(0,5))
    eCard3.changeCard(random.randint(0,5))
    eCard4.changeCard(random.randint(0,5))
    eCard5.changeCard(random.randint(0,5))

def throwCards(card1, card2, card3, card4, card5):
    if card1.selected:
        card1.throwAway()
    if card2.selected:
        card2.throwAway()
    if card3.selected:
        card3.throwAway()
    if card4.selected:
        card4.throwAway()
    if card5.selected:
        card5.throwAway()
    waitAndUpdateCardPos(card1, card2, card3, card4, card5)

def changeCards():
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

def returnCards(card1, card2, card3, card4, card5):
    if card1.selected:
        card1.returnCard()
    if card2.selected:
        card2.returnCard()
    if card3.selected:
        card3.returnCard()
    if card4.selected:
        card4.returnCard()
    if card5.selected:
        card5.returnCard()
    waitAndUpdateCardPos(card1, card2, card3, card4, card5)

def waitAndUpdateCardPos(card1, card2, card3, card4, card5):
    while card1.movingFrames > 0 or card2.movingFrames > 0 or card3.movingFrames > 0 or card4.movingFrames > 0 or card5.movingFrames > 0:
        if card1.movingFrames > 0:
            card1.move()
        else:
            card1.moveType = "Idle"
        if card2.movingFrames > 0:
            card2.move()
        else:
            card2.moveType = "Idle"
        if card3.movingFrames > 0:
            card3.move()
        else:
            card3.moveType = "Idle"
        if card4.movingFrames > 0:
            card4.move()
        else:
            card4.moveType = "Idle"
        if card5.movingFrames > 0:
            card5.move()
        else:
            card5.moveType = "Idle"
        redrawAll()
    card1.moveType = "Idle"
    card2.moveType = "Idle"
    card3.moveType = "Idle"
    card4.moveType = "Idle"
    card5.moveType = "Idle"

def sortCards(card1, card2, card3, card4, card5):
    print(card1.type, card2.type, card3.type, card4.type, card5.type)
    playerHand = (card1.type, card2.type, card3.type, card4.type, card5.type)
    playerHandSorted = sorted(playerHand, reverse = True)
    playerHandSorted = sorted(playerHandSorted, key = playerHandSorted.count, reverse = True)
    
    print("Og:", playerHand)
    print("Sorted:", playerHandSorted)

    index1 = playerHandSorted.index(playerHand[0])
    playerHandSortedCut = playerHandSorted
    playerHandSortedCut[index1] = 6
    #print(playerHandSortedCut)
    index2 = playerHandSorted.index(playerHand[1])
    playerHandSortedCut[index2] = 6
    #print(playerHandSortedCut)
    index3 = playerHandSorted.index(playerHand[2])
    playerHandSortedCut[index3] = 6
    #print(playerHandSortedCut)
    index4 = playerHandSorted.index(playerHand[3])
    playerHandSortedCut[index4] = 6
    #print(playerHandSortedCut)
    index5 = playerHandSorted.index(playerHand[4])

    print("Sorted indices1:", index1)
    print("Sorted indices2:", index2)
    print("Sorted indices3:", index3)
    print("Sorted indices4:", index4)
    print("Sorted indices5:", index5)

    card1.moveInOrder(index1 - 0)
    card2.moveInOrder(index2 - 1)
    card3.moveInOrder(index3 - 2)
    card4.moveInOrder(index4 - 3)
    card5.moveInOrder(index5 - 4)

    waitAndUpdateCardPos(card1, card2, card3, card4, card5)

    #card1.changeCard(playerHandSorted[0])
    #card2.changeCard(playerHandSorted[1])
    #card3.changeCard(playerHandSorted[2])
    #card4.changeCard(playerHandSorted[3])
    #card5.changeCard(playerHandSorted[4])

def showEnemyCards():
    eCard1.flip1()
    eCard2.flip1()
    eCard3.flip1()
    eCard4.flip1()
    eCard5.flip1()
    waitAndUpdateCardPos(eCard1, eCard2, eCard3, eCard4, eCard5)
    eCard1.show()
    eCard2.show()
    eCard3.show()
    eCard4.show()
    eCard5.show()
    eCard1.flip2()
    eCard2.flip2()
    eCard3.flip2()
    eCard4.flip2()
    eCard5.flip2()
    waitAndUpdateCardPos(eCard1, eCard2, eCard3, eCard4, eCard5)
    eCard1.show()
    eCard2.show()
    eCard3.show()
    eCard4.show()
    eCard5.show()
    playerHand = HandTypes.findHandType(pCard1, pCard2, pCard3, pCard4, pCard5)
    Game.playerHandText = font.render(playerHand, True, BLACK)
    enemyHand = HandTypes.findHandType(eCard1, eCard2, eCard3, eCard4, eCard5)
    Game.enemyHandText = font.render(enemyHand, True, BLACK)

def initGame():
    Game.gameover = False
    againButton.image.set_alpha(127)
    winnerText.image.set_alpha(0)
    pCard1.resetPos()
    pCard2.resetPos()
    pCard3.resetPos()
    pCard4.resetPos()
    pCard5.resetPos()
    eCard1.resetPos()
    eCard2.resetPos()
    eCard3.resetPos()
    eCard4.resetPos()
    eCard5.resetPos()
    dealCards()
    drawButton.image.set_alpha(255)
    eCard1.hide()
    eCard2.hide()
    eCard3.hide()
    eCard4.hide()
    eCard5.hide()

def checkWinner():
    if HandTypes.countScore(pCard1, pCard2, pCard3, pCard4, pCard5) > HandTypes.countScore(eCard1, eCard2, eCard3, eCard4, eCard5):
        #print("pelaaja voitti")
        winnerText.image = pygame.image.load("teksti_voitto.png")
        winnerText.image.set_alpha(255)
    elif HandTypes.countScore(pCard1, pCard2, pCard3, pCard4, pCard5) < HandTypes.countScore(eCard1, eCard2, eCard3, eCard4, eCard5):
        #print("vihollinen voitti")
        winnerText.image = pygame.image.load("teksti_häviö.png")
        winnerText.image.set_alpha(255)
    else:
        #print("tasapeli")
        winnerText.image = pygame.image.load("teksti_tasapeli.png")
        winnerText.image.set_alpha(255)
    Game.gameover = True
    againButton.image.set_alpha(255)

def resetCardPos(pCard1, pCard2, pCard3, pCard4, pCard5):
    if pCard1.selected:
        pCard1.select()
    if pCard2.selected:
        pCard2.select()
    if pCard3.selected:
        pCard3.select()
    if pCard4.selected:
        pCard4.select()
    if pCard5.selected:
        pCard5.select()

def redrawAll():
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
    if Game.gameover:
        DISPLAYSURF.blit(Game.playerHandText, playerHandtextRect)
        DISPLAYSURF.blit(Game.enemyHandText, enemyHandtextRect)
         
    pygame.display.update()
    FramePerSec.tick(FPS)

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

font = pygame.font.Font("freesansbold.ttf", 32)
Game.playerHandText = font.render("Player Hand", True, BLACK, BLUE)
playerHandtextRect = Game.playerHandText.get_rect()
playerHandtextRect.center = (200, 380)
Game.enemyHandText = font.render("Enemy Hand", True, BLACK, WHITE)
enemyHandtextRect = Game.playerHandText.get_rect()
enemyHandtextRect.center = (200, 190)


initGame()
 
while True:     
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and not Game.gameover:
            if event.type == MOUSEBUTTONDOWN:
                if pCard1.rect.collidepoint(pygame.mouse.get_pos()):
                    if pCard1.moveType == "Idle":
                        pCard1.select()
                        waitAndUpdateCardPos(pCard1, pCard2, pCard3, pCard4, pCard5)
                elif pCard2.rect.collidepoint(pygame.mouse.get_pos()):
                    if pCard2.moveType == "Idle":
                        pCard2.select()
                        waitAndUpdateCardPos(pCard1, pCard2, pCard3, pCard4, pCard5)
                elif pCard3.rect.collidepoint(pygame.mouse.get_pos()):
                    if pCard3.moveType == "Idle":
                        pCard3.select()
                        waitAndUpdateCardPos(pCard1, pCard2, pCard3, pCard4, pCard5)
                elif pCard4.rect.collidepoint(pygame.mouse.get_pos()):
                    if pCard4.moveType == "Idle":
                        pCard4.select()
                        waitAndUpdateCardPos(pCard1, pCard2, pCard3, pCard4, pCard5)
                elif pCard5.rect.collidepoint(pygame.mouse.get_pos()):
                    if pCard5.moveType == "Idle":
                        pCard5.select()
                        waitAndUpdateCardPos(pCard1, pCard2, pCard3, pCard4, pCard5)
                elif drawButton.rect.collidepoint(pygame.mouse.get_pos()):
                    if gameState == "Idle":
                        drawButton.image.set_alpha(127)
                        throwCards(pCard1, pCard2, pCard3, pCard4, pCard5)
                        changeCards()
                        returnCards(pCard1, pCard2, pCard3, pCard4, pCard5)

                        if pCard1.selected:
                            pCard1.select()
                        if pCard2.selected:
                            pCard2.select()
                        if pCard3.selected:
                            pCard3.select()
                        if pCard4.selected:
                            pCard4.select()
                        if pCard5.selected:
                            pCard5.select()
                        waitAndUpdateCardPos(pCard1, pCard2, pCard3, pCard4, pCard5)

                        #print("Player:", pCard1.type, pCard2.type, pCard3.type, pCard4.type, pCard5.type)
                        sortCards(pCard1, pCard2, pCard3, pCard4, pCard5)
                        #print("Enemy:", eCard1.type, eCard2.type, eCard3.type, eCard4.type, eCard5.type)
                        sortCards(eCard1, eCard2, eCard3, eCard4, eCard5)
                        showEnemyCards()
                        checkWinner()
                        resetCardPos(pCard1, pCard2, pCard3, pCard4, pCard5)
                        resetCardPos(eCard1, eCard2, eCard3, eCard4, eCard5)
                #elif againButton.rect.collidepoint(pygame.mouse.get_pos()):
                #    initGame()
        elif event.type == MOUSEBUTTONDOWN and Game.gameover:
            if againButton.rect.collidepoint(pygame.mouse.get_pos()):
                initGame()

    if not Game.gameover:
        if pCard1.selected or pCard2.selected or pCard3.selected or pCard4.selected or pCard5.selected:
            drawButton.image = pygame.image.load("draw_button.png")
        else:
            drawButton.image = pygame.image.load("hold_button.png")
     
    #if pCard1.movingFrames > 0:
    #    pCard1.move()
    #else:
    #    pCard1.moveType = "Idle"
    #if pCard2.movingFrames > 0:
    #    pCard2.move()
    #else:
    #    pCard2.moveType = "Idle"
    #if pCard3.movingFrames > 0:
    #    pCard3.move()
    #else:
    #    pCard3.moveType = "Idle"
    #if pCard4.movingFrames > 0:
    #    pCard4.move()
    #else:
    #    pCard4.moveType = "Idle"
    #if pCard5.movingFrames > 0:
    #    pCard5.move()
    #else:
    #    pCard5.moveType = "Idle"

    if pCard1.moveType == "Idle" and pCard2.moveType == "Idle" and pCard3.moveType == "Idle" and pCard4.moveType == "Idle" and pCard5.moveType == "Idle":
        gameState = "Idle"

    redrawAll()