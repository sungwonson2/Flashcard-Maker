#FLASHCARD MANAGER

import sets
import flashcards

import os
import sys

randomness_var = False
current_file = ""

dest = os.path.dirname(os.path.realpath(__file__))

def sets_menu():
    "The menu for sets"
    print("*****Manage Sets*****")
    print("1. View Sets")
    print("2. Import Set")
    print("3. Create Set")
    print("4. Exit to menu")
    a = input()
    if a == "1":
        sets.viewsets()
        sets_menu()
    elif a == "2":
        sets.importset()
    elif a == "3":
        sets.createset()
        sets_menu()
    elif a == "4":
        main()
    else:
        print("\nIncorrect value inputted. Please try again. \n")
        sets_menu()

def flashcards_menu(file, flashcards_list):
    "Menu for flashcards"
    print("Flashcards Menu")
    print("1. Add Flashcards")
    print("2. Delete Flashcards")
    print("3. Edit Flashcards")
    print("4. View Flashcards")
    print("5. Test")
    if randomness_var == True:
        print("6. Reset randomness")
        print("7. Exit " + str(file))
    else:
        print("6. Exit " + str(file))
    a = input()
    if a == "1":
        flashcards.createflash(file, flashcards_list)
    elif a == "2":
        flashcards.deleteflash(file, flashcards_list)
    elif a == "3":
        flashcards.editflash(file, flashcards_list)
    elif a == "4":
        for flash in flashcards_list:
            print(flash)
    elif a == "5":
        test()
    elif a == "6":
        if randomness_var == True:
            resetrandomness()
        else:
            main()
    elif a == "7":
        if randomness_var == True:
            main()
        else:
            print("\nIncorrect value inputted. Please try again.\n")
            flashcards_menu()
    else:
        print("\nIncorrect value inputted. Please try again.\n")
        flashcards_menu(file, flashcards_list)
    flashcards_menu(file, flashcards_list)

def options():
    print("Options")
    print("1. Randomness")
    print("2. Exit to menu")
    a = input()
    if a == "1":
        print("1. Randomness on")
        print("2. Randomness off")
        b = input()
        if b == "1":
            randomness_var = True
        elif b == "2":
            ranomdness_var = False
        else:
            print("\nIncorrect value inputted. Please try again.\n")
            options()        
    elif a == "2":
        main()
    else:
        print("\nIncorrect value inputted. Please try again.\n")
        options()

def exit_program():
    "Exits the program"
    sys.exit

def main():
    print("Welcome to Flashcard Manager")
    print("1. Manage Sets")
    print("2. Manage Flashcards")
    print("3. Options")
    print("4. Exit")
    a = input()
    if a == "1":
        sets_menu()
    elif a == "2":
        flashcards.pickset()
    elif a == "3":
        options()
    elif a == "4":
        exit_program()
    else:
        print("\nIncorrect value inputted. Please try again.\n")
        main()

if __name__ == '__main__':
    main()
