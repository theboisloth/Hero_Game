import random
#Spider has no crit chance

#Damage ranges
BITE_DAMAGE_RANGE = ((3, 15), (10, 25), (15, 30))

MISS_CHANCE_RANGE = (15, 10, 2)
MISS_CHANCE = 0

HEALTH_RANGE = (150, 200, 350)
health = 0


def configure_difficulty(difficultyLevel):
    global health, MISS_CHANCE, BITE_DAMAGE_RANGE,\
        BITE_DAMAGE_LO, BITE_DAMAGE_HI

    BITE_DAMAGE_LO, BITE_DAMAGE_HI = BITE_DAMAGE_RANGE[difficultyLevel]
    MISS_CHANCE = MISS_CHANCE_RANGE[difficultyLevel]
    health = HEALTH_RANGE[difficultyLevel]
    
def deal_damage(damage):
    global health
    health -= damage

def attack(is_stunned): #Expects a bool
    damage = 0
    didPoison = False
    if not is_stunned:
        roll = random.randint(1, 100)
        if roll > MISS_CHANCE:    
            damage = random.randint(BITE_DAMAGE_LO, BITE_DAMAGE_HI)
            print(f"The Spider bit you for {damage} damage!")
            roll = random.randint(1, 100)
            if roll < 30:
                didPoison = True

    return damage, didPoison