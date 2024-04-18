import sys, pygame
from pygame.locals import *

yläkuvanLeveys = 400
yläkuvanKorkeus = 300

class YläKuva(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("kuvat/vihollinen.jpg")
        self.rect = self.image.get_rect()
        self.rect.center = (yläkuvanLeveys/2, yläkuvanKorkeus/2)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class TulosTausta(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("kuvat/harmaa_tausta.png")
        self.rect = self.image.get_rect()
        self.rect.center = (yläkuvanLeveys/2, yläkuvanKorkeus/2 + 20)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class JuomaTaulukko(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("kuvat/juomataulukko.png")
        self.rect = self.image.get_rect()
        self.rect.center = (130/2+10, 146/2+10)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class ArvoTaulukko(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("kuvat/arvotaulukko.png")
        self.rect = self.image.get_rect()
        self.rect.center = ((400 - 18/2)-10, 194/2+10)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class VoittoTaulukko_Juomapeli(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("kuvat/voittotaulukko_juomapeli.png")
        self.rect = self.image.get_rect()
        self.rect.center = (130/2+10, 10 + 146 + 10 + 124/2)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class VoittoTaulukko_Rahapeli(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("kuvat/voittotaulukko_rahapeli.png")
        self.rect = self.image.get_rect()
        self.rect.center = (130/2+10, 10 + + 146 + 10 + 80/2)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)
 
class DrawButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("kuvat/vaihda_nappi.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 450)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class AgainButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("kuvat/uudelleen_nappi.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 240)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class WinnerText(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("kuvat/teksti_voitto.png")
        self.image.set_alpha(0)
        self.rect = self.image.get_rect()
        self.rect.center = (200, 140)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Aloita_Juomapeli(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("kuvat/aloita_juomapeli_nappi.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 350)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Aloita_Rahapeli(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("kuvat/aloita_rahapeli_nappi.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 400)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Jatka_Nappi(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("kuvat/jatka_nappi.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 350)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Palaa_Valikkoon_Nappi(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("kuvat/alkuvalikkoon_nappi.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 400)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Rahan_Kuvake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("kuvat/raha.png")
        self.rect = self.image.get_rect()
        self.rect.center = (20, 320)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class PanosNappi(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("kuvat/panos.png")
        self.rect = self.image.get_rect()
        self.rect.center = (20, 360)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class VoittokädenOsoitinPunainen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("kuvat/voittokäden_osoitin_punainen.png")
        self.rect = self.image.get_rect()
        self.rect.center = (20, 360)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class VoittokädenOsoitinVihreä(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("kuvat/voittokäden_osoitin_vihreä.png")
        self.rect = self.image.get_rect()
        self.rect.center = (20, 360)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class VoittojenOsoitinPunainen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("kuvat/voittojen_osoitin_punainen.png")
        self.rect = self.image.get_rect()
        self.rect.center = (130/2+10 + 130/4, 222)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class VoittojenOsoitinVihreä(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("kuvat/voittojen_osoitin_vihreä.png")
        self.rect = self.image.get_rect()
        self.rect.center = (130/2+10 - 130/4, 222)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class VoittoKolikko(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("kuvat/raha.png")
        self.rect = self.image.get_rect()
        self.rect.center = (20, 360)

    def draw(self, surface):
        surface.blit(self.image, self.rect)