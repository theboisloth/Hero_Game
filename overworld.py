import game
import hero
import inventory
import orc
import os
import random
import saveGame

current_coords = [0,0]
the_end = False
def movement(current_coords, action):
    accepted_input = False
    while accepted_input == False:
        move_command = action
        if move_command == "n":
            if current_coords [1] == 2:
                accepted_input = False
                print ("You can't go any further this way")
            else:
                current_coords[1]= current_coords[1] + 1
                accepted_input = True
        elif move_command == "s":
            if current_coords [1] == -2:
                accepted_input = False
                print ("You can't go any further this way")
            else:
                current_coords[1]= current_coords[1] - 1
                accepted_input = True
        elif move_command == "w":
            if current_coords [0] == -2:
                accepted_input = False
                print ("You can't go any further this way")
            else:
                current_coords[0]= current_coords[0] - 1
                accepted_input = True
        elif move_command == "e":
            if current_coords [0] == 2:
                accepted_input = False
                print ("You can't go any further this way")
            else:
                current_coords[0]= current_coords[0] + 1
                accepted_input = True
        elif move_command == "help":
            print ("n for north, s for south, w for west, e for east")
            accepted_input = False
        if accepted_input == True:
            overworld_flavor_text (current_coords)
        else:
            print ("Invalid input")
        print ("Your new position is: ", current_coords)
        return current_coords

def random_encounter (current_coords):
    encounter_chance = random.randint (0, 100)
    x = current_coords [0]
    y = current_coords [1]
    if x >= 1 and y >= 1: #NE
        if encounter_chance > 65 and encounter_chance < 85: #secondary enemy for NE, wolf
            enemy = "wolf"
            print ("NE")
            pass
        elif encounter_chance > 85: #primary enemy for north, spider
            enemy = "spider"
            print ("NE")
            pass
        else:
            enemy = "none"
            print ("NE")
            pass
    elif x <= -1 and y >= 1: #NW
        if encounter_chance > 65 and encounter_chance < 85: # secondary enemy for NW, witch
            enemy = "witch"
            print ("NW")
            pass
        elif encounter_chance > 85: #primary enemy for north, spider
            enemy = "spider"
            print ("NW")
            pass
        else:
            enemy = "none"
            print ("NW")
    elif y >= 1: # straight north
        if encounter_chance > 85:
            enemy = "spider"
            print ("N")
        else:
            enemy = "none"
            print ("N")
    elif  y <= -1 and x >= 1: # SE
        if encounter_chance > 65 and encounter_chance < 85: #secondary enemy for SE, wolf
            enemy = "wolf"
            print ("SE")
        elif encounter_chance > 85: #primary enemy for south, Ooze
            enemy = "ooze"
            print ("SE")
        else:
            enemy = "none"
            print ("SE")
    elif x >= 1: #straight east
        if encounter_chance > 85: # east is secondary direction, only enemy is wolf on direct path east.
            enemy = "wolf"
            print ("E")
        else:
            enemy = "none"
            print ("E")
    elif y <= -1 and x <= -1: #SW
        if encounter_chance > 65 and encounter_chance < 85: #secondary enemy for SW, witch
            enemy = "witch"
            print ("SW")
        elif encounter_chance > 85:
            enemy = "ooze"
            print ("SW")
        else:
            enemy = "none"
            print ("SW")
    elif x <= -1: #straight west
        if encounter_chance < 85:
            enemy = "witch"
            print ("W")
        else:
            enemy = "none"
            print ("W")
    elif y <= -1: #straight south
        if encounter_chance > 85: #
            enemy = "ooze"
            print ("S")
        else:
            enemy = "none"
            print ("S")
    elif y == 0 and x == 0:
        enemy = "none"
    return enemy

def overworld_flavor_text(current_coords):
    if current_coords == [0,0]:
        print ("Its safer here than elsewhere, but you can't just sit around forever")
    elif current_coords == [-1,0]:
        print ("something")
    elif current_coords == [0,-1 ]:
        print ("something")
    elif current_coords == [0,0]:   
        print ("something")
    elif current_coords == [0,0]:
        print ("something")
    elif current_coords == [0,0]:
        print ("something")
    elif current_coords == [0,0]:
        print ("something")
    elif current_coords == [0,0]:
        print ("something")
    elif current_coords == [0,0]:
        print ("something")
    elif current_coords == [0,0]:
        print ("something")
#for testing code
# while the_end == False:
#      current_coords = movement(current_coords)
#      print (current_coords)
title = """
\033[0;31m
 ██░ ██ ▓█████  ██▀███   ▒█████       ██████  ██▓    ▄▄▄     ▓██   ██▓▓█████  ██▀███  
▓██░ ██▒▓█   ▀ ▓██ ▒ ██▒▒██▒  ██▒   ▒██    ▒ ▓██▒   ▒████▄    ▒██  ██▒▓█   ▀ ▓██ ▒ ██▒
▒██▀▀██░▒███   ▓██ ░▄█ ▒▒██░  ██▒   ░ ▓██▄   ▒██░   ▒██  ▀█▄   ▒██ ██░▒███   ▓██ ░▄█ ▒
░▓█ ░██ ▒▓█  ▄ ▒██▀▀█▄  ▒██   ██░     ▒   ██▒▒██░   ░██▄▄▄▄██  ░ ▐██▓░▒▓█  ▄ ▒██▀▀█▄  
░▓█▒░██▓░▒████▒░██▓ ▒██▒░ ████▓▒░   ▒██████▒▒░██████▒▓█   ▓██▒ ░ ██▒▓░░▒████▒░██▓ ▒██▒
 ▒ ░░▒░▒░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░▒░▒░    ▒ ▒▓▒ ▒ ░░ ▒░▓  ░▒▒   ▓▒█░  ██▒▒▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░▒░ ░ ░ ░  ░  ░▒ ░ ▒░  ░ ▒ ▒░    ░ ░▒  ░ ░░ ░ ▒  ░ ▒   ▒▒ ░▓██ ░▒░  ░ ░  ░  ░▒ ░ ▒░
 ░  ░░ ░   ░     ░░   ░ ░ ░ ░ ▒     ░  ░  ░    ░ ░    ░   ▒   ▒ ▒ ░░     ░     ░░   ░ 
 ░  ░  ░   ░  ░   ░         ░ ░           ░      ░  ░     ░  ░░ ░        ░  ░   ░     
                                                              ░ ░                 
\033[0m                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
"""
def start():
    print (title)
    get_difficulty()
    current_coords = [0,0]
    global enemy
    enemy = False

    while the_end == False:
        main(current_coords)


def permanent_encounters(current_coords):
    if current_coords[0] == 0 and current_coords[1] == -1:
        #orc
        print ("broken orc encounter")
        unique_encounter = "orc"
        pass
    elif current_coords [0] == -3 and current_coords [1] == -3:
        #orc
        unique_encounter = "orc"
        print ("broken orc encounter")
        pass 
    elif current_coords [0] == 4 and current_coords [1] == 3:
        unique_encounter = "shop"
        print ("broken shop encounter")
    else:
        unique_encounter = "none"
    return unique_encounter


def main(current_coords):
    global saved_coords
    saved_coords = current_coords
    action = input ("Enter what you want to do (help for commands): ")
    if action == "help":
        print ("Input uses no capital letters. n, e, s, and w are used to move in cardinal directions")
    elif action == "n" or action == "s" or action == "e" or action == "w":
        movement(current_coords, action)
    elif action == "save":
        saveGame.save_game_state()
    else:
        print ("Unaccepted input.")
    unique_encounter = permanent_encounters(current_coords)
    if unique_encounter == "none":
        enemy = random_encounter(current_coords)
        if enemy != "none":
            combat = True
        elif enemy == "none":
            combat = False
        if combat == True:
            print ("IT WORKED") #ADD CODE TO START FIGHT

def get_difficulty ():
    print("[1] Easy")
    print("[2] Normal")
    print("[3] Impossible")
    print("[4] Load game")
    difficulty = int(input("Choose your difficulty level: "))

    if difficulty not in (1, 2, 3, 4):
        print("Invalid option: You're playing impossible mode!")
        difficulty = 3
    if difficulty < 4:
        difficulty -= 1
        global difficulty_level
        difficulty_level = difficulty
        hero.configure_difficulty(difficulty)
        orc.configure_difficulty(difficulty)
        inventory.configure_difficulty(difficulty)
    else:
        (saveGame.load_game_state())

start()