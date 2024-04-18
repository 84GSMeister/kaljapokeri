import sys, pygame
from pygame.locals import *

yläkuvanLeveys = 400
yläkuvanKorkeus = 300

class Rahan_Määrä():
    text = ""
    def __init__(self):
        super().__init__()
        self.text = pygame.font.Font("freesansbold.ttf", 16).render("" + str(0), True, (0, 0, 0), (255, 255, 255))
        self.rect = self.text.get_rect()
        self.rect.center = (40, 320)

    def draw(self, surface):
        surface.blit(self.text, self.rect)

    def päivitä_rahan_määrä(self, määrä):
        self.text = pygame.font.Font("freesansbold.ttf", 16).render("" + str(määrä), True, (0, 0, 0), (255, 255, 255))

class Panoksen_Määrä():
    text = ""
    def __init__(self):
        super().__init__()
        self.text = pygame.font.Font("freesansbold.ttf", 16).render("" + str(0), True, (0, 0, 0), (255, 255, 255))
        self.rect = self.text.get_rect()
        self.rect.center = (20, 280)

    def draw(self, surface):
        surface.blit(self.text, self.rect)

    def päivitä_panoksen_määrä(self, määrä):
        self.text = pygame.font.Font("freesansbold.ttf", 16).render("Panos: " + str(määrä), True, (0, 0, 0), (255, 255, 255))

class Pelaajan_Käsi_Teksti():
    text = ""
    def __init__(self):
        super().__init__()
        self.text = pygame.font.Font("freesansbold.ttf", 32).render("", True, (0, 0, 0), (255, 255, 255))
        self.rect = self.text.get_rect()
        self.rect.center = (200, 500)

    def draw(self, surface):
        surface.blit(self.text, self.rect)

    def päivitä_teksti(self, päivitetty_teksti):
        self.text = pygame.font.Font("freesansbold.ttf", 32).render(päivitetty_teksti, True, (0, 0, 0), (255, 255, 255))
        self.rect = self.text.get_rect()
        self.rect.center = (200, 500)

class Vihollisen_Käsi_Teksti():
    text = ""
    def __init__(self):
        super().__init__()
        self.text = pygame.font.Font("freesansbold.ttf", 32).render("", True, (0, 0, 0), (255, 255, 255))
        self.rect = self.text.get_rect()
        self.rect.center = (200, 400)

    def draw(self, surface):
        surface.blit(self.text, self.rect)

    def päivitä_teksti(self, päivitetty_teksti):
        self.text = pygame.font.Font("freesansbold.ttf", 32).render(päivitetty_teksti, True, (0, 0, 0), (255, 255, 255))
        self.rect = self.text.get_rect()
        self.rect.center = (200, 400)

class Pelaajan_Voitot_Teksti():
    text = ""
    def __init__(self):
        super().__init__()
        self.text = pygame.font.Font("freesansbold.ttf", 24).render("0", True, (0, 0, 0))
        self.rect = self.text.get_rect()
        self.rect.center = (55, 222)

    def draw(self, surface):
        surface.blit(self.text, self.rect)

    def päivitä_teksti(self, päivitetty_teksti):
        self.text = pygame.font.Font("freesansbold.ttf", 24).render(päivitetty_teksti, True, (0, 0, 0))

class Vihollisen_Voitot_Teksti():
    text = ""
    def __init__(self):
        super().__init__()
        self.text = pygame.font.Font("freesansbold.ttf", 24).render("0", True, (0, 0, 0))
        self.rect = self.text.get_rect()
        self.rect.center = (120, 222)

    def draw(self, surface):
        surface.blit(self.text, self.rect)

    def päivitä_teksti(self, päivitetty_teksti):
        self.text = pygame.font.Font("freesansbold.ttf", 24).render(päivitetty_teksti, True, (0, 0, 0))

class Pelaajan_Huikat_Teksti():
    text = ""
    def __init__(self):
        super().__init__()
        self.text = pygame.font.Font("freesansbold.ttf", 24).render("0", True, (0, 0, 0))
        self.rect = self.text.get_rect()
        self.rect.center = (55, 268)

    def draw(self, surface):
        surface.blit(self.text, self.rect)

    def päivitä_teksti(self, päivitetty_teksti):
        self.text = pygame.font.Font("freesansbold.ttf", 24).render(päivitetty_teksti, True, (0, 0, 0))

class Vihollisen_Huikat_Teksti():
    text = ""
    def __init__(self):
        super().__init__()
        self.text = pygame.font.Font("freesansbold.ttf", 24).render("0", True, (0, 0, 0))
        self.rect = self.text.get_rect()
        self.rect.center = (120, 268)

    def draw(self, surface):
        surface.blit(self.text, self.rect)

    def päivitä_teksti(self, päivitetty_teksti):
        self.text = pygame.font.Font("freesansbold.ttf", 24).render(päivitetty_teksti, True, (0, 0, 0))


class Otsikko_Teksti():
    text = ""
    def __init__(self):
        super().__init__()
        self.text = pygame.font.Font("freesansbold.ttf", 50).render("Kaljapokeri", True, (0, 0, 0), (255, 255, 255))
        self.rect = self.text.get_rect()
        self.rect.center = (200, 150)

    def draw(self, surface):
        surface.blit(self.text, self.rect)

class Ohjeteksti1():
    text = ""
    def __init__(self):
        super().__init__()
        self.text = pygame.font.Font("freesansbold.ttf", 16).render("Tehtävänäsi on päihittää ilkeä", True, (0, 0, 0), (255, 255, 255))
        self.rect = self.text.get_rect()
        self.rect.center = (200, 230)

    def draw(self, surface):
        surface.blit(self.text, self.rect)

class Ohjeteksti2():
    text = ""
    def __init__(self):
        super().__init__()
        self.text = pygame.font.Font("freesansbold.ttf", 16).render("vinoviiksinen gangsteri kaljapokerissa.", True, (0, 0, 0), (255, 255, 255))
        self.rect = self.text.get_rect()
        self.rect.center = (200, 250)

    def draw(self, surface):
        surface.blit(self.text, self.rect)

class Ohjeteksti3():
    text = ""
    def __init__(self):
        super().__init__()
        self.text = pygame.font.Font("freesansbold.ttf", 20).render("Valitse pelimuoto", True, (0, 0, 0), (255, 255, 255))
        self.rect = self.text.get_rect()
        self.rect.center = (200, 300)

    def draw(self, surface):
        surface.blit(self.text, self.rect)

class Gameover_Otsikko(pygame.sprite.Sprite):
    text = ""
    def __init__(self):
        super().__init__()
        self.text = pygame.font.Font("freesansbold.ttf", 50).render("Hävisit pelin!", True, (0, 0, 0), (255, 255, 255))
        self.rect = self.text.get_rect()
        self.rect.center = (200, 150)

    def draw(self, surface):
        surface.blit(self.text, self.rect)

class Gameover_Teksti():
    text = ""
    def __init__(self):
        super().__init__()
        self.text = pygame.font.Font("freesansbold.ttf", 20).render("Käytit kaikki rahasi", True, (0, 0, 0), (255, 255, 255))
        self.rect = self.text.get_rect()
        self.rect.center = (200, 280)

    def draw(self, surface):
        surface.blit(self.text, self.rect)

class Pause_Otsikko(pygame.sprite.Sprite):
    text = ""
    def __init__(self):
        super().__init__()
        self.text = pygame.font.Font("freesansbold.ttf", 50).render("Pause", True, (0, 0, 0), (255, 255, 255))
        self.rect = self.text.get_rect()
        self.rect.center = (200, 150)

    def draw(self, surface):
        surface.blit(self.text, self.rect)