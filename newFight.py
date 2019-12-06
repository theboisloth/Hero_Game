#Fight code made from scratch
#This starts the fight, takes enemy type
#Cannnot save while in combat
import hero, orc, inventory, overworld, saveGame#, wolf, spider, witch, slime
import random

rounds_poisoned = 0
rounds_stunned = 0

def fight(enemyType): #Takes enemy encountered
    if enemyType == "Wolf": #Checks enemy type
        enemyType = 1
    if enemyType == "Spider":
        enemyType = 2
    if enemyType == "Slime":
        enemyType = 3
    if enemyType == "Witch":
        enemyType = 4
    if enemyType == "Orc":
        enemyType = 5
    
    while not fight_is_over(enemyType): #Before Implementation, need enemy files
        pass 

def enemy_turn_logic(rounds_poisoned, rounds_stunned, enemyType): 
    #Not Implemented, need enemy files and status effects.
    
    if enemyType == 1: #Checks enemy type
        pass
    if enemyType == 2:
        pass
    if enemyType == 3:
        pass
    if enemyType == 4:
        pass
    if enemyType == 5:
        pass

#Determines if either the enemy or the hero has died in combat.
def fight_is_over(enemyType): 
    if enemyType == 1:
        enemyHealth = 5
    
    elif enemyType == 2:
        enemyHealth = 5
        
    elif enemyType == 3:
        enemyHealth = 5

    elif enemyType == 4:
        enemyHealth = 5
    
    elif enemyType == 5:
        enemyHealth = orc.health

    return (hero.health <= 0 or enemyHealth <= 0)