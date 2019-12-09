import inventory as inv
import hero

FIREBOMB_PRICE = (100, 150, 200)
SMALL_HEALTHPOT_PRICE = (50, 75, 100)
HEALTHPOT_PRICE = (100, 200, 300)
IRONSKIN_PRICE = (100, 150, 200)

def configure_difficulty(difficultyLevel):
    global FIREBOMB_PRICE, SMALL_HEALTHPOT_PRICE, HEALTHPOT_PRICE, \
        IRONSKIN_PRICE
    FIREBOMB_PRICE = FIREBOMB_PRICE[difficultyLevel]
    SMALL_HEALTHPOT_PRICE = SMALL_HEALTHPOT_PRICE[difficultyLevel]
    HEALTHPOT_PRICE = HEALTHPOT_PRICE[difficultyLevel]
    IRONSKIN_PRICE = IRONSKIN_PRICE[difficultyLevel]

def displayShopIntro():
    print("You walked into the shoppe, the owner greets you.")
    print("\033[1;31mShop Owner: \n"
    "Welcome, traveller, to my humble shop!"
    "\033[0;0m")
    print("Please, browse my wares!")
    itemDisplay()

def itemDisplay():
    global FIREBOMB_PRICE, SMALL_HEALTHPOT_PRICE, HEALTHPOT_PRICE, \
        IRONSKIN_PRICE
    gold = hero.gold
    print(f"You have {gold} gp left")
    print(f"[1]Firebomb({FIREBOMB_PRICE} gp)\n"
    f"[2]Small Health Potion({SMALL_HEALTHPOT_PRICE} gp)\n"
    f"[3]Health Potion({HEALTHPOT_PRICE} gp)\n"
    f"[4]Ironskin Potion({IRONSKIN_PRICE} gp )\n"
    "[5]Item Info\n"
    "[6]Exit Shop")


    itemValue = int(input("Choose an Item To Buy: \n"))
    while itemValue not in [1, 2, 3, 4, 5, 6]:
        print(f"That is not a valid item.")
        itemValue = int(input("Choose an Item To Buy: \n"))
        print(f"You have {gold} gp left")
        print(f"[1]Firebomb({FIREBOMB_PRICE} gp)\n"
        f"[2]Small Health Potion({SMALL_HEALTHPOT_PRICE} gp)\n"
        f"[3]Health Potion({HEALTHPOT_PRICE} gp)\n"
        f"[4]Ironskin Potion({IRONSKIN_PRICE} gp )\n"
        "[5]Item Info\n"
        "[6]Exit Shop")
    
    if itemValue == 5:
        inv.describeItems()

        itemValue = int(input("Choose an Item To Buy: \n"))

        while itemValue not in [1, 2, 3, 4, 5, 6]:
            print(f"That is not a valid item.")
            itemValue = int(input("Choose an Item To Buy: \n"))

    if itemValue in [1, 2, 3, 4]:
        calcPrice(itemValue)
    


def calcPrice(itemValue):
    if itemValue == 1 and hero.gold >= FIREBOMB_PRICE:
        price = FIREBOMB_PRICE
        inv.FIREBOMBS += 1
        print("You bought a Firebomb")
        shoppe(price)
    elif itemValue == 2 and hero.gold >= SMALL_HEALTHPOT_PRICE:
        inv.SMALL_HEALTH_POTS += 1
        price = SMALL_HEALTHPOT_PRICE
        print("You bought a Small Health Potion")
        shoppe(price)
    elif itemValue == 3 and hero.gold >= HEALTHPOT_PRICE:
        inv.HEALTH_POTS += 1
        price = HEALTHPOT_PRICE
        print("You bought a Health Potion")
        shoppe(price)
    elif itemValue == 4 and hero.gold >= IRONSKIN_PRICE:
        inv.IRONSKIN_POTS += 1
        price = IRONSKIN_PRICE
        print("You bought an Ironskin Potion")
        shoppe(price)
    else:
        print("You do not have enough gold for that.")
        shoppe(0)

def shoppe(itemCost):

    hero.updateGold(False, itemCost)
    gold = hero.gold
    print(f"You have {gold} gp left")
    print("[1]Continue Shopping\n[2]Leave")
    again = int(input("Would you like to keep shopping?\n"))
    while again not in [1, 2]:
        print("Invalid Input, try again.")
        again = int(input("Would you like to keep shopping?\n"))
    if again == 1:
        itemDisplay()