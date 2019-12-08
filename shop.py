import inventory as inv

def configure_difficulty(difficultyLevel):
    pass

def displayShopIntro():
    print("You walked into the shoppe, the owner greets you.")
    print("\033[1;31mShop Owner: \n"
    "Welcome, traveller, to my humble shop!"
    "\033[0;0m")
    print("Please, browse my wares!")

    global FIREBOMBS, SMALL_HEALTH_POTS, HEALTH_POTS, IRONSKIN_POTS
    print(f"[1]Firebomb(x{FIREBOMBS})\n"
    "[2]Small Health Potion(x{SMALL_HEALTH_POTS})\n"
    "[3]Health Potion(x{HEALTH_POTS})\n"
    "[4]Ironskin Potion(x{IRONSKIN_POTS})\n"
    "[5]Item Info")
    shoppe(1)


def shoppe(itemValue):
    pass



displayShopIntro()