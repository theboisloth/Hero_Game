#Fight code made from scratch
#This starts the fight, takes enemy type
#Cannnot save while in combat
import hero, orc, saveGame, wolf, slime, spider, witch
import inventory as inv
import random
import sys

rounds_poisoned = 0
rounds_stunned = 0
STUN_RATE = 10
rounds_bled = 0

def fight(enemyType, difficultyLevel): #Takes enemy encountered
    round = 1
    configure_difficulty(difficultyLevel)
    battleEntry(enemyType)
    
    if enemyType == 1: 
        enemy = "Wolf"
    elif enemyType == 2:
        enemy = "Slime"
    
    elif enemyType == 3:
        enemy = "Spider"
    
    elif enemyType == 4:
        enemy = "Witch"
    
    elif enemyType == 5:
        enemy = "Orc"

    
    while not fight_is_over(enemyType): #Before Implementation, need enemy files
        
        print(f"\n{'+'*100}{'Round '+str(round):^21}{'+'*100}")
        
        #Hero Goes First
        if hero.health > 0:
            global rounds_poisoned, rounds_bled, rounds_stunned
            hero_attack_damage, did_kick, quit_game, usedItem = hero.attack(rounds_poisoned > 0, rounds_stunned > 0, rounds_bled > 0, enemyType)
 
            if rounds_stunned > 0:
                rounds_stunned -= 1

            if did_kick:
                rounds_stunned = stun_logic(rounds_stunned, enemy)
            
            if hero_attack_damage > 0:#Check enemy type and damage them
                
                if enemyType == 1: 
                    wolf.deal_damage(hero_attack_damage)

                elif enemyType == 2:
                    slime.deal_damage(hero_attack_damage)
                
                elif enemyType == 3:
                    spider.deal_damage(hero_attack_damage)
                
                elif enemyType == 4:
                    witch.deal_damage(hero_attack_damage)
                
                elif enemyType == 5:
                    orc.deal_damage(hero_attack_damage)
            
            if hero_attack_damage == 0 and usedItem: #Implements from inventory
                pass #Using an item does NOT mean you missed, skip the message
            
            if hero_attack_damage == 0 and not usedItem:
                print("You missed")
        #End of Hero Attack Phase

        #Enemy Attack Phase
        rounds_poisoned, rounds_bled = enemy_turn_logic(rounds_poisoned, rounds_stunned, rounds_bled, enemyType)
        if orc.health < 10:
            damage = orc.frenzy()
            hero.deal_damage(damage)
        #End of Enemy Attack Phase

        if rounds_poisoned > 0:
            rounds_poisoned -= 1
            dealPoisonDamage()
        if rounds_bled > 0:
            rounds_bled -= 1
            dealBleedDamage()
        display_health(enemyType)
        round += 1
    
    #End of Fight
    if hero.health <= 0:
        print("The Hero has fallen.")
        terminate()
    
    if getEnemyHealth(enemyType) <= 0:
        print(f"The {enemy} died.")
        hero.updateGold(True, random.randint(20, 50))


def terminate():
    exit()

def battleEntry(enemyType):
    if enemyType == 1:
        print("You Encountered a Wolf!")
    elif enemyType == 2:
        print("You Encountered a Slime!")
    elif enemyType == 3:
        print("You Encountered a Spider!")
    elif enemyType == 4:
        print("You Encountered a Witch!")
    elif enemyType == 5:
        print("You Encountered the Orc...")

def enemy_turn_logic(rounds_poisoned, rounds_stunned, rounds_bled, enemyType): 
    damage = 0
    
    if enemyType == 1: #Checks enemy type
        damage, didBleed = wolf.attack(rounds_stunned > 0)
        if damage > 0 and didBleed and rounds_stunned == 0:
            hero.deal_damage(damage)
            rounds_bled = random.randint(1, 6)
            print("The attack caused you to bleed!")
        elif damage > 0 and not didBleed and rounds_stunned == 0:
            hero.deal_damage(damage)
        elif rounds_stunned == 0:
            print("The Wolf Missed!")
        elif rounds_stunned != 0:
            print("The Wolf is Stunned!")


    elif enemyType == 2:
        damage = slime.attack(rounds_stunned > 0)
        if damage > 0 and rounds_stunned == 0:
            hero.deal_damage(damage)
        elif rounds_stunned == 0:
            print("The Slime Missed!")
        elif rounds_stunned != 0:
            print("The Slime is Stunned!")


    elif enemyType == 3:
        damage, did_poison = spider.attack(rounds_stunned > 0)
        if damage > 0 and rounds_stunned == 0:
            hero.deal_damage(damage)
        elif rounds_stunned == 0:
            print("The Spider Missed!")
        elif rounds_stunned != 0:
            print("The Spider is Stunned!")
        if did_poison:
            rounds_poisoned = random.randint(2, 5)

    elif enemyType == 4:
        damage, did_poison, didHeal = witch.attack(rounds_stunned > 0)
        if damage > 0 and rounds_stunned == 0:
            hero.deal_damage(damage)
        elif rounds_stunned == 0 and not didHeal:
            print("The witch Missed!")
        elif rounds_stunned != 0:
            print("The Witch is Stunned!")
        if did_poison:
            rounds_poisoned = random.randint(2, 5)
        


    elif enemyType == 5:
        orc_attack_damage, did_poison = orc.attack(rounds_stunned > 0)
        
        if orc_attack_damage > 0:
            hero.deal_damage(orc_attack_damage)
        
        if did_poison:
            rounds_poisoned = random.randint(2, 5)
        
        else:
            print("The orc missed")

    return rounds_poisoned, rounds_bled


def dealPoisonDamage():
    poison_damage = random.randint(2, 4)
    hero.deal_damage(poison_damage)
    print(f"You took {poison_damage} damage from poison.")

def dealBleedDamage():
    bleedDamage = random.randint(5, 10)
    hero.deal_damage(bleedDamage)
    print(f"You took {bleedDamage} damage from severe bleeding.")

def stun_logic (rounds_stunned, enemy):
    if rounds_stunned <= 0:
        stun_roll = random.randint(1, 100)
        if stun_roll <= STUN_RATE:
            print(f"You stunned the {enemy}!")
            rounds_stunned = random.randint(1, 2)
    return rounds_stunned

def display_health (enemyType):
    print(f"You have {hero.health} health remaining")
    print(f"The enemy has {getEnemyHealth(enemyType)} health left")

def getEnemyHealth(enemyType):
    if enemyType == 1:
        enemyHealth = wolf.health
    
    elif enemyType == 2:
        enemyHealth = slime.health


    elif enemyType == 3:
        enemyHealth = spider.health

    elif enemyType == 4: #Not implemented yet
        enemyHealth = witch.health
    

    elif enemyType == 5:
        enemyHealth = orc.health
    
    return enemyHealth

def configure_difficulty(difficultyLevel):
    hero.configure_difficulty(difficultyLevel)
    wolf.configure_difficulty(difficultyLevel)
    slime.configure_difficulty(difficultyLevel)
    spider.configure_difficulty(difficultyLevel)
    witch.configure_difficulty(difficultyLevel)
    orc.configure_difficulty(difficultyLevel)

#Determines if either the enemy or the hero has died in combat.
def fight_is_over(enemyType):
    return (hero.health <= 0 or getEnemyHealth(enemyType) <= 0)
