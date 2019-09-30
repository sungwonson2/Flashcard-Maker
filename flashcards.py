import os

import sets
import main

class flashcard():
    "The class for all flashcards"
    def __init__(self, word : str, definition : str, randomness : int):
        self.word = word
        self.definition = definition
        self.randomness = randomness
    def __repr__(self):
        return ("flashcard(" + self.word + ", " + self.definition + ", " + str(self.randomness) + ")")
    def __str__(self):
        return(str([self.word, self.definition, self.randomness]))

def createflash(file, flashcards):
    #ADD CANCEL FEATURE + DEAL WITH SAME WORDS
    "Creates a flashcard and adds them to the set"
    current_file = open(file, "a")
    print("What is the word you want to add to the set")
    name = input()
    print("What is the definition you want to add to the set")
    definition = input()
    if main.randomness_var == True:
        print("Would you like to adjust the randomness of the flashcard?\n1. Yes\n2. No")
        randomness = input()
        if randomness == 1:
            print("What would you like to adjust the randomness to?")
            randomness = input()
        else:
            randomness = 0
    else:
        randomness = 0
    flash = flashcard(name, definition, randomness)
    current_file.write(str(name) + " " + str(definition) + " " + str(randomness) + "\n")
    flashcards.append(flash)
    current_file.close()
    return 0
    

def deleteflash(file, flashcards):
    #ADD CANCEL FEATURE
    "Deletes a flashcard from the set"
    current_file_in = open(file, "r")
    current_file_out = open(file, "a")
    print(current_file_in.readlines())
    file_contents = []
    for line in current_file_in.readlines():
        print(line)
        file_contents.append(line)
    print("What is the word you would like to delete from the set")
    name = input()
    for line in current_file_in:
        if name in line:
            file_contents.delete(line)
            current_file_in.close()
            current_file_out.close()
            for content in file_contents:
                current_file_out.write(line)
            for flashcard in flashcards:
                if name in flashcard:
                    flashcards.delete(flashcard)
            return 0
    print("This word does not exist in this flashcard set\nPlease try again.")
    deleteflash(file,flashcards)

def editflash(file, flashcards):
    #ADD CANCEL FEATURE
    "Edit a flashcard from the set"
    return 0

def randomness():
    "Defines the randomness component in the probability of the flashcard showing up"
    return 0

def resetrandomness():
    "Resets the randomness of all cards in the set"
    for flashcard in flashcards:
        flashcard[2] = 0
    return 0

def test():
    "Tests the user using the flashcards in the set"

def pickset():
    "Allows user to pick the set they want to use"
    print("*****Pick Set*****")
    print("Which set would you like to use")
    sets.viewsets()
    file = input()
    if file in os.listdir() or file + ".txt" in os.listdir():
        current_file = file
        if current_file[-4:0] != ".txt":
            current_file += ".txt"
        f = open(current_file, "r")
        f.close()
        make_flashcards(current_file)
    else:
        print("Set does not exist in directory. Please try again")
        pickset()
    
def make_flashcards(file):
    #MAKE RANDOMNESS 0 IF DOES NOT EXIST
    "Converts the text document into a list of flashcards"
    current_file = open(file, "r")
    flashcards = []
    for line in current_file.readlines():
        split = line.split()
        if len(split) == 2:
            flashcards.append(flashcard(split[0], split[1], 0))
        elif len(split) == 3:
            flashcards.append(flashcard(split[0], split[1], split[2]))
    current_file.close()
    main.flashcards_menu(file, flashcards)
