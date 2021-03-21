# Michael D'Agostino
# Integration Project

# A tool for displaying, calculating, and understanding data commonly used in various fighting games.

# Sources:
# http://dustloop.com/wiki/index.php?title=GGXRD-R2/Damage
# https://bit.ly/3bOeVt6

import math
import random
import time

def main():
    print("Welcome to my Integration Project!")
    print("This is a tool built to demonstrate my coding")
    print("skills in the context of fighting games!")
    menu_selection = input("Enter any key to proceed to the Main Menu: ")
    main_menu()


def main_menu():
    menu_loop = True
    display_main_menu()
    while menu_loop == True:
        menu_selection = input("Where would you like to go? ")
        if (menu_selection == "1"):
            print("Game Data Success")
            game_data_menu()
        elif (menu_selection == "2"):
            print("Numpad Notation Success")
            display_numpad()
        elif (menu_selection == "3"):
            summon_zappa()
            display_main_menu()
        elif (menu_selection == "4"):
            print("Round Timer Success")
            run_game_timer()
        elif (menu_selection == "0"):
            end_program = input("Are you sure you want to quit? (y/n) ")
            if (end_program == "y"):
                print("Thanks for playing!")
                menu_loop = False
            else:
                print("Returning to Main Menu...")
        else:
            print("Unknown command input! Try Again!")

def display_main_menu():
    print("""
Main Menu

Select a mode:
 [1] Game Data
 [2] Guide to Numpad Notation
 [3] Random Summon
 [4] Round Timer
 [0] Quit
""")


def run_game_timer():
    print("Round Timer. Press any key during the timer to summon with Zappa!")
    round_timer = initialize_timer()
    round_timer_first = round_timer // 10
    round_timer_last = round_timer % 10
    # idea: collect input from user during countdown to emulate Zappa's random summons. is it possible to
    # run two functions at once, and use the "last" variable as an argument in the Zappa function?
    print(round_timer_first, round_timer_last)
    while ((round_timer_first > 0) or (round_timer_last > 0)):
        round_timer_first, round_timer_last = cycle_round_timer(round_timer_first, round_timer_last)
        # the plan is to have zappa randomizer run along side this timer function,
        # and let the user spin zappa while the timer ticks. zappa can be
        # determined by the last digit on the timer. i.e. 0, 1, or 2 gives
        # specific summons, every other digit gives a random summon.
    time.sleep(1)
    print("\nTime's Up!\n")
    time.sleep(2)
    print("Returning to Main Menu...")
    display_main_menu()

def initialize_timer():
    round_timer = int(input("How long should the countdown last? (0-99): "))
    if (round_timer <= 0):
        round_timer = 0
    else:
        print("Timer Counting Down!")
    return round_timer

def cycle_round_timer(first, last):
    # The last digit should be used in summon_zappa, when I learn how to run 2 functions at once
    time.sleep(0.8)
    if (last == 0):
        last = 9
        first -= 1
    else:
        last -= 1
    print(first, last)
    return first, last

def summon_zappa():
    summon = random.choice(["dog", "ghost", "sword", "dog", "ghost", "sword", "Raoh!"])
    print("You summoned a" , summon + "!")
    return summon


def game_data_menu():
    menu_loop = True
    display_game_menu()
    while menu_loop == True:
        menu_selection = input("What would you like to do? ")
        if (menu_selection == "1"):
            print("Frame Data Display not available yet. Returning to Frame Data Menu...")
            # Eventually, when I learn how to do databasing in Python, or maybe SQL.
        elif (menu_selection == "2"):
            print("Damage Calculator (SF4) Success")
            run_sf4_calc()
        elif (menu_selection == "3"):
            print("Damage Calculator (GGXrd) Success")
            run_ggxrd_calc()
        elif (menu_selection == "0"):
            print("Returning to Main Menu... ")
            display_main_menu()
            menu_loop = False
        else:
            print("Unknown command input! Try Again!")

def display_game_menu():
    print("""
Game Data Menu

Select a mode:
 [1] Character Frame Data
 [2] Damage Calculator (SF4)
 [3] Damage Calculator (GGXrd)
 [0] Back
""")


def display_numpad():
    print("""
The Numeric Annotation System
 ---------
| 7  8  9 |   The numeric annotation system, or "numpad notation," is based on how
|         |   numbers are arranged on the number pad of a standard keyboard. Each
| 4  5  6 |   number corresponds to a direction, assuming you're facing to the right.
|         |   ie:
| 1  2  3 |   2 = pressing down
 ---------    6 = pressing forwards
              1 = pressing down + back
              5 = "neutral position", which means you don't press any direction
                  and let the joystick return to its neutral position in the
                  center.

              Common Fighting Game inputs:
            236 = Quarter Circle Forwards
            214 = Quarter Circle Backwards
            623 = Dragon Punch
          41236 = Half Circle Forwards

              Buttons are denoted as letters, which are specific to the game at hand and
              how many buttons the game uses.
     Most games = A,B,C,D...
    Guilty Gear = P,K,S,H,D
      DBFZ/MvC3 = L,M,H,S,A1,A2

              You can combine numbers and letters to denote specific moves.
             5A = Standing A
             2C = Crouching C
           236D = Quarter Circle Forwards D
        632146B = Half Circle Back then Forwards B

              There are also certain symbols used that help to notate how to perform
              certain actions, or to designate a specific set of actions.
           [4]6 = Hold back (charge back) for a
                  certain amount of time, then hit
                  forwards.
        5A > 5B = Hit with 5A, then press 5B
            j.C = Press C while in the air (jumping)
             jc = Jump Cancel
    """)
    menu_selection = input("Enter any key to return to the Main Menu: ")
    display_main_menu()

def run_sf4_calc():
    print("\nDamage Calculator (SF4)",
          "Enter the initial damage each move in the combo does to output the total damage done.",
          "Each normal is usually an integer between 30 and 200", sep='\n', end='\n')
    health, combo, counter, proration, total_damage = initialize_sf4()
    for hits in range(combo):
        move_damage = int(input("How much damage does the move do? "))
        if (counter == "y"):
            total_damage *= total_damage * 1.25
            counter = "n"
        proration *= .9
        total_damage += move_damage
    health -= total_damage
    print("Your combo did", total_damage, "damage!")
    print("Your opponent is at", health, "/ 1000 HP!")
    menu_selection = input("Press any key to return to the Game Data Menu.")
    print("Returning to Game Data Menu...")
    display_game_menu()

def initialize_sf4():
    try:
        total_health = 1000
        total_damage = 0
        proration = 1.00
        combo_count = int(input("How many hits does you combo do? "))
        counter_hit = input("Did you land a counter hit? (y/n) ")
        return total_health, combo_count, counter_hit, proration, total_damage
    except:
        print("Unknown value input! Returning to Main Menu...")
        main_menu()

def run_ggxrd_calc():
    print("\nDamage Calculator (GGXrd)", "Enter enemy stats and move data to determine how much damage is done.",
          "(The numbers in parentheses are standardized values in GGXrd.)", sep='\n', end='\n')
    total_health, guts, defense, risc, max_health, proration, move_count, combo = initialize_ggxrd()
    move_damage = set_move_damage()

    while ((move_damage > 0) and (total_health > 0)):
        move_scaling = set_move_scaling()
        move_count += 1

        if (risc > 0):
            move_scaling = 1.0
            risc = int(risc - ((move_damage // 10) + (2 ** move_count) + 5))
            if (risc < 0):
                risc = 0
        else:
            risc = 0

        if (total_health < (max_health * .5)):
            guts_scaling = get_guts(total_health, max_health, guts)
        else:
            guts_scaling = 1.0

        move_damage = int(move_damage * proration * guts_scaling * defense)
        if (move_damage < 1):
            move_damage = 1

        proration *= move_scaling

        total_health -= move_damage
        if (total_health < 0):
            total_health = 0

        if (combo == 0):
            combo = str(move_damage)
        else:
            combo = combo + " + " + str(move_damage)

        display_gauges(move_damage, total_health, risc, max_health, proration, move_count, combo, guts_scaling)
        if check_health(total_health) == 0:
            print("SLASH!\n\n" * 3)
            time.sleep(3)

        else:
            move_damage = set_move_damage()
            if (move_damage == 0):
                print("Nice Combo!")
    print("Returning to Frame Data Menu...")
    display_game_menu()

def initialize_ggxrd():
    # Sets values for GGXrd calc that don't need to be updated every loop. Needed for chars with unique stats.
    try:
        total_health = int(input("What's the enemy's starting health? (integer 1-420): "))
        guts_rating = int(input("What's your opponent's Guts rating? (integer 0-5): "))
        defense_mod = float(input("What's your opponent's Defense Modifier? (0.93-1.30): "))
        risc_gauge = int(input("What's your opponent's starting RISC Gauge? (integer 0-100): "))
        max_health = 420
        proration_scaling = 1.0
        move_count = 0
        combo_equation = 0
        if (total_health > 420):
            total_health = 420
        if (risc_gauge > 100):
            risc_gauge = 100
        return total_health, guts_rating, defense_mod, risc_gauge, max_health, proration_scaling, move_count, combo_equation
    except:
        print("Unknown Input Detected! Returning to Main Menu...")
        main_menu()

def get_guts(total, max, guts):
    # roundabout way of making the health gauge appear lower than how much health you actually have. based on
    # the guts stat, there's a % scaling value applied to the move to make it do less damage when at low health.
    if (total < (max * .1)):
        guts_scaling = float((40 - int((guts * .2) * 4)) * 0.01)
    elif (total < (max * .2)):
        guts_scaling = float((50 - int((guts * .2) * 10)) * 0.01)
    elif (total < (max * .3)):
        guts_scaling = float((60 - int((guts * .2) * 12)) * 0.01)
    elif (total < (max * .4)):
        guts_scaling = float((76 - int((guts * .2) * 16)) * 0.01)
    elif (total < (max * .5)):
        guts_scaling = float((90 - int((guts * .2) * 15)) * 0.01)
    else:
        guts_scaling = 1.0
    return guts_scaling

def set_move_scaling():
    move_scaling = 0.01 * float(input("How much proration scaling does this move have? (integer 50-100%): "))
    return move_scaling

def set_move_damage():
    try:
        move_damage = float(input("How much damage does your move do? (0 to end combo):"))
        return move_damage
    except:
        print("Unknown Input Detected! Returning to Main Menu...")
        main_menu()

def check_health(total_health):
    if (total_health <= 0):
        return 0
    else:
        return 1

def display_gauges(move_damage, total_health, risc, max_health, proration, move_count, combo, guts_scaling):
    filled_gauge = round(20 * (total_health / max_health))
    empty_gauge = 20 - filled_gauge
    print("\nHP:" , "[" + "#"*filled_gauge + " "*empty_gauge + "]")
    print("Total Health:", total_health, "/ 420", sep=' ')
    print("RISC Gauge:  ", risc, "/ 100", sep=' ', end='\n\n')
    print("Combo:", move_count, sep=' ')
    print("Damage of Last Hit:", move_damage, sep=' ')
    print("Next Move's Proration:", format((proration * 100.0), '.2f'), "%", sep=' ')
    print("Guts Scaling:", int(guts_scaling * 100.0), "%", sep=' ')
    print("Current Combo:", combo, sep=' ', end='\n\n')

main()