class HandTypes:
    def countStars(card1, card2, card3, card4, card5):
        stars = 0
        if card1.type == 5:
            stars = stars + 1
        if card2.type == 5:
            stars = stars + 1
        if card3.type == 5:
            stars = stars + 1
        if card4.type == 5:
            stars = stars + 1
        if card5.type == 5:
            stars = stars + 1
        return stars
    
    def countMarios(card1, card2, card3, card4, card5):
        marios = 0
        if card1.type == 4:
            marios = marios + 1
        if card2.type == 4:
            marios = marios + 1
        if card3.type == 4:
            marios = marios + 1
        if card4.type == 4:
            marios = marios + 1
        if card5.type == 4:
            marios = marios + 1
        return marios
    
    def countLuigis(card1, card2, card3, card4, card5):
        luigis = 0
        if card1.type == 3:
            luigis = luigis + 1
        if card2.type == 3:
            luigis = luigis + 1
        if card3.type == 3:
            luigis = luigis + 1
        if card4.type == 3:
            luigis = luigis + 1
        if card5.type == 3:
            luigis = luigis + 1
        return luigis
    
    def countFlowers(card1, card2, card3, card4, card5):
        flowers = 0
        if card1.type == 2:
            flowers = flowers + 1
        if card2.type == 2:
            flowers = flowers + 1
        if card3.type == 2:
            flowers = flowers + 1
        if card4.type == 2:
            flowers = flowers + 1
        if card5.type == 2:
            flowers = flowers + 1
        return flowers
    
    def countMushrooms(card1, card2, card3, card4, card5):
        mushrooms = 0
        if card1.type == 1:
            mushrooms = mushrooms + 1
        if card2.type == 1:
            mushrooms = mushrooms + 1
        if card3.type == 1:
            mushrooms = mushrooms + 1
        if card4.type == 1:
            mushrooms = mushrooms + 1
        if card5.type == 1:
            mushrooms = mushrooms + 1
        return mushrooms
    
    def countClouds(card1, card2, card3, card4, card5):
        clouds = 0
        if card1.type == 0:
            clouds = clouds + 1
        if card2.type == 0:
            clouds = clouds + 1
        if card3.type == 0:
            clouds = clouds + 1
        if card4.type == 0:
            clouds = clouds + 1
        if card5.type == 0:
            clouds = clouds + 1
        return clouds
    
    def countScore(card1, card2, card3, card4, card5):
        score = 0
        if HandTypes.countStars(card1, card2, card3, card4, card5) == 5: score = 69
        elif HandTypes.countMarios(card1, card2, card3, card4, card5) == 5: score = 68
        elif HandTypes.countLuigis(card1, card2, card3, card4, card5) == 5: score = 67
        elif HandTypes.countFlowers(card1, card2, card3, card4, card5) == 5: score = 66
        elif HandTypes.countMushrooms(card1, card2, card3, card4, card5) == 5: score = 65
        elif HandTypes.countClouds(card1, card2, card3, card4, card5) == 5: score = 64
        elif HandTypes.countStars(card1, card2, card3, card4, card5) == 4: score = 63
        elif HandTypes.countMarios(card1, card2, card3, card4, card5) == 4: score = 62
        elif HandTypes.countLuigis(card1, card2, card3, card4, card5) == 4: score = 61
        elif HandTypes.countFlowers(card1, card2, card3, card4, card5) == 4: score = 60
        elif HandTypes.countMushrooms(card1, card2, card3, card4, card5) == 4: score = 59
        elif HandTypes.countClouds(card1, card2, card3, card4, card5) == 4: score = 58
        elif HandTypes.countStars(card1, card2, card3, card4, card5) == 3:
            if HandTypes.countMarios(card1, card2, card3, card4, card5) == 2: score = 57
            elif HandTypes.countLuigis(card1, card2, card3, card4, card5) == 2: score = 56
            elif HandTypes.countFlowers(card1, card2, card3, card4, card5) == 2: score = 55
            elif HandTypes.countMushrooms(card1, card2, card3, card4, card5) == 2: score = 54
            elif HandTypes.countClouds(card1, card2, card3, card4, card5) == 2: score = 53
            else: score = 27
        elif HandTypes.countMarios(card1, card2, card3, card4, card5) == 3:
            if HandTypes.countStars(card1, card2, card3, card4, card5) == 2: score = 52
            elif HandTypes.countLuigis(card1, card2, card3, card4, card5) == 2: score = 51
            elif HandTypes.countFlowers(card1, card2, card3, card4, card5) == 2: score = 50
            elif HandTypes.countMushrooms(card1, card2, card3, card4, card5) == 2: score = 49
            elif HandTypes.countClouds(card1, card2, card3, card4, card5) == 2: score = 48
            else: score = 26
        elif HandTypes.countLuigis(card1, card2, card3, card4, card5) == 3:
            if HandTypes.countStars(card1, card2, card3, card4, card5) == 2: score = 47
            elif HandTypes.countMarios(card1, card2, card3, card4, card5) == 2: score = 46
            elif HandTypes.countFlowers(card1, card2, card3, card4, card5) == 2: score = 45
            elif HandTypes.countMushrooms(card1, card2, card3, card4, card5) == 2: score = 44
            elif HandTypes.countClouds(card1, card2, card3, card4, card5) == 2: score = 43
            else: score = 25
        elif HandTypes.countFlowers(card1, card2, card3, card4, card5) == 3:
            if HandTypes.countStars(card1, card2, card3, card4, card5) == 2: score = 42
            elif HandTypes.countMarios(card1, card2, card3, card4, card5) == 2: score = 41
            elif HandTypes.countLuigis(card1, card2, card3, card4, card5) == 2: score = 40
            elif HandTypes.countMushrooms(card1, card2, card3, card4, card5) == 2: score = 39
            elif HandTypes.countClouds(card1, card2, card3, card4, card5) == 2: score = 38
            else: score = 24
        elif HandTypes.countMushrooms(card1, card2, card3, card4, card5) == 3:
            if HandTypes.countStars(card1, card2, card3, card4, card5) == 2: score = 37
            elif HandTypes.countMarios(card1, card2, card3, card4, card5) == 2: score = 36
            elif HandTypes.countLuigis(card1, card2, card3, card4, card5) == 2: score = 35
            elif HandTypes.countFlowers(card1, card2, card3, card4, card5) == 2: score = 34
            elif HandTypes.countClouds(card1, card2, card3, card4, card5) == 2: score = 33
            else: score = 23
        elif HandTypes.countClouds(card1, card2, card3, card4, card5) == 3:
            if HandTypes.countStars(card1, card2, card3, card4, card5) == 2: score = 32
            elif HandTypes.countMarios(card1, card2, card3, card4, card5) == 2: score = 31
            elif HandTypes.countLuigis(card1, card2, card3, card4, card5) == 2: score = 30
            elif HandTypes.countFlowers(card1, card2, card3, card4, card5) == 2: score = 29
            elif HandTypes.countMushrooms(card1, card2, card3, card4, card5) == 2: score = 28
            else: score = 22
        elif HandTypes.countStars(card1, card2, card3, card4, card5) == 2:
            if HandTypes.countMarios(card1, card2, card3, card4, card5) == 2: score = 21
            elif HandTypes.countLuigis(card1, card2, card3, card4, card5) == 2: score = 20
            elif HandTypes.countFlowers(card1, card2, card3, card4, card5) == 2: score = 19
            elif HandTypes.countMushrooms(card1, card2, card3, card4, card5) == 2: score = 18
            elif HandTypes.countClouds(card1, card2, card3, card4, card5) == 2: score = 17
            else: score = 6
        elif HandTypes.countMarios(card1, card2, card3, card4, card5) == 2:
            if HandTypes.countLuigis(card1, card2, card3, card4, card5) == 2: score = 16
            elif HandTypes.countFlowers(card1, card2, card3, card4, card5) == 2: score = 15
            elif HandTypes.countMushrooms(card1, card2, card3, card4, card5) == 2: score = 14
            elif HandTypes.countClouds(card1, card2, card3, card4, card5) == 2: score = 13
            else: score = 5
        elif HandTypes.countLuigis(card1, card2, card3, card4, card5) == 2:
            if HandTypes.countFlowers(card1, card2, card3, card4, card5) == 2: score = 12
            elif HandTypes.countMushrooms(card1, card2, card3, card4, card5) == 2: score = 11
            elif HandTypes.countClouds(card1, card2, card3, card4, card5) == 2: score = 10
            else: score = 4
        elif HandTypes.countFlowers(card1, card2, card3, card4, card5) == 2:
            if HandTypes.countMushrooms(card1, card2, card3, card4, card5) == 2: score = 9
            elif HandTypes.countClouds(card1, card2, card3, card4, card5) == 2: score = 8
            else: score = 3
        elif HandTypes.countMushrooms(card1, card2, card3, card4, card5) == 2:
            if HandTypes.countClouds(card1, card2, card3, card4, card5) == 2: score = 7
            else: score = 2
        elif HandTypes.countClouds(card1, card2, card3, card4, card5) == 2: score = 1
        else: score = 0
        return score
    
    def findHandType(card1, card2, card3, card4, card5):
        handType = "Paskaa"
        if HandTypes.countStars(card1, card2, card3, card4, card5) == 5: handType = "Vitoset"
        elif HandTypes.countMarios(card1, card2, card3, card4, card5) == 5: handType = "Vitoset"
        elif HandTypes.countLuigis(card1, card2, card3, card4, card5) == 5: handType = "Vitoset"
        elif HandTypes.countFlowers(card1, card2, card3, card4, card5) == 5: handType = "Vitoset"
        elif HandTypes.countMushrooms(card1, card2, card3, card4, card5) == 5: handType = "Vitoset"
        elif HandTypes.countClouds(card1, card2, card3, card4, card5) == 5: handType = "Vitoset"
        elif HandTypes.countStars(card1, card2, card3, card4, card5) == 4: handType = "Neloset"
        elif HandTypes.countMarios(card1, card2, card3, card4, card5) == 4: handType = "Neloset"
        elif HandTypes.countLuigis(card1, card2, card3, card4, card5) == 4: handType = "Neloset"
        elif HandTypes.countFlowers(card1, card2, card3, card4, card5) == 4: handType = "Neloset"
        elif HandTypes.countMushrooms(card1, card2, card3, card4, card5) == 4: handType = "Neloset"
        elif HandTypes.countClouds(card1, card2, card3, card4, card5) == 4: handType = "Neloset"
        elif HandTypes.countStars(card1, card2, card3, card4, card5) == 3:
            if HandTypes.countMarios(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            elif HandTypes.countLuigis(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            elif HandTypes.countFlowers(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            elif HandTypes.countMushrooms(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            elif HandTypes.countClouds(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            else: handType = "Kolmoset"
        elif HandTypes.countMarios(card1, card2, card3, card4, card5) == 3:
            if HandTypes.countStars(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            elif HandTypes.countLuigis(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            elif HandTypes.countFlowers(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            elif HandTypes.countMushrooms(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            elif HandTypes.countClouds(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            else: handType = "Kolmoset"
        elif HandTypes.countLuigis(card1, card2, card3, card4, card5) == 3:
            if HandTypes.countStars(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            elif HandTypes.countMarios(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            elif HandTypes.countFlowers(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            elif HandTypes.countMushrooms(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            elif HandTypes.countClouds(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            else: handType = "Kolmoset"
        elif HandTypes.countFlowers(card1, card2, card3, card4, card5) == 3:
            if HandTypes.countStars(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            elif HandTypes.countMarios(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            elif HandTypes.countLuigis(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            elif HandTypes.countMushrooms(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            elif HandTypes.countClouds(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            else: handType = "Kolmoset"
        elif HandTypes.countMushrooms(card1, card2, card3, card4, card5) == 3:
            if HandTypes.countStars(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            elif HandTypes.countMarios(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            elif HandTypes.countLuigis(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            elif HandTypes.countFlowers(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            elif HandTypes.countClouds(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            else: handType = "Kolmoset"
        elif HandTypes.countClouds(card1, card2, card3, card4, card5) == 3:
            if HandTypes.countStars(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            elif HandTypes.countMarios(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            elif HandTypes.countLuigis(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            elif HandTypes.countFlowers(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            elif HandTypes.countMushrooms(card1, card2, card3, card4, card5) == 2: handType = "Täyskäsi"
            else: handType = "Kolmoset"
        elif HandTypes.countStars(card1, card2, card3, card4, card5) == 2:
            if HandTypes.countMarios(card1, card2, card3, card4, card5) == 2: handType = "2 Paria"
            elif HandTypes.countLuigis(card1, card2, card3, card4, card5) == 2: handType = "2 Paria"
            elif HandTypes.countFlowers(card1, card2, card3, card4, card5) == 2: handType = "2 Paria"
            elif HandTypes.countMushrooms(card1, card2, card3, card4, card5) == 2: handType = "2 Paria"
            elif HandTypes.countClouds(card1, card2, card3, card4, card5) == 2: handType = "2 Paria"
            else: handType = "1 Pari"
        elif HandTypes.countMarios(card1, card2, card3, card4, card5) == 2:
            if HandTypes.countLuigis(card1, card2, card3, card4, card5) == 2: handType = "2 Paria"
            elif HandTypes.countFlowers(card1, card2, card3, card4, card5) == 2: handType = "2 Paria"
            elif HandTypes.countMushrooms(card1, card2, card3, card4, card5) == 2: handType = "2 Paria"
            elif HandTypes.countClouds(card1, card2, card3, card4, card5) == 2: handType = "2 Paria"
            else: handType = "1 Pari"
        elif HandTypes.countLuigis(card1, card2, card3, card4, card5) == 2:
            if HandTypes.countFlowers(card1, card2, card3, card4, card5) == 2: handType = "2 Paria"
            elif HandTypes.countMushrooms(card1, card2, card3, card4, card5) == 2: handType = "2 Paria"
            elif HandTypes.countClouds(card1, card2, card3, card4, card5) == 2: handType = "2 Paria"
            else: handType = "1 Pari"
        elif HandTypes.countFlowers(card1, card2, card3, card4, card5) == 2:
            if HandTypes.countMushrooms(card1, card2, card3, card4, card5) == 2: handType = "2 Paria"
            elif HandTypes.countClouds(card1, card2, card3, card4, card5) == 2: handType = "2 Paria"
            else: handType = "1 Pari"
        elif HandTypes.countMushrooms(card1, card2, card3, card4, card5) == 2:
            if HandTypes.countClouds(card1, card2, card3, card4, card5) == 2: handType = "2 Paria"
            else: handType = "1 Pari"
        elif HandTypes.countClouds(card1, card2, card3, card4, card5) == 2: handType = "1 Pari"
        else: handType = "Paskaa"
        return handType

