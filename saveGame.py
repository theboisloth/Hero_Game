import inventory, hero, orc#, overworld
import os.path
#New File, needed to save ALL of the data
#Works with files imported so far.
def save_game_state(coords): #If used after difficulty configuration, working
    saveFile = open(f"saveGame.csv", "w")
    saveFile.write(str(hero.health) + ',')
    inventoryState = str(inventory.get_save_data())
    i = 0
    while i < len(inventoryState):
        saveFile.write(inventoryState[i])
        i += 1

    saveFile.write(str(f","))
    saveFile.write(str(f"{coords[0]},"))
    saveFile.write(str(f"{coords[1]}"))


    saveFile.close()

def load_game_state():
    loadFile = open(f"saveGame.csv", "r")
    loadData = loadFile.readline().split(",")
    
    print(loadData)
    global lastPlace
    lastPlace = loadData[11].strip("]\n")
    hero.health = int(loadData[0])
    inventoryState = int(loadData[1].strip("[")), int(loadData[2]), \
    int(loadData[3]), int(loadData[4]), int(loadData[5]), int(loadData[6]), \
    int(loadData[7]), float(loadData[8]), int(loadData[9]), int(loadData[10]),\
    int(lastPlace)
    saved_coords = [int(loadData[12]), int(loadData[13])]

    inventory.load_save_data(inventoryState)
    return saved_coords