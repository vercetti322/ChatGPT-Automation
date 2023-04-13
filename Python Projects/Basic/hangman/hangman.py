import random as rd
import string
from words import words # use to import words from words.py file



def getvalid(words):
    word = rd.choice(words) # takes a word from list 'words'
    while '-' in word or ' ' in word:
        word = rd.choice(words)
    return word.upper()

def hangman():
    word = getvalid(words)
    word_letters = set(word) # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guessed
    lives = 6
    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a','b','cd']) --> 'a b cd'
        print('You have', lives, 'lives left. You have used following letters: ', ' '.join(used_letters))

        # what curent word is (ie W_RD)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)  
            else:
                lives = lives - 1
                print('Letter is not in the word')          
        elif user_letter in used_letters:
            print('You have already used that character. Please try again!')
        else:
            print('Invalid character. PLease try again!')

    if lives == 0:
        print('You died, sorry. The word was', word, '!!')
    else:
        print('You guessed the word', word, '!!')

hangman()

# user_input = input('Type something: ')
# print(user_input)


