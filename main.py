import sys
import random 
from termcolor import colored, cprint



def welcomeUser():
    print("Welcome to Wordle!")
    print("Would you like to learn about the rules of the game? (y/n)")
    answer = input()
    if answer == "y":
        print("""\nThe rules of the game are simple. You will be given a word of 5 letters.
        You will have 5 guesses to guess the word. After each guess, you will be given
        a hint. The hint will tell you how many letters are in the correct position
        and how many letters are in the word but not in the correct position.\n""")

def pickWord():

    rWords = open("word.txt", "r") # opens file
    word = random.choice(rWords.readlines()) # picks random word from file
    word = word.strip().lower() # removes \n and makes lowercase
    return word # returns word

def getHint(word, guess):
    
        for i in range(min(len(guess), 5)): 
            if guess[i] == word[i]: # if letter is in correct position
                print(colored(guess[i], 'green'), end = "") # colors letter green

            elif guess[i] in word: # if letter is in word but not in correct position
                print(colored(guess[i], 'yellow'), end = "") # colors letter yellow

            else: # if letter is not in word
                print(colored(guess[i], 'red'), end = "") # colors letter red

def playGame():

    word = pickWord() # picks random word
    guesses = 5 # sets number of guesses to 5
    hold = "_ _ _ _ _"

    while guesses > 0: # while there are still guesses
        print("\nGuess a 5 letter word\n")
        print(hold) # prints word with blanks

        guess = input() # gets user input
        guess = guess.strip().lower() # removes \n and makes lowercase

        if guess == word: # if guess is correct
            print("\nYou win!")
            print("The word was " + word)
            break # breaks out of while loop

        else: # if guess is incorrect
            guesses -= 1 # subtracts 1 from guesses

            if guesses == 0: # if there are no more guesses
                print("\nYou lose!")
                print("The word was " + word)
                break # breaks out of while loop

            else: # if there are still guesses
                print("\nYou have " + str(guesses) + " guesses left")
                getHint(word, guess) # gets hint
                print("\n")
        

def main():
    welcomeUser() # welcomes user
    playGame() # plays game
    

main()