class Kädet:

    def laskeSantut(card1, card2, card3, card4, card5):
        santut = 0
        if card1.type == 7:
            santut += 1
        if card2.type == 7:
            santut += 1
        if card3.type == 7:
            santut += 1
        if card4.type == 7:
            santut += 1
        if card5.type == 7:
            santut += 1
        return santut
    
    def laskeOlvit(card1, card2, card3, card4, card5):
        olvit = 0
        if card1.type == 6:
            olvit += 1
        if card2.type == 6:
            olvit += 1
        if card3.type == 6:
            olvit += 1
        if card4.type == 6:
            olvit += 1
        if card5.type == 6:
            olvit += 1
        return olvit
    
    def laskeKarhut(card1, card2, card3, card4, card5):
        karhut = 0
        if card1.type == 5:
            karhut += 1
        if card2.type == 5:
            karhut += 1
        if card3.type == 5:
            karhut += 1
        if card4.type == 5:
            karhut += 1
        if card5.type == 5:
            karhut += 1
        return karhut
    
    def laskeAlecoqit(card1, card2, card3, card4, card5):
        alecoqit = 0
        if card1.type == 4:
            alecoqit += 1
        if card2.type == 4:
            alecoqit += 1
        if card3.type == 4:
            alecoqit += 1
        if card4.type == 4:
            alecoqit += 1
        if card5.type == 4:
            alecoqit += 1
        return alecoqit
    
    def laskeLapparit(card1, card2, card3, card4, card5):
        lapparit = 0
        if card1.type == 3:
            lapparit += 1
        if card2.type == 3:
            lapparit += 1
        if card3.type == 3:
            lapparit += 1
        if card4.type == 3:
            lapparit += 1
        if card5.type == 3:
            lapparit += 1
        return lapparit
    
    def laskeKarjalat(card1, card2, card3, card4, card5):
        karjalat = 0
        if card1.type == 2:
            karjalat += 1
        if card2.type == 2:
            karjalat += 1
        if card3.type == 2:
            karjalat += 1
        if card4.type == 2:
            karjalat += 1
        if card5.type == 2:
            karjalat += 1
        return karjalat
    
    def laskeOlutOluet(card1, card2, card3, card4, card5):
        olutOluet = 0
        if card1.type == 1:
            olutOluet += 1
        if card2.type == 1:
            olutOluet += 1
        if card3.type == 1:
            olutOluet += 1
        if card4.type == 1:
            olutOluet += 1
        if card5.type == 1:
            olutOluet += 1
        return olutOluet
    
    def laskeKuparit(card1, card2, card3, card4, card5):
        kuparit = 0
        if card1.type == 0:
            kuparit += 1
        if card2.type == 0:
            kuparit += 1
        if card3.type == 0:
            kuparit += 1
        if card4.type == 0:
            kuparit += 1
        if card5.type == 0:
            kuparit += 1
        return kuparit
    
    def laskePisteet(card1, card2, card3, card4, card5):
        pisteet = 0
        if Kädet.laskeSantut(card1, card2, card3, card4, card5) == 5: pisteet = 116
        elif Kädet.laskeOlvit(card1, card2, card3, card4, card5) == 5: pisteet = 115
        elif Kädet.laskeKarhut(card1, card2, card3, card4, card5) == 5: pisteet = 114
        elif Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 5: pisteet = 113
        elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 5: pisteet = 112
        elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 5: pisteet = 111
        elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 5: pisteet = 110
        elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 5: pisteet = 109

        elif Kädet.laskeSantut(card1, card2, card3, card4, card5) == 4: pisteet = 108
        elif Kädet.laskeOlvit(card1, card2, card3, card4, card5) == 4: pisteet = 107
        elif Kädet.laskeKarhut(card1, card2, card3, card4, card5) == 4: pisteet = 106
        elif Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 4: pisteet = 105
        elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 4: pisteet = 104
        elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 4: pisteet = 103
        elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 4: pisteet = 102
        elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 4: pisteet = 101

        elif Kädet.laskeSantut(card1, card2, card3, card4, card5) == 3:
            if Kädet.laskeOlvit(card1, card2, card3, card4, card5) == 2: pisteet = 100
            elif Kädet.laskeKarhut(card1, card2, card3, card4, card5) == 2: pisteet = 99
            elif Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 2: pisteet = 98
            elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 2: pisteet = 97
            elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 2: pisteet = 96
            elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2: pisteet = 95
            elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: pisteet = 94
            else: pisteet = 44
        elif Kädet.laskeOlvit(card1, card2, card3, card4, card5) == 3:
            if Kädet.laskeSantut(card1, card2, card3, card4, card5) == 2: pisteet = 93
            elif Kädet.laskeKarhut(card1, card2, card3, card4, card5) == 2: pisteet = 92
            elif Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 2: pisteet = 91
            elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 2: pisteet = 90
            elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 2: pisteet = 89
            elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2: pisteet = 88
            elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: pisteet = 87
            else: pisteet = 43
        elif Kädet.laskeKarhut(card1, card2, card3, card4, card5) == 3:
            if Kädet.laskeSantut(card1, card2, card3, card4, card5) == 2: pisteet = 86
            elif Kädet.laskeOlvit(card1, card2, card3, card4, card5) == 2: pisteet = 85
            elif Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 2: pisteet = 84
            elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 2: pisteet = 83
            elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 2: pisteet = 82
            elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2: pisteet = 81
            elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: pisteet = 80
            else: pisteet = 42
        elif Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 3:
            if Kädet.laskeSantut(card1, card2, card3, card4, card5) == 2: pisteet = 79
            elif Kädet.laskeOlvit(card1, card2, card3, card4, card5) == 2: pisteet = 78
            elif Kädet.laskeKarhut(card1, card2, card3, card4, card5) == 2: pisteet = 77
            elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 2: pisteet = 76
            elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 2: pisteet = 75
            elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2: pisteet = 74
            elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: pisteet = 73
            else: pisteet = 41
        elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 3:
            if Kädet.laskeSantut(card1, card2, card3, card4, card5) == 2: pisteet = 72
            elif Kädet.laskeOlvit(card1, card2, card3, card4, card5) == 2: pisteet = 71
            elif Kädet.laskeKarhut(card1, card2, card3, card4, card5) == 2: pisteet = 70
            elif Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 2: pisteet = 69
            elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 2: pisteet = 68
            elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2: pisteet = 67
            elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: pisteet = 66
            else: pisteet = 40
        elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 3:
            if Kädet.laskeSantut(card1, card2, card3, card4, card5) == 2: pisteet = 65
            elif Kädet.laskeOlvit(card1, card2, card3, card4, card5) == 2: pisteet = 64
            elif Kädet.laskeKarhut(card1, card2, card3, card4, card5) == 2: pisteet = 63
            elif Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 2: pisteet = 62
            elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 2: pisteet = 61
            elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2: pisteet = 60
            elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: pisteet = 59
            else: pisteet = 39
        elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 3:
            if Kädet.laskeSantut(card1, card2, card3, card4, card5) == 2: pisteet = 58
            elif Kädet.laskeOlvit(card1, card2, card3, card4, card5) == 2: pisteet = 57
            elif Kädet.laskeKarhut(card1, card2, card3, card4, card5) == 2: pisteet = 56
            elif Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 2: pisteet = 55
            elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 2: pisteet = 54
            elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 2: pisteet = 53
            elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: pisteet = 52
            else: pisteet = 38
        elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 3:
            if Kädet.laskeSantut(card1, card2, card3, card4, card5) == 2: pisteet = 51
            elif Kädet.laskeOlvit(card1, card2, card3, card4, card5) == 2: pisteet = 50
            elif Kädet.laskeKarhut(card1, card2, card3, card4, card5) == 2: pisteet = 49
            elif Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 2: pisteet = 48
            elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 2: pisteet = 47
            elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 2: pisteet = 46
            elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2: pisteet = 45
            else: pisteet = 37
        
        elif Kädet.laskeSantut(card1, card2, card3, card4, card5) == 2:
            if Kädet.laskeOlvit(card1, card2, card3, card4, card5) == 2: pisteet = 36
            elif Kädet.laskeKarhut(card1, card2, card3, card4, card5) == 2: pisteet = 35
            elif Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 2: pisteet = 34
            elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 2: pisteet = 33
            elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 2: pisteet = 32
            elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2: pisteet = 31
            elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: pisteet = 30
            else: pisteet = 8
        elif Kädet.laskeOlvit(card1, card2, card3, card4, card5) == 2:
            if Kädet.laskeKarhut(card1, card2, card3, card4, card5) == 2: pisteet = 29
            elif Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 2: pisteet = 28
            elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 2: pisteet = 27
            elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 2: pisteet = 26
            elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2: pisteet = 25
            elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: pisteet = 24
            else: pisteet = 7
        elif Kädet.laskeKarhut(card1, card2, card3, card4, card5) == 2:
            if Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 2: pisteet = 23
            elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 2: pisteet = 22
            elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 2: pisteet = 21
            elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2: pisteet = 20
            elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: pisteet = 19
            else: pisteet = 6
        elif Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 2:
            if Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 2: pisteet = 18
            elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 2: pisteet = 17
            elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2: pisteet = 16
            elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: pisteet = 15
            else: pisteet = 5
        elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 2:
            if Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 2: pisteet = 14
            elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2: pisteet = 13
            elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: pisteet = 12
            else: pisteet = 4
        elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 2:
            if Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2: pisteet = 11
            elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: pisteet = 10
            else: pisteet = 3
        elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2:
            if Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: pisteet = 9
            else: pisteet = 2
        elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: pisteet = 1
        else: pisteet = 0
        return pisteet
    
    def haeKäsiTyyppi(card1, card2, card3, card4, card5):
        käsiTyyppi = "Paskaa"
        if Kädet.laskeSantut(card1, card2, card3, card4, card5) == 5: käsiTyyppi = "Vitoset"
        elif Kädet.laskeOlvit(card1, card2, card3, card4, card5) == 5: käsiTyyppi = "Vitoset"
        elif Kädet.laskeKarhut(card1, card2, card3, card4, card5) == 5: käsiTyyppi = "Vitoset"
        elif Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 5: käsiTyyppi = "Vitoset"
        elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 5: käsiTyyppi = "Vitoset"
        elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 5: käsiTyyppi = "Vitoset"
        elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 5: käsiTyyppi = "Vitoset"
        elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 5: käsiTyyppi = "Vitoset"

        elif Kädet.laskeSantut(card1, card2, card3, card4, card5) == 4: käsiTyyppi = "Neloset"
        elif Kädet.laskeOlvit(card1, card2, card3, card4, card5) == 4: käsiTyyppi = "Neloset"
        elif Kädet.laskeKarhut(card1, card2, card3, card4, card5) == 4: käsiTyyppi = "Neloset"
        elif Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 4: käsiTyyppi = "Neloset"
        elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 4: käsiTyyppi = "Neloset"
        elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 4: käsiTyyppi = "Neloset"
        elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 4: käsiTyyppi = "Neloset"
        elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 4: käsiTyyppi = "Neloset"

        elif Kädet.laskeSantut(card1, card2, card3, card4, card5) == 3:
            if Kädet.laskeOlvit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeKarhut(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            else: käsiTyyppi = "Kolmoset"
        elif Kädet.laskeOlvit(card1, card2, card3, card4, card5) == 3:
            if Kädet.laskeSantut(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeKarhut(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            else: käsiTyyppi = "Kolmoset"
        elif Kädet.laskeKarhut(card1, card2, card3, card4, card5) == 3:
            if Kädet.laskeSantut(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeOlvit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            else: käsiTyyppi = "Kolmoset"
        elif Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 3:
            if Kädet.laskeSantut(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeOlvit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeKarhut(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            else: käsiTyyppi = "Kolmoset"
        elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 3:
            if Kädet.laskeSantut(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeOlvit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeKarhut(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            else: käsiTyyppi = "Kolmoset"
        elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 3:
            if Kädet.laskeSantut(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeOlvit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeKarhut(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            else: käsiTyyppi = "Kolmoset"
        elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 3:
            if Kädet.laskeSantut(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeOlvit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeKarhut(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            else: käsiTyyppi = "Kolmoset"
        elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 3:
            if Kädet.laskeSantut(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeOlvit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeKarhut(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "Täyskäsi"
            else: käsiTyyppi = "Kolmoset"
        
        elif Kädet.laskeSantut(card1, card2, card3, card4, card5) == 2:
            if Kädet.laskeOlvit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            elif Kädet.laskeKarhut(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            elif Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            else: käsiTyyppi = "1 Pari"
        elif Kädet.laskeOlvit(card1, card2, card3, card4, card5) == 2:
            if Kädet.laskeKarhut(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            elif Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            else: käsiTyyppi = "1 Pari"
        elif Kädet.laskeKarhut(card1, card2, card3, card4, card5) == 2:
            if Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            else: käsiTyyppi = "1 Pari"
        elif Kädet.laskeAlecoqit(card1, card2, card3, card4, card5) == 2:
            if Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            else: käsiTyyppi = "1 Pari"
        elif Kädet.laskeLapparit(card1, card2, card3, card4, card5) == 2:
            if Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            else: käsiTyyppi = "1 Pari"
        elif Kädet.laskeKarjalat(card1, card2, card3, card4, card5) == 2:
            if Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            else: käsiTyyppi = "1 Pari"
        elif Kädet.laskeOlutOluet(card1, card2, card3, card4, card5) == 2:
            if Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "2 Paria"
            else: käsiTyyppi = "1 Pari"
        elif Kädet.laskeKuparit(card1, card2, card3, card4, card5) == 2: käsiTyyppi = "1 Pari"
        else: käsiTyyppi = "Paskaa"
        return käsiTyyppi
    
    def laskeJuomisMäärä(card1, card2, card3, card4, card5):
        juomisMäärä = 0
        if Kädet.haeKäsiTyyppi(card1, card2, card3, card4, card5) is "Vitoset":
            juomisMäärä = 12
        elif Kädet.haeKäsiTyyppi(card1, card2, card3, card4, card5) is "Neloset":
            juomisMäärä = 8
        elif Kädet.haeKäsiTyyppi(card1, card2, card3, card4, card5) is "Täyskäsi":
            juomisMäärä = 6
        elif Kädet.haeKäsiTyyppi(card1, card2, card3, card4, card5) is "Kolmoset":
            juomisMäärä = 4
        elif Kädet.haeKäsiTyyppi(card1, card2, card3, card4, card5) is "2 Paria":
            juomisMäärä = 3
        elif Kädet.haeKäsiTyyppi(card1, card2, card3, card4, card5) is "1 Pari":
            juomisMäärä = 2
        else:
            juomisMäärä = 0
        return juomisMäärä
