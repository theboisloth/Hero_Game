import hero, orc, inventory, saveGame
# import overworld 
import os.path, random

difficulty_level = 1
rounds_poisoned = 0
rounds_stunned = 0
STUN_RATE = 10
save_and_quit = False

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

def game ():
    print(title)
    get_difficulty()
    global rounds_poisoned, rounds_stunned
    round = 1
    while not game_is_over():
        print(f"\n{'+'*100}{'Round '+str(round):^21}{'+'*100}")
        # Orc's Turn
        rounds_poisoned = orc_turn_logic(rounds_poisoned, rounds_stunned)
        if orc.health < 10:
            damage = orc.frenzy()
            hero.deal_damage(damage)

        # Hero's Turn
        if hero.health > 0:
            hero_attack_damage, did_kick, quit_game, usedItem = hero.attack(rounds_poisoned > 0, rounds_stunned > 0)
            if quit_game:
                global save_and_quit
                save_and_quit = True
                # break
            else: 
                if rounds_stunned > 0:
                    rounds_stunned -= 1
                if did_kick:
                    rounds_stunned = stun_logic(rounds_stunned)
                if hero_attack_damage > 0:
                    orc.deal_damage(hero_attack_damage)
                
                if hero_attack_damage == 0 and usedItem: #Implements from inventory
                    pass #Using an item does NOT mean you missed, skip the message
                
                if hero_attack_damage == 0 and not usedItem:
                    print("You missed")

        # Deal poison damage
        if rounds_poisoned > 0:
            rounds_poisoned -= 1
            deal_poison_damage()

        display_health()
        round += 1

    if save_and_quit:
        save()
    else: 
        # Check who died
        if hero.health <= 0:
            print("The hero died")
        if orc.health <= 0:
            print("The orc died")

def game_is_over ():
    return (hero.health <= 0 or orc.health <= 0) or save_and_quit

def orc_turn_logic (rounds_poisoned, rounds_stunned):
    orc_attack_damage, did_poison = orc.attack(rounds_stunned > 0)
    if orc_attack_damage > 0:
        hero.deal_damage(orc_attack_damage)
        if did_poison:
            rounds_poisoned = random.randint(2, 5)
    else:
        print("The orc missed")
    
    return rounds_poisoned

def deal_poison_damage ():
    poison_damage = random.randint(2, 4)
    print(f"You took {poison_damage} damage from poison.")
    hero.deal_damage(poison_damage)

def stun_logic (rounds_stunned):
    if rounds_stunned <= 0:
        stun_roll = random.randint(1, 100)
        if stun_roll <= STUN_RATE:
            print("You stunned the orc!")
            rounds_stunned = random.randint(1, 2)
    return rounds_stunned

def display_health ():
    print(f"You have {hero.health} health remaining")
    print(f"The orc has {orc.health} health remaining")

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
        
        
        saveGame.save_game_state() #Testing Purposes

    else:
        load()

def save ():
    save_file = open("save_game.csv", "w")
    save_file.write(str(hero.health) + ',')
    save_file.write(str(orc.health) + ',')
    save_file.write(str(difficulty_level) + ',')
    save_file.write(str(rounds_poisoned) + ',')
    save_file.write(str(rounds_stunned) + '\n')
    save_file.close()

def load ():
    global difficulty_level, rounds_poisoned, rounds_stunned
    if os.path.isfile("save_game.csv"):
        save_file = open("save_game.csv", "r")
        params = save_file.readline().strip().split(',')

        hero.health, orc.health, difficulty_level, rounds_poisoned, rounds_stunned = params
        hero.configure_difficulty(difficulty_level)
        orc.configure_difficulty(difficulty_level)
        save_file.close()
    else:
        hero.configure_difficulty(2)
        orc.configure_difficulty(2)
        inventory.configure_difficulty(2) #Implemented for inventory

game()