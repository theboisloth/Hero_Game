import random
#Slime has no crit chance

#Damage ranges
SMASH_DAMAGE_RANGE = ((1, 10), (4, 18), (8, 25))

MISS_CHANCE_RANGE = (15, 10, 2)
MISS_CHANCE = 0

HEALTH_RANGE = (100, 150, 200)
health = 0


def configure_difficulty(difficultyLevel):
    global health, MISS_CHANCE, SMASH_DAMAGE_RANGE,\
        SMASH_DAMAGE_LO, SMASH_DAMAGE_HI

    SMASH_DAMAGE_LO, SMASH_DAMAGE_HI = SMASH_DAMAGE_RANGE[difficultyLevel]
    MISS_CHANCE = MISS_CHANCE_RANGE[difficultyLevel]
    health = HEALTH_RANGE[difficultyLevel]
    
def deal_damage(damage):
    global health
    health -= damage

def attack(is_stunned): #Expects a bool
    damage = 0
    if not is_stunned:
        roll = random.randint(1, 100)
        if roll > MISS_CHANCE:    
            damage = random.randint(SMASH_DAMAGE_LO, SMASH_DAMAGE_HI)
            print(f"The Slime smashed into you for {damage} damage!")

    return damage