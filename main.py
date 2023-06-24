import random 


def welcomeUser():
    print("Welcome to Wordle!")
    print("Would you like to learn about the rules of the game? (y/n)")
    answer = input()
    if answer == "y":
        print("""The rules of the game are simple. You will be given a word of 5 letters.
        You will have 5 guesses to guess the word. After each guess, you will be given
        a hint. The hint will tell you how many letters are in the correct position
        and how many letters are in the word but not in the correct position.""")

def pickWord():

    rWords = open("word.txt", "r") # opens file
    word = random.choice(rWords.readlines()) # picks random word from file
    word = word.strip().lower() # removes \n and makes lowercase
    return word # returns word

def getHint(word, guess):
    
        hint = "" # initializes hint
        for i in range(0, len(word)): # for each letter in word
            if guess[i] == word[i]: # if letter is in correct position
                hint += guess[i].upper() # adds letter to hint in uppercase
            elif guess[i] in word: # if letter is in word but not in correct position
                hint += guess[i] # adds letter to hint
            else: # if letter is not in word
                hint += "-" # adds - to hint
        return hint # returns hint

def playGame():

    word = pickWord() # picks random word
    guesses = 5 # sets number of guesses to 5
    while guesses > 0: # while there are still guesses
        print("Guess a 5 letter word")
        guess = input() # gets user input
        guess = guess.strip().lower() # removes \n and makes lowercase
        if guess == word: # if guess is correct
            print("You win!")
            break # breaks out of while loop
        else: # if guess is incorrect
            guesses -= 1 # subtracts 1 from guesses
            if guesses == 0: # if there are no more guesses
                print("You lose!")
                print("The word was " + word)
                break # breaks out of while loop
            else: # if there are still guesses
                print("You have " + str(guesses) + " guesses left")
                hint = getHint(word, guess) # gets hint
                print(hint) # prints hint
        

def main():
    welcomeUser() # welcomes user
    playGame() # plays game
    

main()