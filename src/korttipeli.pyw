import sys, pygame, random, time, threading, collections, pygame.midi
from pygame.locals import *

from card import *
from spritet import *
from tekstit import *
from kädet import Kädet

pygame.init()
FPS = 60
kello = pygame.time.Clock()
 
# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
PIIRTOALUSTA = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
PIIRTOALUSTA.fill(WHITE)
pygame.display.set_caption("Kaljapokeri")
pygame.display.set_icon(pygame.image.load("kuvat/kaljat/rainbow_lager.png"))

yläkuvanLeveys = 400
yläkuvanKorkeus = 300

korttienMäärä = 8

pygame.midi.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512, devicename="Microsoft GS Wavetable Synth")
pygame.mixer.music.load("casino_loop.mid")
pygame.mixer.music.load("casino_intro.mid")
pygame.mixer.music.play(loops = 1)
loopLoaded = False

class Peli:
    gameover = False
    skene = "Valikko"
    pelinTila = "Idle"
    musaSäieKäynnissä = True

    juomisTeksti = ""
    voittaja = ""

    otsikkoTeksti = ""
    ohjeTeksti = ""
    ohjeTeksti2 = ""
    ohjeTeksti3 = ""

    pelaajan_voitot = 0
    vihollisen_voitot = 0
    pelaajan_huikat = 0
    vihollisen_huikat = 0

    rahan_määrä = 10
    panoksen_määrä = 1
    voittoraha = 0

def jaa_kortit(card1, card2, card3, card4, card5):
    card1.changeCard(random.randint(0, korttienMäärä - 1))
    card2.changeCard(random.randint(0, korttienMäärä - 1))
    card3.changeCard(random.randint(0, korttienMäärä - 1))
    card4.changeCard(random.randint(0, korttienMäärä - 1))
    card5.changeCard(random.randint(0, korttienMäärä - 1))

def heitä_kortit(card1, card2, card3, card4, card5):
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
    odota_ja_päivitä_korttien_sij(card1, card2, card3, card4, card5)

def vaihda_kortit(card1, card2, card3, card4, card5):
    if card1.selected:
        card1.changeCard(random.randint(0, korttienMäärä - 1))
    if card2.selected:
        card2.changeCard(random.randint(0, korttienMäärä - 1))
    if card3.selected:
        card3.changeCard(random.randint(0, korttienMäärä - 1))
    if card4.selected:
        card4.changeCard(random.randint(0, korttienMäärä - 1))
    if card5.selected:
        card5.changeCard(random.randint(0, korttienMäärä - 1))

def palauta_kortit(card1, card2, card3, card4, card5):
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
    odota_ja_päivitä_korttien_sij(card1, card2, card3, card4, card5)

def valitse_vihollisen_kortit():
    select1 = True
    select2 = True
    select3 = True
    select4 = True
    select5 = True
    enemyHand = (eCard1.type, eCard2.type, eCard3.type, eCard4.type, eCard5.type)
    enemyHandSorted = sorted(enemyHand, reverse = True)
    enemyHandSorted = sorted(enemyHandSorted, key = enemyHandSorted.count, reverse = True)
    counts = collections.Counter(enemyHand)
    max_count = counts.most_common(1)[0][1]
    out = [value for value, count in counts.most_common() if count == max_count]
    for i in out:
        if eCard1.type is i:
            select1 = False
        if eCard2.type is i:
            select2 = False
        if eCard3.type is i:
            select3 = False
        if eCard4.type is i:
            select4 = False
        if eCard5.type is i:
            select5 = False
    if select1:
        eCard1.select()
    if select2:
        eCard2.select()
    if select3:
        eCard3.select()
    if select4:
        eCard4.select()
    if select5:
        eCard5.select()
    if not select1 and not select2 and not select3 and not select4 and not select5:
        eCard1.select()
        eCard2.select()
        eCard3.select()
        eCard4.select()
        eCard5.select()

def odota_ja_päivitä_korttien_sij(card1, card2, card3, card4, card5):
    extra_loops = 0
    while True:
        if card1.movingFrames > 0:
            card1.move()
        else:
            if card1.moveType is "Return":
                korttiääni.play()
            card1.moveType = "Idle"
        if card2.movingFrames > 0:
            card2.move()
        else:
            if card2.moveType is "Return":
                korttiääni.play()
            card2.moveType = "Idle"
        if card3.movingFrames > 0:
            card3.move()
        else:
            if card3.moveType is "Return":
                korttiääni.play()
            card3.moveType = "Idle"
        if card4.movingFrames > 0:
            card4.move()
        else:
            if card4.moveType is "Return":
                korttiääni.play()
            card4.moveType = "Idle"
        if card5.movingFrames > 0:
            card5.move()
        else:
            if card5.moveType is "Return":
                korttiääni.play()
            card5.moveType = "Idle"

        uudelleenpiirrä_kaikki()
        if not (card1.movingFrames > 0 or card2.movingFrames > 0 or card3.movingFrames > 0 or card4.movingFrames > 0 or card5.movingFrames > 0):
            extra_loops += 1

        if extra_loops >= 3:
            break
        else:
            continue
        
    card1.moveType = "Idle"
    card2.moveType = "Idle"
    card3.moveType = "Idle"
    card4.moveType = "Idle"
    card5.moveType = "Idle"
    uudelleenpiirrä_kaikki()
    pygame.event.get()

def järjestä_kortit(card1, card2, card3, card4, card5):
    playerHand = (card1.type, card2.type, card3.type, card4.type, card5.type)
    playerHandSorted = sorted(playerHand, reverse = True)
    playerHandSorted = sorted(playerHandSorted, key = playerHandSorted.count, reverse = True)

    index1 = playerHandSorted.index(playerHand[0])
    playerHandSortedCut = playerHandSorted
    playerHandSortedCut[index1] = 2^31
    index2 = playerHandSorted.index(playerHand[1])
    playerHandSortedCut[index2] = 2^31
    index3 = playerHandSorted.index(playerHand[2])
    playerHandSortedCut[index3] = 2^31
    index4 = playerHandSorted.index(playerHand[3])
    playerHandSortedCut[index4] = 2^31
    index5 = playerHandSorted.index(playerHand[4])

    card1.moveInOrder(index1 - 0)
    card2.moveInOrder(index2 - 1)
    card3.moveInOrder(index3 - 2)
    card4.moveInOrder(index4 - 3)
    card5.moveInOrder(index5 - 4)

    odota_ja_päivitä_korttien_sij(card1, card2, card3, card4, card5)

def näytä_vihollisen_kortit():
    eCard1.flip1()
    eCard2.flip1()
    eCard3.flip1()
    eCard4.flip1()
    eCard5.flip1()
    odota_ja_päivitä_korttien_sij(eCard1, eCard2, eCard3, eCard4, eCard5)
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
    odota_ja_päivitä_korttien_sij(eCard1, eCard2, eCard3, eCard4, eCard5)
    eCard1.show()
    eCard2.show()
    eCard3.show()
    eCard4.show()
    eCard5.show()
    pelaajan_käsi_teksti.päivitä_teksti(Kädet.haeKäsiTyyppi(pCard1, pCard2, pCard3, pCard4, pCard5))
    vihollisen_käsi_teksti.päivitä_teksti(Kädet.haeKäsiTyyppi(eCard1, eCard2, eCard3, eCard4, eCard5))
    juomisMäärä = Kädet.laskeJuomisMäärä(eCard1, eCard2, eCard3, eCard4, eCard5)
    Peli.juomisTeksti = font24.render("Juo " + str(juomisMäärä) + " huikkaa!", True, BLACK)
    odota_ja_päivitä_korttien_sij(eCard1, eCard2, eCard3, eCard4, eCard5)

def aloita_peli():
    Peli.rahan_määrä = 20
    Peli.pelaajan_voitot = 0
    Peli.vihollisen_voitot = 0
    Peli.pelaajan_huikat = 0
    Peli.vihollisen_huikat = 0
    pelaajan_voitot_teksti.päivitä_teksti(str(Peli.pelaajan_voitot))
    vihollisen_voitot_teksti.päivitä_teksti(str(Peli.vihollisen_voitot))
    pelaajan_huikat_teksti.päivitä_teksti(str(Peli.pelaajan_huikat))
    vihollisen_huikat_teksti.päivitä_teksti(str(Peli.vihollisen_huikat))
    nollaa_korttien_valinta(pCard1, pCard2, pCard3, pCard4, pCard5)
    nollaa_korttien_valinta(eCard1, eCard2, eCard3, eCard4, eCard5)

def nollaa_peli():
    Peli.gameover = False
    if Peli.skene is "Rahapeli":
        if Peli.rahan_määrä > 0:
            Peli.panoksen_määrä = 1
            Peli.rahan_määrä -= 1
            kolikkoääni.play()
        else: 
            Peli.skene = "Gameover"

    againButton.image.set_alpha(0)
    winnerText.image.set_alpha(0)
    harmaa_tausta.image.set_alpha(0)
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
    jaa_kortit(pCard1, pCard2, pCard3, pCard4, pCard5)
    jaa_kortit(eCard1, eCard2, eCard3, eCard4, eCard5)
    drawButton.image.set_alpha(255)
    eCard1.hide()
    eCard2.hide()
    eCard3.hide()
    eCard4.hide()
    eCard5.hide()
    panoksen_määrä_teksti.päivitä_panoksen_määrä(Peli.panoksen_määrä)
    rahan_määrä_teksti.päivitä_rahan_määrä(Peli.rahan_määrä)

def tarkista_voittaja():
    Peli.gameover = True
    if Kädet.laskePisteet(pCard1, pCard2, pCard3, pCard4, pCard5) > Kädet.laskePisteet(eCard1, eCard2, eCard3, eCard4, eCard5):
        Peli.voittaja = "Pelaaja"
        Peli.pelaajan_voitot += 1
        pelaajan_voitot_teksti.päivitä_teksti(str(Peli.pelaajan_voitot))
        väläytä_voittokäden_osoitinta()
        winnerText.image = pygame.image.load("kuvat/teksti_voitto.png")
        winnerText.image.set_alpha(255)
        harmaa_tausta.image.set_alpha(255)
        Peli.voittoraha = Peli.panoksen_määrä * Kädet.laskeJuomisMäärä(pCard1, pCard2, pCard3, pCard4, pCard5)
        Peli.vihollisen_huikat += Kädet.laskeJuomisMäärä(pCard1, pCard2, pCard3, pCard4, pCard5)
        vihollisen_huikat_teksti.päivitä_teksti(str(Peli.vihollisen_huikat))
    elif Kädet.laskePisteet(pCard1, pCard2, pCard3, pCard4, pCard5) < Kädet.laskePisteet(eCard1, eCard2, eCard3, eCard4, eCard5):
        Peli.voittaja = "Vihollinen"
        Peli.vihollisen_voitot += 1
        vihollisen_voitot_teksti.päivitä_teksti(str(Peli.vihollisen_voitot))
        väläytä_voittokäden_osoitinta()
        winnerText.image = pygame.image.load("kuvat/teksti_häviö.png")
        winnerText.image.set_alpha(255)
        harmaa_tausta.image.set_alpha(255)
        Peli.voittoraha = 0
        Peli.pelaajan_huikat += Kädet.laskeJuomisMäärä(eCard1, eCard2, eCard3, eCard4, eCard5)
        pelaajan_huikat_teksti.päivitä_teksti(str(Peli.pelaajan_huikat))
    else:
        Peli.voittaja = ""
        winnerText.image = pygame.image.load("kuvat/teksti_tasapeli.png")
        winnerText.image.set_alpha(255)
        harmaa_tausta.image.set_alpha(255)
        Peli.voittoraha = 0
        Peli.rahan_määrä += Peli.panoksen_määrä
    if Peli.skene is "Rahapeli":
        anna_rahaa()
    againButton.image.set_alpha(255)

def nollaa_korttien_valinta(card1, card2, card3, card4, card5):
    if card1.selected:
        card1.selected = False
    if card2.selected:
        card2.selected = False
    if card3.selected:
        card3.selected = False
    if card4.selected:
        card4.selected = False
    if card5.selected:
        card5.selected = False

def lisää_panos():
    if Peli.panoksen_määrä < 5 and Peli.rahan_määrä > 0:
        Peli.panoksen_määrä += 1
        Peli.rahan_määrä -=1
        kolikkoääni.play()
    else:
        virheääni.play()
    panoksen_määrä_teksti.päivitä_panoksen_määrä(Peli.panoksen_määrä)
    rahan_määrä_teksti.päivitä_rahan_määrä(Peli.rahan_määrä)

def anna_rahaa():
    voittorahan_kuvakkeet = []
    uudelleenpiirrä_kaikki()
    for i in range(Peli.voittoraha):
        voittorahan_kuvakkeet.append(VoittoKolikko())
        sij_x = 128 + ((i % 10) * 16)
        sij_y = 192 + int(i / 10) * 16
        voittorahan_kuvakkeet[i].image.set_alpha(255)
        voittorahan_kuvakkeet[i].rect.center = (sij_x, sij_y)
        voittorahan_kuvakkeet[i].draw(PIIRTOALUSTA)
    pygame.display.update()
    pygame.event.get()
    time.sleep(0.5)
    for i in range(Peli.voittoraha):
        Peli.rahan_määrä += 1
        rahan_määrä_teksti.päivitä_rahan_määrä(Peli.rahan_määrä)
        kolikkoääni.play()
        uudelleenpiirrä_kaikki()
        voittorahan_kuvakkeet[i].image.set_alpha(0)
        for kuvake in voittorahan_kuvakkeet:
            kuvake.draw(PIIRTOALUSTA)
        pygame.display.update()
        pygame.event.get()
        time.sleep(0.1)

def väläytä_voittokäden_osoitinta():
    match Peli.voittaja:
        case "Pelaaja":
            x_keski = 130/2 + 10
            y_keski = 0
            match Kädet.haeKäsiTyyppi(pCard1, pCard2, pCard3, pCard4, pCard5):
                case "Vitoset": y_keski = 24/2 + 10
                case "Neloset": y_keski = 24/2 + 34
                case "Täyskäsi": y_keski = 24/2 + 58
                case "Kolmoset": y_keski = 24/2 + 82
                case "2 Paria": y_keski = 24/2 + 106
                case "1 Pari": y_keski = 24/2 + 130
            voittokäden_osoitin_pelaaja.rect.center = (x_keski, y_keski)
            for i in range(10):
                uudelleenpiirrä_kaikki()
                if i % 2 is 0:
                    voittokäden_osoitin_pelaaja.draw(PIIRTOALUSTA)
                    voittojen_osoitin_pelaaja.draw(PIIRTOALUSTA)
                pygame.display.update()
                time.sleep(0.2)
        case "Vihollinen":
            x_keski = 130/2 + 10
            y_keski = 0
            match Kädet.haeKäsiTyyppi(eCard1, eCard2, eCard3, eCard4, eCard5):
                case "Vitoset": y_keski = 24/2 + 10
                case "Neloset": y_keski = 24/2 + 34
                case "Täyskäsi": y_keski = 24/2 + 58
                case "Kolmoset": y_keski = 24/2 + 82
                case "2 Paria": y_keski = 24/2 + 106
                case "1 Pari": y_keski = 24/2 + 130
            voittokäden_osoitin_vihollinen.rect.center = (x_keski, y_keski)
            for i in range(10):
                uudelleenpiirrä_kaikki()
                if i % 2 is 0:
                    voittokäden_osoitin_vihollinen.draw(PIIRTOALUSTA)
                    voittojen_osoitin_vihollinen.draw(PIIRTOALUSTA)
                pygame.display.update()
                time.sleep(0.2)

def uudelleenpiirrä_kaikki():
    match Peli.skene:
        case "Juomapeli":
            PIIRTOALUSTA.fill(WHITE)
            eCard1.draw(PIIRTOALUSTA)
            eCard2.draw(PIIRTOALUSTA)
            eCard3.draw(PIIRTOALUSTA)
            eCard4.draw(PIIRTOALUSTA)
            eCard5.draw(PIIRTOALUSTA)
            pCard1.draw(PIIRTOALUSTA)
            pCard2.draw(PIIRTOALUSTA)
            pCard3.draw(PIIRTOALUSTA)
            pCard4.draw(PIIRTOALUSTA)
            pCard5.draw(PIIRTOALUSTA)
            yläkuva.draw(PIIRTOALUSTA)
            drawButton.draw(PIIRTOALUSTA)
            juomataulukko.draw(PIIRTOALUSTA)
            arvoTaulukko.draw(PIIRTOALUSTA)
            voittotaulukko_juomapeli.draw(PIIRTOALUSTA)
            pelaajan_voitot_teksti.draw(PIIRTOALUSTA)
            vihollisen_voitot_teksti.draw(PIIRTOALUSTA)
            pelaajan_huikat_teksti.draw(PIIRTOALUSTA)
            vihollisen_huikat_teksti.draw(PIIRTOALUSTA)
            if Peli.gameover:
                harmaa_tausta.draw(PIIRTOALUSTA)
                againButton.draw(PIIRTOALUSTA)
                winnerText.draw(PIIRTOALUSTA)
                pelaajan_käsi_teksti.draw(PIIRTOALUSTA)
                vihollisen_käsi_teksti.draw(PIIRTOALUSTA)
                if Peli.voittaja is "Vihollinen":
                    PIIRTOALUSTA.blit(Peli.juomisTeksti, juomisTekstiRect)

        case "Rahapeli":
            PIIRTOALUSTA.fill(WHITE)
            eCard1.draw(PIIRTOALUSTA)
            eCard2.draw(PIIRTOALUSTA)
            eCard3.draw(PIIRTOALUSTA)
            eCard4.draw(PIIRTOALUSTA)
            eCard5.draw(PIIRTOALUSTA)
            pCard1.draw(PIIRTOALUSTA)
            pCard2.draw(PIIRTOALUSTA)
            pCard3.draw(PIIRTOALUSTA)
            pCard4.draw(PIIRTOALUSTA)
            pCard5.draw(PIIRTOALUSTA)
            yläkuva.draw(PIIRTOALUSTA)
            drawButton.draw(PIIRTOALUSTA)
            rahan_kuvake.draw(PIIRTOALUSTA)
            rahan_määrä_teksti.draw(PIIRTOALUSTA)
            panoksen_määrä_teksti.draw(PIIRTOALUSTA)
            juomataulukko.draw(PIIRTOALUSTA)
            arvoTaulukko.draw(PIIRTOALUSTA)
            voittotaulukko_rahapeli.draw(PIIRTOALUSTA)
            pelaajan_voitot_teksti.draw(PIIRTOALUSTA)
            vihollisen_voitot_teksti.draw(PIIRTOALUSTA)
            if Peli.gameover:
                harmaa_tausta.draw(PIIRTOALUSTA)
                againButton.draw(PIIRTOALUSTA)
                winnerText.draw(PIIRTOALUSTA)
                pelaajan_käsi_teksti.draw(PIIRTOALUSTA)
                vihollisen_käsi_teksti.draw(PIIRTOALUSTA)
                if Peli.voittaja is "Pelaaja":
                    voittokäsi = Kädet.laskeJuomisMäärä(pCard1, pCard2, pCard3, pCard4, pCard5)
                    käsityyppi = Kädet.haeKäsiTyyppi(pCard1, pCard2, pCard3, pCard4, pCard5)
                    panos = Peli.panoksen_määrä
                    teksti = "+" + str(voittokäsi) + " (" + käsityyppi + ") * " + str(panos) + " (panos) = " + str(voittokäsi * panos)
                    Peli.juomisTeksti = pygame.font.Font("freesansbold.ttf", 16).render(teksti, True, BLACK)
                elif Peli.voittaja is "Vihollinen":
                    Peli.juomisTeksti = pygame.font.Font("freesansbold.ttf", 16).render("-" + str(Peli.panoksen_määrä) + " (panos)", True, BLACK)
                else:
                    Peli.juomisTeksti = pygame.font.Font("freesansbold.ttf", 16).render("Panokset palautetaan.", True, BLACK)
                PIIRTOALUSTA.blit(Peli.juomisTeksti, juomisTekstiRect)
            else:
                panosnappi.draw(PIIRTOALUSTA)
        case "Valikko":
            PIIRTOALUSTA.fill(WHITE)
            aloita_juomapeli.draw(PIIRTOALUSTA)
            aloita_rahapeli.draw(PIIRTOALUSTA)
            otsikko_teksti.draw(PIIRTOALUSTA)
            ohjeteksti1.draw(PIIRTOALUSTA)
            ohjeteksti2.draw(PIIRTOALUSTA)
            ohjeteksti3.draw(PIIRTOALUSTA)
        
        case "Gameover":
            PIIRTOALUSTA.fill(WHITE)
            gameover_otsikko.draw(PIIRTOALUSTA)
            gameover_teksti.draw(PIIRTOALUSTA)
            alkuvalikkoon_nappi.draw(PIIRTOALUSTA)

        case "Juomapeli_pause":
            PIIRTOALUSTA.fill(WHITE)
            pause_otsikko.draw(PIIRTOALUSTA)
            jatka_nappi.draw(PIIRTOALUSTA)
            alkuvalikkoon_nappi.draw(PIIRTOALUSTA)

        case "Rahapeli_pause":
            PIIRTOALUSTA.fill(WHITE)
            pause_otsikko.draw(PIIRTOALUSTA)
            jatka_nappi.draw(PIIRTOALUSTA)
            alkuvalikkoon_nappi.draw(PIIRTOALUSTA)
        
    pygame.display.update()
    kello.tick(FPS)

def toista_musa():
    while Peli.musaSäieKäynnissä:
        try:
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load("casino_loop.mid")
                pygame.mixer.music.play(loops = -1)
            else:
                time.sleep(0.2)
        except:
            print("virhe")


def prosessoi_tapahtumat():
    for event in pygame.event.get():
        if event.type == QUIT:
            Peli.musaSäieKäynnissä = False
            pygame.quit()
            sys.exit()

        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            match Peli.skene:
                case "Juomapeli": Peli.skene = "Juomapeli_pause"
                case "Rahapeli": Peli.skene = "Rahapeli_pause"
                case "Juomapeli_pause": Peli.skene = "Juomapeli"
                case "Rahapeli_pause": Peli.skene = "Rahapeli"
        
        elif event.type == MOUSEBUTTONDOWN:
            if not Peli.gameover:
                if Peli.skene is "Juomapeli" or Peli.skene is "Rahapeli":
                    if pCard1.rect.collidepoint(pygame.mouse.get_pos()):
                        if pCard1.moveType == "Idle":
                            if not pCard1.selected:
                                valintaääni.play()
                            else:
                                valinnanpoistoääni.play()
                            pCard1.select()
                            odota_ja_päivitä_korttien_sij(pCard1, pCard2, pCard3, pCard4, pCard5)
                    elif pCard2.rect.collidepoint(pygame.mouse.get_pos()):
                        if pCard2.moveType == "Idle":
                            if not pCard2.selected:
                                valintaääni.play()
                            else:
                                valinnanpoistoääni.play()
                            pCard2.select()
                            odota_ja_päivitä_korttien_sij(pCard1, pCard2, pCard3, pCard4, pCard5)
                    elif pCard3.rect.collidepoint(pygame.mouse.get_pos()):
                        if pCard3.moveType == "Idle":
                            if not pCard3.selected:
                                valintaääni.play()
                            else:
                                valinnanpoistoääni.play()
                            pCard3.select()
                            odota_ja_päivitä_korttien_sij(pCard1, pCard2, pCard3, pCard4, pCard5)
                    elif pCard4.rect.collidepoint(pygame.mouse.get_pos()):
                        if pCard4.moveType == "Idle":
                            if not pCard4.selected:
                                valintaääni.play()
                            else:
                                valinnanpoistoääni.play()
                            pCard4.select()
                            odota_ja_päivitä_korttien_sij(pCard1, pCard2, pCard3, pCard4, pCard5)
                    elif pCard5.rect.collidepoint(pygame.mouse.get_pos()):
                        if pCard5.moveType == "Idle":
                            if not pCard5.selected:
                                valintaääni.play()
                            else:
                                valinnanpoistoääni.play()
                            pCard5.select()
                            odota_ja_päivitä_korttien_sij(pCard1, pCard2, pCard3, pCard4, pCard5)
                    elif drawButton.rect.collidepoint(pygame.mouse.get_pos()):
                        if Peli.pelinTila == "Idle":
                            drawButton.image.set_alpha(127)
                            heitä_kortit(pCard1, pCard2, pCard3, pCard4, pCard5)
                            CardAnim.resetAnimOffset()
                            vaihda_kortit(pCard1, pCard2, pCard3, pCard4, pCard5)
                            palauta_kortit(pCard1, pCard2, pCard3, pCard4, pCard5)
                            CardAnim.resetAnimOffset()

                            valitse_vihollisen_kortit()
                            heitä_kortit(eCard1, eCard2, eCard3, eCard4, eCard5)
                            CardAnim.resetAnimOffset()
                            vaihda_kortit(eCard1, eCard2, eCard3, eCard4, eCard5)
                            palauta_kortit(eCard1, eCard2, eCard3, eCard4, eCard5)
                            CardAnim.resetAnimOffset()

                            järjestä_kortit(pCard1, pCard2, pCard3, pCard4, pCard5)
                            järjestä_kortit(eCard1, eCard2, eCard3, eCard4, eCard5)
                            näytä_vihollisen_kortit()
                            tarkista_voittaja()
                            nollaa_korttien_valinta(pCard1, pCard2, pCard3, pCard4, pCard5)
                            nollaa_korttien_valinta(eCard1, eCard2, eCard3, eCard4, eCard5)
                    elif panosnappi.rect.collidepoint(pygame.mouse.get_pos()):
                        if Peli.pelinTila is "Idle":
                            lisää_panos()

                elif Peli.skene is "Valikko":
                    if aloita_juomapeli.rect.collidepoint(pygame.mouse.get_pos()):
                        if Peli.pelinTila == "Idle":
                            Peli.skene = "Juomapeli"
                            nollaa_peli()
                    elif aloita_rahapeli.rect.collidepoint(pygame.mouse.get_pos()):
                        if Peli.pelinTila == "Idle":
                            Peli.skene = "Rahapeli"
                            nollaa_peli()

                elif Peli.skene is "Gameover":
                    if alkuvalikkoon_nappi.rect.collidepoint(pygame.mouse.get_pos()):
                        Peli.skene = "Valikko"
                        aloita_peli()

                elif Peli.skene is "Juomapeli_pause":
                    if jatka_nappi.rect.collidepoint(pygame.mouse.get_pos()):
                        Peli.skene = "Juomapeli"
                    elif alkuvalikkoon_nappi.rect.collidepoint(pygame.mouse.get_pos()):
                        Peli.skene = "Valikko"
                        aloita_peli()

                elif Peli.skene is "Rahapeli_pause":
                    if jatka_nappi.rect.collidepoint(pygame.mouse.get_pos()):
                        Peli.skene = "Rahapeli"
                    elif alkuvalikkoon_nappi.rect.collidepoint(pygame.mouse.get_pos()):
                        Peli.skene = "Valikko"
                        aloita_peli()
            else:
                if againButton.rect.collidepoint(pygame.mouse.get_pos()):
                    nollaa_peli()

    if not Peli.gameover:
        if pCard1.selected or pCard2.selected or pCard3.selected or pCard4.selected or pCard5.selected:
            drawButton.image = pygame.image.load("kuvat/vaihda_nappi.png")
        else:
            drawButton.image = pygame.image.load("kuvat/pidä_nappi.png")

    if pCard1.moveType == "Idle" and pCard2.moveType == "Idle" and pCard3.moveType == "Idle" and pCard4.moveType == "Idle" and pCard5.moveType == "Idle":
        Peli.pelinTila = "Idle"

# Alusta peli
yläkuva = YläKuva()
harmaa_tausta = TulosTausta()

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
juomataulukko = JuomaTaulukko()
arvoTaulukko = ArvoTaulukko()
againButton = AgainButton()
winnerText = WinnerText()
aloita_juomapeli = Aloita_Juomapeli()
aloita_rahapeli = Aloita_Rahapeli()
rahan_kuvake = Rahan_Kuvake()
rahan_määrä_teksti = Rahan_Määrä()
panosnappi = PanosNappi()
voittokäden_osoitin_pelaaja = VoittokädenOsoitinVihreä()
voittokäden_osoitin_vihollinen = VoittokädenOsoitinPunainen()
voittojen_osoitin_pelaaja = VoittojenOsoitinVihreä()
voittojen_osoitin_vihollinen = VoittojenOsoitinPunainen()

panoksen_määrä_teksti = Panoksen_Määrä()
pelaajan_käsi_teksti = Pelaajan_Käsi_Teksti()
vihollisen_käsi_teksti = Vihollisen_Käsi_Teksti()

voittotaulukko_juomapeli = VoittoTaulukko_Juomapeli()
voittotaulukko_rahapeli = VoittoTaulukko_Rahapeli()
pelaajan_voitot_teksti = Pelaajan_Voitot_Teksti()
vihollisen_voitot_teksti = Vihollisen_Voitot_Teksti()
pelaajan_huikat_teksti = Pelaajan_Huikat_Teksti()
vihollisen_huikat_teksti = Vihollisen_Huikat_Teksti()

otsikko_teksti = Otsikko_Teksti()
ohjeteksti1 = Ohjeteksti1()
ohjeteksti2 = Ohjeteksti2()
ohjeteksti3 = Ohjeteksti3()

gameover_otsikko = Gameover_Otsikko()
gameover_teksti = Gameover_Teksti()
alkuvalikkoon_nappi = Palaa_Valikkoon_Nappi()
pause_otsikko = Pause_Otsikko()
jatka_nappi = Jatka_Nappi()

kolikkoääni = pygame.mixer.Sound("sfx/koin.wav")
kolikkoääni.set_volume(0.4)
virheääni = pygame.mixer.Sound("sfx/virhe.wav")
virheääni.set_volume(0.5)
valintaääni = pygame.mixer.Sound("sfx/valitse.wav")
valintaääni.set_volume(0.5)
valinnanpoistoääni = pygame.mixer.Sound("sfx/poista_valinta.wav")
valinnanpoistoääni.set_volume(0.5)
korttiääni = pygame.mixer.Sound("sfx/kortti.wav")
korttiääni.set_volume(0)

font32 = pygame.font.Font("freesansbold.ttf", 32)
font24 = pygame.font.Font("freesansbold.ttf", 24)
Peli.juomisTeksti = font24.render("Juo", True, BLACK, WHITE)
juomisTekstiRect = Peli.juomisTeksti.get_rect()
juomisTekstiRect.center = (140, 180)

aloita_peli()
nollaa_peli()
musaSäie = threading.Thread(target = toista_musa)
musaSäie.start()
 
while True:
    prosessoi_tapahtumat()
    uudelleenpiirrä_kaikki()