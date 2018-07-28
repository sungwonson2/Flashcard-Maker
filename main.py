ID_LIST=[]
FLASHCARD_DICT=dict()
from random import randrange

def user():
    print()
    print('MAIN MENU')
    print('1. Create a new flashcard')
    print('2. Delete a flashcard')
    print('3. View all flashcards')
    print('4. Test flashcards')
    user_input=input()
    if user_input=='1':
        create()
    if user_input=='2':
        delete()
    if user_input=='3':
        view()
    if user_input=='4':
        test()
    else:
        print('Invalid input. Please try again.')
        user()

def create():
    id_input=input('What is the numerical id of the flashcard you would like to input:\n')
    try:
        id_input=int(id_input)
    except:
        print('Invalid id input')
    else:
        if id_input in ID_LIST:
            print('Invalid id input: ID already bound to a flaschard')
        if id_input < 1:
            print('Invalid id input: ID cannot be negative')
        else:
            ID_LIST.append(id_input)
            question_input=input('What is the question of the flashcard you would like to input:\n')
            answer_input=input('What is the answer of the flashcard you would like to input:\n')
            FLASHCARD_DICT[id_input]=(question_input,answer_input)
            print('Flashcard has been successfully created')
    user()

def delete():
    if len(ID_LIST)==0:
        print('No flashcards to be deleted')
    delete_input=input('What is the ID of the flashcard that you would like to delete?:\n')
    try:
        delete_input=int(delete_input)
    except:
        invalid('Invalid flashcard ID number')
    if delete_input in ID_LIST:
        ID_LIST.remove(delete_input)
        del FLASHCARD_DICT[delete_input]
        print('Your flashcard has been deleted!')
    else:
        print('Invalid flashcard ID number')
    user()

def view():
    ID_LIST.sort()
    print(ID_LIST)
    for id in ID_LIST:
        print()
        print(str(id)+'.')
        print(FLASHCARD_DICT[id][0])
        print(FLASHCARD_DICT[id][1])
    user()

def test():
    pass

if __name__ == '__main__':
    print('Hello!')
    print('Welcome to Sungwon Son\'s Flashcard Maker!')
    user()
