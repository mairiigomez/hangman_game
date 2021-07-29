"""Hagman game version 2 
Date: July 26, 2021 
Created by: Mairiyisel """

import random
import os

def clean_screen():
    return os.system("cls")

def read_data():
    with open("./data.txt","r",encoding="utf-8") as file:
        list_of_words = file.readlines()
        return list_of_words

def draw_hangman(failure, list_of_letters):
    hangman_list = [
        '''
    ||==================
    ||            |
    || 
    ||
    ||
    ||
    ||
    ||
    ||
    ||
    ||
    ||
    ||
    ||
    ||
    =======@========== ========
    ||                        ||
    ||                        ||
    ||                        ||
    ''',
        '''
    ||==================
    ||           |
    ||          ___
    ||         /   \\
    ||        | * * |
    ||         \___/
    ||           
    ||
    ||
    ||
    ||
    ||
    ||
    ||
    ||
    =======@========== ========
    ||                        ||
    ||                        ||
    ||                        ||
    ''',
        '''
    ||==================
    ||            |
    ||           ___
    ||          /   \\
    ||         | * * |
    ||          \___/
    ||            |
    ||            |
    ||            |
    ||            |
    ||            |
    ||
    ||
    ||
    ||
    =======@========== ========
    ||                        ||
    ||                        ||
    ||                        ||
    ''',
        '''
    ||==================
    ||            |
    ||           ___
    ||          /   \\
    ||         | * * |
    ||          \___/
    ||            |
    ||        ----|
    ||            |
    ||            |
    ||            |
    ||
    ||
    ||
    ||
    =======@========== ========
    ||                        ||
    ||                        ||
    ||                        ||
    ''',
        '''
    ||==================
    ||            |
    ||           ___
    ||          /   \\
    ||         | * * |
    ||          \___/
    ||            |
    ||        ----|----
    ||            |
    ||            |
    ||            |
    ||
    ||
    ||
    ||
    =======@========== ========
    ||                        ||
    ||                        ||
    ||                        ||
    ''',
        '''
    ||==================
    ||            |
    ||           ___
    ||          /   \\
    ||         | * * |
    ||          \___/
    ||            |
    ||        ----|----
    ||            |
    ||            |
    ||            |
    ||           /
    ||          /
    ||         /
    ||
    =======@========== ========
    ||                        ||
    ||                        ||
    ||                        ||
    ''',
        '''
    ||==================
    ||            |
    ||           ___
    ||          /   \\
    ||         | x x |
    ||          \___/
    ||            |
    ||        ----|----
    ||            |
    ||            |
    ||            |
    ||           / \\
    ||          /   \\
    ||         /     \\
    ||
    =======@            ========
    ||      \                 ||
    ||       \                ||
    ||        \               ||
    '''
    ]
    if failure >= len(hangman_list)-1:
        print(hangman_list[len(hangman_list)-1], list_of_letters)
    else:
        print(hangman_list[failure],list_of_letters)

def run():
    clean_screen()
    print(
        '''
   **  **    ***    **   **  *******  **      **    ***    **   **
   **  **   ** **   ***  **  **       ***    ***   ** **   ***  **
   ******   *****   **** **  ** ****  ****  ****   *****   **** **
   **  **  **   **  ** ****  **   **  ** **** **  **   **  ** ****
   **  **  **   **  **  ***  *******  **  **  **  **   **  **  ***
    ''')
    os.system('pause')

    list_of_words = read_data()
    word = random.choice(list_of_words)
    chosen_word = list(word.strip().upper())
    #lenght_chosen_word = len(chosen_word)
    list_letters = ['-']*len(chosen_word)
    #print(list_letters)
    number_of_tries = 0
    failure = 0
    clean_screen()
    draw_hangman(failure, list_letters)
    while list_letters != chosen_word and failure < 6:
        position = 0
        user_fail = True
        letter = input("Choose a letter: ")
        user_letter = letter.upper()
        try: 
            if user_letter.isnumeric() == True:
                raise ValueError("Please, Enter one LETTER")
            elif len(user_letter) > 1:
                raise ValueError("Please, enter just one letter")
            #elif number_of_tries > 7:
             #   raise ValueError("Game Over!")
            for guess_letter in chosen_word:
                if guess_letter == user_letter:
                    list_letters[position] = user_letter
                    user_fail = False
                position += 1
            number_of_tries += 1
            
            if user_fail == True:
                failure += 1

            clean_screen()
            draw_hangman(failure, list_letters)
        
        except ValueError as ve:
            print(ve)
        


    clean_screen()
    
    if list_letters == chosen_word:
        user_won = f'¡You won! it took you {number_of_tries} times to figure it out'
        print(user_won) 
    else:
        draw_hangman(failure, list_letters)
        print("GAME OVER")   

if __name__ == '__main__':
    run()