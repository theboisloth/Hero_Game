import random

# Set initial damage ranges
BITE_DAMAGE_RANGE = ((1, 10), (5, 15), (15, 30))
SLASH_DAMAGE_RANGE = ((5, 20), (8, 25), (12, 35))
FRENZY_DAMAGE_RANGE = ((5, 10), (10, 30), (20, 40))
# Set critical hit rates
BIND_CRITICAL_RATES = (10, 30, 50)

# Set hit rates
FRENZY_HIT_RATES = (20, 40, 55)
MACHETE_HIT_RATES = (85, 92, 95)
BIND_HIT_RATES = (50, 70, 80)

POISON_RATES = (10, 20, 35)

HEALTH_RANGE = (1000, 1250, 1750)

# Init to normal mode
BITE_DAMAGE_LO, BITE_DAMAGE_HI = BITE_DAMAGE_RANGE[1]
SLASH_DAMAGE_LO, SLASH_DAMAGE_HI = SLASH_DAMAGE_RANGE[1]
FRENZY_DAMAGE_LO, FRENZY_DAMAGE_HI = FRENZY_DAMAGE_RANGE[1]
BIND_CRITICAL_RATE = BIND_CRITICAL_RATES[1]

FRENZY_HIT_RATE = FRENZY_HIT_RATES[1]
MACHETE_HIT_RATE = MACHETE_HIT_RATES[1]
BIND_HIT_RATE = BIND_HIT_RATES[1]
POISON_RATE = POISON_RATES[1]
health = HEALTH_RANGE[1]

def configure_difficulty (difficulty_level):
    global  BITE_DAMAGE_LO, BITE_DAMAGE_HI, SLASH_DAMAGE_LO, SLASH_DAMAGE_HI, \
            FRENZY_DAMAGE_LO, FRENZY_DAMAGE_HI, BIND_CRITICAL_RATE,           \
            FRENZY_HIT_RATE, MACHETE_HIT_RATE, BIND_HIT_RATE, POISON_RATE, \
            health
    BITE_DAMAGE_LO, BITE_DAMAGE_HI = BITE_DAMAGE_RANGE[difficulty_level]
    SLASH_DAMAGE_LO, SLASH_DAMAGE_HI = SLASH_DAMAGE_RANGE[difficulty_level]
    FRENZY_DAMAGE_LO, FRENZY_DAMAGE_HI = FRENZY_DAMAGE_RANGE[difficulty_level]
    BIND_CRITICAL_RATE = BIND_CRITICAL_RATES[difficulty_level]

    FRENZY_HIT_RATE = FRENZY_HIT_RATES[difficulty_level]
    MACHETE_HIT_RATE = MACHETE_HIT_RATES[difficulty_level]
    BIND_HIT_RATE = BIND_HIT_RATES[difficulty_level]
    POISON_RATE = POISON_RATES[difficulty_level]
    health = HEALTH_RANGE[difficulty_level]

def attack (is_stunned):
    damage = 0
    did_poison = False

    if not is_stunned:
        roll = random.randint(1, 100)
        if roll <= 30: #used bite
            damage = random.randint(BITE_DAMAGE_LO, BITE_DAMAGE_HI)
            print(f"The orc bit you for {damage} damage!")
            roll_for_poison = random.randint(1, 100)
            if roll_for_poison <= POISON_RATE:
                did_poison = True
        elif roll <= 80: # used machete
            roll_to_hit = random.randint(1, 100)
            if roll_to_hit <= MACHETE_HIT_RATE:
                damage = random.randint(SLASH_DAMAGE_LO, SLASH_DAMAGE_HI)
                print(f"The orc slashed you with it's machete for {damage} damage!")
        else: #used bind
            roll_to_hit = random.randint(1, 100)
            if roll_to_hit <= BIND_HIT_RATE:
                damage = bind_attack()

    return damage, did_poison

def bind_attack ():
    num_slashes = random.randint(2, 4)
    print(f"The orc bound you and slashes {num_slashes} times!")
    attack_counter = 0
    total_damage = 0
    while attack_counter < num_slashes:
        damage = random.randint(SLASH_DAMAGE_LO, SLASH_DAMAGE_HI)
        crit_roll = random.randint(1, 100)
        if crit_roll <= BIND_CRITICAL_RATE:
            damage *= 2
        total_damage += damage
        attack_counter += 1
    return total_damage

def deal_damage (damage):
    global health
    health -= damage

def frenzy ():
    roll = random.randint(1, 100)
    total_damage = 0
    if roll <= FRENZY_HIT_RATE:
        attacks = random.randint(2, 3)
        attack_count = 0
        print(f"The orc went into a frenzy and punches {attacks} times!")
        while attack_count < attacks:
            damage = random.randint(FRENZY_DAMAGE_LO, FRENZY_DAMAGE_HI)
            print(f"The orc punches for {damage} damage.")
            total_damage += damage
    return total_damage