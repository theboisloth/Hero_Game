import hero
import inventory
import orc
import os
import random
import saveGame
import fight
import shop
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
        if encounter_chance > 75 and encounter_chance < 85: #secondary enemy for NE, wolf
            enemy = "Wolf"
            print ("NE")
            pass
        elif encounter_chance > 85: #primary enemy for north, spider
            enemy = "Spider"
            print ("NE")
            pass
        else:
            enemy = "none"
            print ("NE")
            pass
    elif x <= -1 and y >= 1: #NW
        if encounter_chance > 65 and encounter_chance < 85: # secondary enemy for NW, witch
            enemy = "Witch"
            print ("NW")
            pass
        elif encounter_chance > 85: #primary enemy for north, spider
            enemy = "Spider"
            print ("NW")
            pass
        else:
            enemy = "none"
            print ("NW")
    elif y >= 1: # straight north
        if encounter_chance > 85:
            enemy = "Spider"
            print ("N")
        else:
            enemy = "none"
            print ("N")
    elif  y <= -1 and x >= 1: # SE
        if encounter_chance > 75 and encounter_chance < 85: #secondary enemy for SE, wolf
            enemy = "wolf"
            print ("SE")
        elif encounter_chance > 85: #primary enemy for south, slime
            enemy = "Slime"
            print ("SE")
        else:
            enemy = "none"
            print ("SE")
    elif x >= 1: #straight east
        if encounter_chance > 75: # east is secondary direction, only enemy is wolf on direct path east.
            enemy = "Wolf"
            print ("E")
        else:
            enemy = "none"
            print ("E")
    elif y <= -1 and x <= -1: #SW
        if encounter_chance > 65 and encounter_chance < 85: #secondary enemy for SW, witch
            enemy = "witch"
            print ("SW")
        elif encounter_chance > 85:
            enemy = "slime"
            print ("SW")
        else:
            enemy = "none"
            print ("SW")
    elif x <= -1: #straight west
        if encounter_chance < 85:
            enemy = "Witch"
            print ("W")
        else:
            enemy = "none"
            print ("W")
    elif y <= -1: #straight south
        if encounter_chance > 85: #
            enemy = "slime"
            print ("S")
        else:
            enemy = "none"
            print ("S")
    elif y == 0 and x == 0:
        enemy = "none"
    return enemy

def overworld_flavor_text(current_coords):
    if current_coords == [0,0]:
        print ("Its safe here... but you can't just sit around forever")
    ####################################### east
    elif current_coords == [1, 0]:
        print ("The path leads east through a calm forest. The cobbles are ill maintained, but still fully functional.")
        print ("The further you follow the path, the more apparent ")
    elif current_coords == [2, 0]:
        print ("Theres an orcish camp ahead of you contaminating the otherwise pristine forest with a poorly constructed palisade.")
        print ("An orc guard patrolling the area spots you and rushes.")
    elif current_coords == [1, 1]:
        print ("The trunks of trees are beginning to look as if they were made of silk instead of bark, a thick layer of cobwebs covers the area and makes movement difficult.")
    elif current_coords == [2, 1]:
        print ("The forest grows thinner here, a cliff on the east side stretches as far north as the eye can see.")
        print ("In the distance you can see a rainbow crossing over a stream and a village nearby, but you can't go back yet.")
    elif current_coords == [2, 2]:
        print ("A lone shack stands, with a sign that has 'WARES' written sloppily on a slanted massive board.")
        print ("A madman lives inside, but he's still more friendly than the rest of the forests inhabitants.")
        print ("You enter and he offers to trade, maybe those coins you collected have a use after all.")
    elif current_coords == [0, 2]:
        print ("The forest is silent, except for the scittering spiders and howls of wolves.")
        print ("You don't dare head any further north, the spiders here only get larger.")
    elif current_coords == [0, 1]:
        print ("The path heads north then ends abruptly. apparently man never made it here even before the war.")
        print ("You can see why ahead, the thick cobwebs engulf every surface available to them.")
    elif current_coords == [-1, 1]:
        print ("The forest is dark and caked with cobwebs, you're navigating mostly by touch at this point due to the overcast and cobweb canopy above you.")
    elif current_coords == [-2, 1]:
        print ("The cobwebs are thick here, which is better than before")
    elif current_coords == [-2, 2]:
        print ("This is the wrong way. You've heard tales about the innerlands, not many claim to return from there, and none who claimed they would return have.")
    ####################################### south
    elif current_coords == [0,-1]: #orc camp
        print ("You push through the light brush towards a clearing. The air has a metallic property to it")
        print ("You push through the woods loudly, exiting the forest and entering a sickening scene.")
        print ("There is a camp ahead of you, featuring decorations such as spikes adorned with heads of your fellow man")
        print ("The camp has a barbaric property to it, poorly cleaned and cured animal skin tents, simple and horrifying weaponry strewn about.")
        print ("Not even the grass dares approach the camp site, a lush forest turns into a green clearing, and ends in cracked earth, ruining an otherwise picturesque setting")
        print ("The most gut wrenching site of all however; an orc with a sack over its shoulder, likely returning to camp, has spotted you.")
        print ("The sack was likely filled with morsels. Maybe you'll make a nice addition?")
    elif current_coords == [0, -2]:
        print ("The marsh ahead of you is an impressive site, to the south mangroves form a shield, keeping you away from the swamp and the swamp away from you. Good riddance.")
    elif current_coords == [1, -2]:
        print ("The swamp seems to radiate a sickly heat, further aiding to the feeling of nausea brought on by the stench.")
    elif current_coords == [2, -2]:
        print ("The further you go the less welcome you feel, craters in the ground bubble and fester with green sludge")
        print ("The smell from the rest of the swamp was a poor imitation of the absolute vile odor emitted from the pools")
    elif current_coords == [1, -1]:
        print ("There are chanting sounds coming from the west, it is certainly a bad idea to go towards them.")
        print ("The forest here is healthy, with an abundance of game ")
    elif current_coords == [0, -2]:
        print ("The forest has taken as much land as it can here, stretching down to the edges of the swamp.")
        print ("Even the men who resemble beasts seem to fear the swamp, as they only venture to the edge to dispose of their victims.")
        print ("The rotting corpses are piled to waist height, some in advanced stages of decay, and some appearing to have been mangled recently.")
    elif current_coords == [2, -1]:
        print ("The swamp lays south of you. You should probably follow the forest's lead and not approach.")
    ################################# west
    elif current_coords == [-1,0]:
        print ("The forest looks haunting here, you hear a cackle that seems to come from the trees. Theres a lot of trees.")
        print ("The path cuts through the forest, but the overgrowth provides cover on both sides.")
        print ("Someone could be very near and you wouldn't know until you were right on top of them.")
    elif current_coords == [-1,1]:
        print ("The forest looks haunting here, you hear a cackle that seems to come from the trees.")
        print ("Theres runes on the trees, not like scratchings, just indents in the wood. No tool could've made these markings")
    elif current_coords == [-1,2]:
        print ("The trees here are withering, a few have fallen. Stumps uprooted, not as if knocked over, but almost like the tree let go of the earth beneath it")
        print ("North of you the forest forms an impenetrable wall. Probably to keep you in this foresaken place.")
    elif current_coords == [-2,0]:
        print ("The path continues westward through more of the endless haunted forest. There is no end in sight.")
        print ("Even though leaving would be so simple, there are still ends loose.")
    elif current_coords == [-1,-1]:
        print ("The ground isn't like the rest of this place, the entire forest is covered in detritus.")
        print ("It seems like the shrubbery was dead when it grew, something evil lurks here.")
    elif current_coords == [-1,-2]:
        print ("The trees become more sparse and the ground is increasingly muddy. The earth turns to mud and further advancement is nearly halted")
        print ("The water smells putrid, and plants are nearingly void, meaning the water is likely brackish. In the east a thick forest lies")
    elif current_coords == [-2,-1]:
        print ("The source of the cackling is apparent ahead of you.")
        print ("A clearing in the forest reveals a house. You can't see it well, but thats probably for the best.")
        print ("The trees until now formed a spare barrier concealing view, but noticeably thin nearer to the house.")
        print ("You assumed the cobweb canopy above was blocking the light, but without any trees how could this be possible?")
        print ("A twig snaps behind you.")
    elif current_coords == [-2,-2]:
        print ("The elevation drops further gradually. The scent of salt fills the air, and brings back fond memories.")
        print ("The roar of the ocean waves certifies your suspicions, you've reached the ocean, not even the dark powers so near can corrupt such a magnificent sight.")
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
        unique_encounter = "orc"
        pass
    elif current_coords [0] == 2 and current_coords [1] == 0:
        #orc
        unique_encounter = "orc"
        print ("broken orc encounter")
        pass
    elif current_coords [0] == 2 and current_coords [1] == 2:
        unique_encounter = "shop"
        print ("You can now use 'shop'")
    else:
        unique_encounter = "none"
    return unique_encounter

def main(current_coords):
    global saved_coords
    saved_coords = current_coords
    action = input ("Enter what you want to do (help for commands): ")
    if action == "help":
        print ("Input uses no capital letters. n, e, s, and w are used to move in cardinal directions, 'gold' checks gold")
    elif action == "n" or action == "s" or action == "e" or action == "w":
        movement(current_coords, action)
    elif action == "gold":
        pass
    elif action == "shop" and current_coords [0] == 2 and current_coords [1] == 2:
        shop.configure_difficulty(difficulty_level)
        shop.displayShopIntro()
    elif action == "save":
        saveGame.save_game_state(saved_coords)
    else:
        print ("Unaccepted input.")
    unique_encounter = permanent_encounters(current_coords)
    if unique_encounter == "none" or unique_encounter == "orc":
        enemy = random_encounter(current_coords)
        if enemy != "none":
            combat = True
        elif enemy == "none":
            combat = False
        if combat == True:
            print (enemy) #ADD CODE TO START FIGHT
        if enemy == "Wolf":
            enemy = 1
            print ("indeed")
        elif enemy == "Slime":
            enemy = 2
            print ("indeed")
        elif enemy == "Spider":
            enemy = 3
            print ("indeed")
        elif enemy == "Witch":
            enemy = 4
            print ("indeed")
        if unique_encounter == "orc":
            enemy = 5
            print ("indeed")
        if enemy == 1 or enemy == 2 or enemy == 3 or enemy == 4 or enemy == 5:
            fight.configure_difficulty(difficulty_level)
            fight.fight(enemy, difficulty_level)
        

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
        go_to(saveGame.load_game_state())

def go_to(saved_coords):
    global current_coords
    current_coords = saved_coords


start()