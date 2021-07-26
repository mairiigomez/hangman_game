"""Hagman game version 1 
Date: July 26, 2021 
Created by: Mairiyisel """

import random
import os

os.system("cls")

with open("./data.txt","r",encoding="utf-8") as file:
    all_the_words = file.readlines()
number_random = random.randint(0, len(all_the_words))
word = all_the_words[number_random]
chosen_word = list(word.strip())
lenght_chosen_word = len(chosen_word)
list_letters = ['-']*len(chosen_word)
print(list_letters)

number_of_tries = 0
while list_letters != chosen_word:
    position = 0
    user_letter = input("Choose a letter: ")
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
        os.system("cls")
        print(list_letters)
    except ValueError as ve:
        print(ve)
    
os.system("cls")

user_won = f'¡You won! it took you {number_of_tries} times to figure it out'
print(user_won)