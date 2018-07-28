ID_LIST=[]
FLASHCARD_DICT=dict()
import random
import sys

def menu():
    print()
    print('MAIN MENU')
    print('1. Create a new flashcard')
    print('2. Delete a flashcard')
    print('3. View all flashcards')
    print('4. Test flashcards')
    print('5. Exit')
    user_input=input()
    if user_input=='1':
        create()
    if user_input=='2':
        delete()
    if user_input=='3':
        view()
    if user_input=='4':
        test()
    if user_input=='5':
        sys.exit()
    else:
        print('Invalid input. Please try again.')
        menu()

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
    menu()

def delete():
    if len(ID_LIST)==0:
        print('No flashcards to be deleted')
    delete_input=input('What is the ID of the flashcard that you would like to delete?:\n')
    try:
        delete_input=int(delete_input)
    except:
        print('Invalid flashcard ID number')
        menu()
    if delete_input in ID_LIST:
        ID_LIST.remove(delete_input)
        del FLASHCARD_DICT[delete_input]
        print('Your flashcard has been deleted!')
    else:
        print('Invalid flashcard ID number')
    menu()

def view():
    ID_LIST.sort()
    print(ID_LIST)
    for id in ID_LIST:
        print()
        print(str(id)+'.')
        print(FLASHCARD_DICT[id][0])
        print(FLASHCARD_DICT[id][1])
    menu()

def flash_test(id=None):
    if id==None:
        flash_id=random.choice(ID_LIST)
    else:
        flash_id=id
    user_answer=input(str(flash_id)+'. '+str(FLASHCARD_DICT[flash_id][0])+'\n')
    if user_answer==FLASHCARD_DICT[flash_id][1]:
        print('Congratulations! You are correct!')
        test()
    else:
        print('Sorry, you are incorrect.')
        user_input=('Input y to try again, input n to skip.')
        if user_input=='y':
            flash_test(flash_id)
                    

def test():
    if len(ID_LIST)==0:
        print('No flashcards to test')
        menu()
    else:
        user_input=input('\nInput n to go to next flashcard. Input e to exit testing\n')
        if user_input=='n':
            flash_test()
        if user_input=='e':
            menu()
        else:
            print('Invalid input. Please try again.')
            test()

if __name__ == '__main__':
    print('Hello!')
    print('Welcome to Sungwon Son\'s Flashcard Maker!')
    menu()
