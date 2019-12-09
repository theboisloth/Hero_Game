import random
#Spider has no crit chance

#Damage ranges
DMGPOTION_DAMAGE_RANGE = ((3, 15), (10, 25), (15, 30))
HEALTH_POTION_HEALRATE = (20, 50, 70)

MISS_CHANCE_RANGE = (15, 10, 2)
MISS_CHANCE = 0

HEALTH_RANGE = (150, 200, 300)
health = 0


def configure_difficulty(difficultyLevel):
    global health, MISS_CHANCE, DMGPOTION_DAMAGE_RANGE,\
        DMGPOTION_DAMAGE_LO, DMGPOTION_DAMAGE_HI, HEALTH_POTION_HEALRATE

    DMGPOTION_DAMAGE_LO, DMGPOTION_DAMAGE_HI = DMGPOTION_DAMAGE_RANGE[difficultyLevel]
    MISS_CHANCE = MISS_CHANCE_RANGE[difficultyLevel]
    HEALTH_POTION_HEALRATE = HEALTH_POTION_HEALRATE[difficultyLevel]
    health = HEALTH_RANGE[difficultyLevel]
    
def deal_damage(damage):
    global health
    health -= damage

def heal_damage(healAmount):
    global health
    health += healAmount

def attack(is_stunned): #Expects a bool
    damage = 0
    didPoison = False
    didHeal = False
    if not is_stunned:
        roll = random.randint(1, 100)
        if roll > MISS_CHANCE:
            roll = random.randint(1, 100)
            
            if roll > 40:
                damage = random.randint(DMGPOTION_DAMAGE_LO, DMGPOTION_DAMAGE_HI)
                print(f"The Witch threw a damaging potion on you for {damage} damage!")
            
            elif roll <= 30:
                damage = random.randint(DMGPOTION_DAMAGE_LO, DMGPOTION_DAMAGE_HI)
                print(f"The Witch threw a poison potion on you!")
                didPoison = True
            
            elif roll > 30 and roll < 41:
                print("The Witch used a potion to heal herself!")
                heal_damage(HEALTH_POTION_HEALRATE)
                didHeal = True

    return damage, didPoison, didHeal
