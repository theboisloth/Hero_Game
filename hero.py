import random
import inventory

# Hit rates
KICK_HIT_RATES = (100, 98, 90)
SWORD_HIT_RATES = (90, 80, 60)
# Default hit rates to normal mode
KICK_HIT_RATE = KICK_HIT_RATES[1]
SWORD_HIT_RATE = SWORD_HIT_RATES[1]

# Damage ranges
KICK_DAMAGE_RANGE = ((15, 35), (8, 20), (5, 10))
SWORD_DAMAGE_RANGE = ((20, 40), (10, 25), (8, 15))
# Default damage ranges to normal mode
KICK_DAMAGE_LO, KICK_DAMAGE_HI = KICK_DAMAGE_RANGE[1] 
SWORD_DAMAGE_LO, SWORD_DAMAGE_HI = SWORD_DAMAGE_RANGE[1]

# Critical rate
CRITICAL_HIT_RATES = (15, 5, 0)
# default critical hit rate to normal mode
CRITICAL_HIT_RATE = CRITICAL_HIT_RATES[1]

# Global var do not access directly
HEALTH_RANGE = (1500, 1000, 750)
# default health to normal mode
health = HEALTH_RANGE[1]

did_block = False

ironskinActive = False #Ironskin potion effect
ironskinRounds = 0

gold = 0

def configure_difficulty (difficulty_level):
    global KICK_HIT_RATE, SWORD_HIT_RATE, KICK_DAMAGE_LO,   \
           KICK_DAMAGE_HI, SWORD_DAMAGE_LO, SWORD_DAMAGE_HI,\
           CRITICAL_HIT_RATE, health
    # Hit rates
    KICK_HIT_RATE = KICK_HIT_RATES[difficulty_level]
    SWORD_HIT_RATE = SWORD_HIT_RATES[difficulty_level]
    # Damage ranges
    KICK_DAMAGE_LO, KICK_DAMAGE_HI = KICK_DAMAGE_RANGE[difficulty_level] 
    SWORD_DAMAGE_LO, SWORD_DAMAGE_HI = SWORD_DAMAGE_RANGE[difficulty_level]
    # Critical rate
    CRITICAL_HIT_RATE = CRITICAL_HIT_RATES[difficulty_level]
    # health range
    health = HEALTH_RANGE[difficulty_level]

def deal_damage (damage):
    global health, ironskinActive, ironskinRounds
    if not did_block and not ironskinActive:
        health -= damage
    
    if not did_block and ironskinActive: #Implements the Ironskin potion effect
        print("Your ironskin prevented some of the damage!")
        damage *= inventory.IRONSKIN_EFFECTRATE
        health -= int(damage)
        ironskinRoll = random.randint(2, 5)
        ironskinRounds += 1
        if ironskinRounds == ironskinRoll:
            ironskinActive = False

def attack (is_poisoned, orc_is_stunned):
    attack_choice = get_attack()

    # Double miss rate if user is poisoned
    miss_rate_modifier = 1
    if is_poisoned:
        miss_rate_modifier = 2

    attack_roll = random.randint(1, 100)
    did_kick = False # assume the hero won't kick the orc
    damage = 0    
    quit_game = False
    
    usedItem = False #Implemented to prevent 'You Missed' message when item used
    
    # attack logic
    if attack_choice == 1 and attack_roll <= KICK_HIT_RATE // miss_rate_modifier:
        damage = calculate_kick_damage() * get_damage_modifiers(orc_is_stunned)
        print(f"You kicked the orc for {damage} damage!")
        did_kick = True
    
    elif attack_choice == 2 and attack_roll <= SWORD_HIT_RATE // miss_rate_modifier:
        damage = calculate_sword_damage() * get_damage_modifiers(orc_is_stunned)
        print(f"You sliced the orc with your sword for {damage} damage!")
    
    elif attack_choice == 3:
        global did_block
        did_block = True
    
    
    
    elif attack_choice == 4: #Entire elif statement is for inventory implement
        usedItem = True
        itemUsed = inventory.displayItemSelect()
        while itemUsed == 5:
            inventory.describeItems()
            itemUsed = inventory.displayItemSelect()
        if itemUsed == 1:
            damage = inventory.useItem(itemUsed)
        elif itemUsed in [2, 3]:
            inventory.useItem(itemUsed)
        elif itemUsed == 4:
            inventory.useItem(itemUsed)
            global ironskinActive
            ironskinActive = True
    
    
    
    elif attack_choice == 5:
        quit_game = True

    return damage, did_kick, quit_game, usedItem


def get_attack ():
    print("\n[1] Kick")
    print("[2] Sword")
    print("[3] Block")
    print("[4] Use Item") #Implements Inventory, new feature
    # print("[5] Save & Quit")
    attack_choice = int(input("Enter your choice: "))
    while attack_choice not in [1, 2, 3, 4, 5]: #Ditto
        attack_choice = int(input(f"{attack_choice} is invalid: Enter your choice: "))
    return attack_choice

def calculate_kick_damage ():
    return random.randint(KICK_DAMAGE_LO, KICK_DAMAGE_HI)

    
def calculate_sword_damage ():
    return random.randint(SWORD_DAMAGE_LO, SWORD_DAMAGE_HI)

def get_crit_damage_modifier ():
    roll_for_crit = random.randint(1, 100)
    damage_modifier = 1 # assume no crit
    if roll_for_crit <= CRITICAL_HIT_RATE: # chance to crit
        print("You landed a critical hit!")
        damage_modifier = 2    
    return damage_modifier

def get_stun_damage_modifier (orc_is_stunned):
    damage_modifier = 1 # assume no stun damage increase
    if orc_is_stunned: 
        print("The orc is stunned!")
        damage_modifier = 2    
    return damage_modifier

def get_damage_modifiers (orc_is_stunned):
    crit_damage_modifier = get_crit_damage_modifier()
    stun_damage_modifier = get_stun_damage_modifier(orc_is_stunned)
    return crit_damage_modifier * stun_damage_modifier

def healDamage(healAmount): #implemented for healing from inventory items/other
    global health
    health += healAmount

def updateGold(gainOrLoss, amount): #gainOrLoss is T/F, amount is amount modifie
    global gold
    if gainOrLoss:
        gold += amount
    else: 
        gold -= amount