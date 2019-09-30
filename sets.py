import os
from shutil import copyfile

def viewsets():
    "View all sets that are located within the flashcard folder"
    for file in os.listdir():
        if ".txt" in str(file):
            print(file)
    return 0

def importset():
    "Imports a set of flash cards from a .txt or .docx file that previously exists on the system"
    #NEED TO EDIT (CANCEL FEATURE / CHECK FEATURE)
    print("*****Import Set*****")
    directory = input("What is the directory of the set you would like to import\n")
    copyfile(directory, dest)
    

def createset():
    #NEED TO EDIT (CANCEL FEATURE)
    "Creates a set of flash cards and writes them in a .txt or .docx file in the system"
    print("*****Create Set*****\n")
    file_name = input("What is the name of the set you would like to create\n")
    if os.path.exists(file_name+".txt"):
        print("This file already exists")
        overwrite = input("Would you like to overwrite this file?\n1. Yes\n2. No\n")
        if overwrite == 1:
            f = open(file_name+".txt", "w+")   
            f.close()
            print("File has been created")
            main()
        if overwrite == 2:
            createset()
    else:
        f = open(file_name+".txt", "w+")   
        f.close()
        print("File has been created")
    return 0
