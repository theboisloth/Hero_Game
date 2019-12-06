import random
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
            combat = True
            print ("NE")
            pass
        else:
            enemy = "none"
            print ("NE")
            pass
    elif x <= -1 and y >= 1: #NW
        if encounter_chance > 65 and encounter_chance < 85: # secondary enemy for NW, witch
            enemy = "witch"
            combat = True
            print ("NW")
            pass
        elif encounter_chance > 85: #primary enemy for north, spider
            enemy = "spider"
            combat = True
            print ("NW")
            pass
        else:
            enemy = "none"
            print ("NW")
    elif y >= 1: # straight north
        if encounter_chance > 85:
            enemy = "spider"
            combat = True
            print ("N")
        else:
            enemy = "none"
            combat = True
            print ("N")
    elif  y <= -1 and x >= 1: # SE
        if encounter_chance > 65 and encounter_chance < 85: #secondary enemy for SE, wolf
            enemy = "wolf"
            combat =  True
            print ("SE")
        elif encounter_chance > 85: #primary enemy for south, Ooze
            enemy = "ooze"
            combat = True
            print ("SE")
        else:
            enemy = "none"
            print ("SE")
    elif x >= 1: #straight east
        if encounter_chance > 85: # east is secondary direction, only enemy is wolf on direct path east.
            enemy = "wolf"
            combat = True
            print ("E")
        else:
            enemy = "none"
            print ("E")
    elif y <= -1 and x <= -1: #SW
        if encounter_chance > 65 and encounter_chance < 85: #secondary enemy for SW, witch
            enemy = "witch"
            combat = True
            print ("SW")
        elif encounter_chance > 85:
            enemy = "ooze"
            combat = True
            print ("SW")
        else:
            enemy = "none"
            print ("SW")
    elif x <= -1: #straight west
        if encounter_chance < 85:
            enemy = "witch"
            combat = True
            print ("W")
        else:
            enemy = "none"
            print ("W")
    elif y <= -1: #straight south
        if encounter_chance > 85: #
            enemy = "ooze"
            combat = True
            print ("S")
        else:
            enemy = "none"
            print ("S")
    elif y == 0 and x == 0:
        enemy = "none"
        print ("Its safer here than elsewhere, but you can't just sit around")
    return enemy

current_coords = [0, -1]
enemy = random_encounter(current_coords)
print (enemy)

    