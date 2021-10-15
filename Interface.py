'''
Created : 14 Oct 2021
@author : Bhargav Modak
'''

import os
from time import sleep
import inventory
import character

from random import randint

# The screen clear function


def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


# A function to show the menu
def menu(player_inventory, person):
    print("==================================================================")
    print(" I : Open Inventory\t E : Exit\t M:Move on ")
    print("==================================================================")
    menuChoice = input()

    # while menuChoice != 'I' and menuChoice != 'E' and menuChoice != 'N':
    #     print("Enter valid input!")
    #     menuChoice = input()

    if menuChoice == 'I':
        player_inventory.display_Inventory(person)
    elif menuChoice == 'E':
        exit()
        # The main function to run the actual interface code


def game_start():
    print("==================================================================")
    print("\t\t\tMonster Battle")
    print("==================================================================")
    sleep(1)
    print("\tGreetings, Fellow adventurer...")
    sleep(1)
    print("\tWelcome to Monster Battle Text Simulator!\n")
    sleep(1)
    print("\tHere you'll go on a great adventure!!\n")
    sleep(1)
    print("==================================================================")
    sleep(1)
    print("Press Enter to continue ...")
    # Consume the input
    input()


def battle_scene(player, player_inventory):
    print("==================================================================")
    print("A wild monster appeared!")
    HP = randint(200, 500)
    print("HP : " + str(HP))
    while player.healthPoints > 0:
        hit = player.attack(player.weapon)
        print("You attacked for " + str(hit) + " damage.")
        HP -= hit
        if HP < 0:
            print("Monster died! Yay!")
            break
        else:
            print("Monster has " + str(HP) + " left.")
            sleep(2)
            hurt = randint(30, 50)
            print("\nMonster hit you for " + str(hurt) + " damage.")
            player.healthPoints -= hurt
            print("You have " + str(player.healthPoints) + " HP left.")
            sleep(2)

    print("==================================================================")


def main():
    game_start()
    #
    screen_clear()
    # Initialize player
    player = character.Character()

    # Initialize inventory
    player_inventory = inventory.Inventory(person=player)
    inventory.inventory_guide(player_inventory, player)

    while(True):
        screen_clear()
        battle_scene(player, player_inventory)

        menu(player_inventory, player)


# If game ran from the main context
if __name__ == '__main__':
    main()
