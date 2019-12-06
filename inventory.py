import hero
import random
import os.path
#Completely new file from original game 

#IRONSKIN POTIONS ARE NOT IMPLEMENTED PROPERLY YET


#Offensive Inventory Items (These Never Miss Opponent)
FIREBOMBS = [3, 1, 0]
FIREBOMB_DAMAGE = [100, 75, 40] 

#Defensive Items

#Healing Food
MAC_N_CHEESE = [0, 0, 0] #Heals Fully, pricey (if shop is implemented), 
#unimplemented


#Health Potions
SMALL_HEALTH_POTS = [5, 2, 1]
SMALL_HEALTHPOT_HEALRATE = [75, 50, 25]
HEALTH_POTS = [3, 2, 1]
HEALTHPOT_HEALRATE = [110, 85, 60]

#Buff Items
IRONSKIN_POTS = [5, 2, 0]
IRONSKIN_EFFECTRATE = [.25, .5, .75]

MUTTON_CHOP = [2, 1, 0] #MUTTON, YET TO BE IMPLEMENTED

def configure_difficulty(difficulty_level):
    global FIREBOMBS, SMALL_HEALTH_POTS, HEALTH_POTS, IRONSKIN_POTS, \
        FIREBOMB_DAMAGE, SMALL_HEALTHPOT_HEALRATE, HEALTHPOT_HEALRATE, \
        IRONSKIN_EFFECTRATE, IRONSKIN_POTS, MAC_N_CHEESE, MUTTON_CHOP

    FIREBOMBS = FIREBOMBS[difficulty_level]
    FIREBOMB_DAMAGE = FIREBOMB_DAMAGE[difficulty_level]
    

    SMALL_HEALTH_POTS = SMALL_HEALTH_POTS[difficulty_level]
    HEALTH_POTS = HEALTH_POTS[difficulty_level]
    
    SMALL_HEALTHPOT_HEALRATE = SMALL_HEALTHPOT_HEALRATE[difficulty_level]
    HEALTHPOT_HEALRATE = HEALTHPOT_HEALRATE[difficulty_level]
    
    MAC_N_CHEESE = MAC_N_CHEESE[difficulty_level]

    IRONSKIN_POTS = IRONSKIN_POTS[difficulty_level]
    IRONSKIN_EFFECTRATE = IRONSKIN_EFFECTRATE[difficulty_level]
    
    MUTTON_CHOP = MUTTON_CHOP[difficulty_level]

def displayItemSelect():
    global FIREBOMBS, SMALL_HEALTH_POTS, HEALTH_POTS, IRONSKIN_POTS
    print(f"[1]Firebomb(x{FIREBOMBS})\n"
    f"[2]Small Health Potion(x{SMALL_HEALTH_POTS})\n"
    f"[3]Health Potion(x{HEALTH_POTS})\n"
    f"[4]Ironskin Potion(x{IRONSKIN_POTS})\n"
    "[5]Item Info")
    
    print("Choose an Item To Use: ", end = "")
    itemUsed = int(input())

    while itemUsed not in [1, 2, 3, 4, 5]:
        print(f"[1]Firebomb(x{FIREBOMBS})\n"
        f"[2]Small Health Potion(x{SMALL_HEALTH_POTS})\n"
        f"[3]Health Potion(x{HEALTH_POTS})\n"
        f"[4]Ironskin Potion(x{IRONSKIN_POTS})\n"
        "[5]Item Info")
        itemUsed = int(input(f"{itemUsed} is invalid: Enter a valid choice: "))

    return itemUsed

def describeItems(): #Implementing...
    
    global FIREBOMBS, SMALL_HEALTH_POTS, HEALTH_POTS, IRONSKIN_POTS
    print(f"Firebombs: Throw a Firebomb to deal {FIREBOMB_DAMAGE} damage to the enemy.")
    print(f"Small Health Potion: Heals the Hero for {SMALL_HEALTHPOT_HEALRATE} health") 
    print(f"Health Potion: Heals the Hero for {HEALTHPOT_HEALRATE} health") 
    print(f"Ironskin Potion: Increases Defense for 2-5 turns.") 


def useItem(item):#Returns damage if firebomb used, otherwise fruitless
    
    global FIREBOMBS, FIREBOMB_DAMAGE, SMALL_HEALTH_POTS, \
        SMALL_HEALTHPOT_HEALRATE, HEALTH_POTS, HEALTHPOT_HEALRATE,\
        IRONSKIN_POTS, IRONSKIN_EFFECTRATE
    if item == 1:

        damage = int(FIREBOMB_DAMAGE)
        
        FIREBOMBS = int(FIREBOMBS) #Ensure Loading doesn't mess up data type

        FIREBOMBS -= 1
        print(f"You Used a Firebomb for {FIREBOMB_DAMAGE} damage!")
        print(f"You have {FIREBOMBS} Firebombs left.")
        return damage

    elif item == 2:

        hero.healDamage(SMALL_HEALTHPOT_HEALRATE)
        SMALL_HEALTH_POTS -= 1
        print("You used a Small Health Potion and healed for "
        f"{SMALL_HEALTHPOT_HEALRATE}")
    elif item == 3:
        hero.healDamage(HEALTHPOT_HEALRATE)
        HEALTH_POTS -= 1
        print("You used a Health Potion and healed for "
        f"{HEALTHPOT_HEALRATE}")
    
    elif item == 4: #Ironskin potion not implemented yet
        global IRONSKIN_POTS, IRONSKIN_EFFECTRATE
        IRONSKIN_POTS -= 1
        print(f"You used an Ironskin Potion, you take "
        f"{IRONSKIN_EFFECTRATE * 100}% of the Damage you normally would!")

def addItem(itemValue, goldSpent):
    global FIREBOMBS, SMALL_HEALTH_POTS, HEALTH_POTS, IRONSKIN_POTS
    if goldSpent == 0:
        if itemValue == 1:
            FIREBOMBS += 1
        elif itemValue == 2:
            SMALL_HEALTH_POTS += 1
        elif itemValue == 3:
            HEALTH_POTS += 1
        elif itemValue == 4:
            IRONSKIN_POTS += 1
    
    if goldSpent != 0:
        if itemValue == 1:
            FIREBOMBS += 1
            hero.updateGold(False, goldSpent)
        elif itemValue == 2:
            SMALL_HEALTH_POTS += 1
            hero.updateGold(False, goldSpent)
        elif itemValue == 3:
            HEALTH_POTS += 1
            hero.updateGold(False, goldSpent)
        elif itemValue == 4:
            IRONSKIN_POTS += 1
            hero.updateGold(False, goldSpent)


def get_save_data():
    global FIREBOMBS, SMALL_HEALTH_POTS, HEALTH_POTS, IRONSKIN_POTS, \
        FIREBOMB_DAMAGE, SMALL_HEALTHPOT_HEALRATE, HEALTHPOT_HEALRATE, \
        IRONSKIN_EFFECTRATE, IRONSKIN_POTS, MAC_N_CHEESE, MUTTON_CHOP
    
    inventoryState = [FIREBOMBS, SMALL_HEALTH_POTS, HEALTH_POTS, IRONSKIN_POTS,\
        FIREBOMB_DAMAGE, SMALL_HEALTHPOT_HEALRATE, HEALTHPOT_HEALRATE, \
        IRONSKIN_EFFECTRATE, IRONSKIN_POTS, MAC_N_CHEESE, MUTTON_CHOP]
    return inventoryState

def load_save_data(inventoryState):
    global FIREBOMBS, SMALL_HEALTH_POTS, HEALTH_POTS, IRONSKIN_POTS, \
        FIREBOMB_DAMAGE, SMALL_HEALTHPOT_HEALRATE, HEALTHPOT_HEALRATE, \
        IRONSKIN_EFFECTRATE, IRONSKIN_POTS, MAC_N_CHEESE, MUTTON_CHOP

    (FIREBOMBS, SMALL_HEALTH_POTS, HEALTH_POTS, IRONSKIN_POTS,
        FIREBOMB_DAMAGE, SMALL_HEALTHPOT_HEALRATE, HEALTHPOT_HEALRATE,
        IRONSKIN_EFFECTRATE, IRONSKIN_POTS, MAC_N_CHEESE, MUTTON_CHOP) = inventoryState