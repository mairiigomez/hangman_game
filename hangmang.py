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

def run():
    clean_screen()
    list_of_words = read_data()
    word = random.choice(list_of_words)
    chosen_word = list(word.strip().upper())
    #lenght_chosen_word = len(chosen_word)
    list_letters = ['-']*len(chosen_word)
    print(list_letters)
    number_of_tries = 0
    while list_letters != chosen_word:
        position = 0
        letter = input("Choose a letter: ")
        user_letter = letter.upper()
        try: 
            if user_letter.isnumeric() == True:
                raise ValueError("Please, Enter one LETTER")
            elif len(user_letter) > 1:
                raise ValueError("Please, enter just one letter")
            for guess_letter in chosen_word:
                if guess_letter == user_letter:
                    list_letters[position] = user_letter
                position += 1
            number_of_tries += 1
            clean_screen()
            print(list_letters)
        except ValueError as ve:
            print(ve)

    clean_screen()
        
    user_won = f'¡You won! it took you {number_of_tries} times to figure it out'
    print(user_won)    

if __name__ == '__main__':
    run()