#HANGMAN GAME

# random, while loop, if-else, strings and lists are used.

# Game working
'''
import random -> list of words -> random choice -> use while loop for the limiting of wrong answers ->
user input (1 letter) -> take the size of word into an undersore ->
if the user input is true then reveal the letter in the under score else increment the incorrect guesses count ->
result fail of success

'''

# importing the random function
import random

# here are the list of words for the game
words_list = ['superman','batman','ironman','captain','spiderman']

# picking a random word
mystery_word = random.choice(words_list)

#locked word length and locked word
word_len = len(mystery_word)

word=[]
for i in range(word_len):
    word.append('_')

incorrect = 0

while incorrect < 6:

    # ask the player for the input letter inside a while loop
    letter_input = input("Please enter a letter you guessed! :" ).lower()


    # checks if the letter is in the secret word
    if letter_input in mystery_word:

        # indexing in matching the positions
        for index,letter in enumerate(mystery_word):
            if letter == letter_input:
                word[index] = letter_input
                    
        print(word)
        if '_' not in word:
            print("\nThe mystery word is \"",mystery_word,"\"")
            print("You have Won the game!!")
            break

    else:
        incorrect += 1
        print("You have guessed it Wrong!! ")
else: print("You have lost your chances!! ")

