import random
#Wolf has no crit chance

#Damage ranges
BITE_DAMAGE_RANGE = ((1, 10), (5, 15), (8, 20))
SCRATCH_DAMAGE_RANGE = ((10, 30), (15, 35), (20, 40))
SEVER_DAMAGE_RANGE = ((20, 40), (25, 45), (30, 50)) #Sever attack has a chance to bleed opponent

SEVER_MISS_CHANCE_RANGE = (50, 40, 25)
MISS_CHANCE_RANGE = (15, 10, 2)
BLEED_CHANCE_RANGE = (70, 40, 20)

HEALTH_RANGE = (250, 350, 500)
health = 0

def configure_difficulty(difficultyLevel):
    global BITE_DAMAGE_RANGE, SCRATCH_DAMAGE_RANGE, SEVER_DAMAGE_RANGE,\
        SEVER_MISS_CHANCE_RANGE, MISS_CHANCE, BLEED_CHANCE, HEALTH_RANGE, \
            BITE_DAMAGE_LO, BITE_DAMAGE_HI, SCRATCH_DAMAGE_LO, \
                SCRATCH_DAMAGE_HI, SEVER_DAMAGE_LO, SEVER_DAMAGE_HI, \
                    health, SEVER_MISS_CHANCE, MISS_CHANCE_RANGE, \
                        BLEED_CHANCE_RANGE
    
    BITE_DAMAGE_LO, BITE_DAMAGE_HI = BITE_DAMAGE_RANGE[difficultyLevel]
    SCRATCH_DAMAGE_LO, SCRATCH_DAMAGE_HI = SCRATCH_DAMAGE_RANGE[difficultyLevel]
    SEVER_DAMAGE_LO, SEVER_DAMAGE_HI = SEVER_DAMAGE_RANGE[difficultyLevel]
    SEVER_MISS_CHANCE = SEVER_MISS_CHANCE_RANGE[difficultyLevel]
    MISS_CHANCE = MISS_CHANCE_RANGE[difficultyLevel]
    BLEED_CHANCE = BLEED_CHANCE_RANGE[difficultyLevel]
    health = HEALTH_RANGE[difficultyLevel]
    
def deal_damage(damage):
    global health
    health -= damage

def attack(is_stunned): #Expects a bool
    damage = 0
    didbleed = False #Assume no bleed
    if not is_stunned:
        roll = random.randint(1, 100)
        if roll > MISS_CHANCE:    
            roll = random.randint(1, 100)

            if roll <= 40:
                damage = random.randint(BITE_DAMAGE_LO, BITE_DAMAGE_HI)
                print(f"The Wolf bit you for {damage} damage!")
            
            elif roll <= 70:
                damage = random.randint(SCRATCH_DAMAGE_LO, SCRATCH_DAMAGE_HI)
                print(f"The Wolf scratched you for {damage} damage!")
            
            else:
                if roll > SEVER_MISS_CHANCE:
                    damage = random.randint(SCRATCH_DAMAGE_LO, SCRATCH_DAMAGE_HI)
                    print(f"The Wolf Severed a vein of yours for {damage} damage!")
                    
                    roll = random.randint(1, 100)
                    if roll >= BLEED_CHANCE:
                        didbleed = True

    return damage, didbleed