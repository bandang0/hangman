"""Main module for the hangman project."""

# Provides:
#   main()

from hangman import data
from hangman.core import *
from hangman.interaction import *

# main function
def main():
    """The whole hangman game, from welcome to exit."""
    # welcome and initialise player info
    welcome()
    listScores()
    (name, score) = askName()
    tellRules()
    printScore(score)

    # enter the sequence of games
    while True:
        # choose word for game nd initialize tries
        word = chooseWord()
        found = list()
        toFind = letters(word)
        tries = data.maxTries

        # play the actual game with this word
        while tries > 1 and found is not toFind:
            printState(word, found)
            showTries(tries)
            letter = chooseLetter(found)
            if letter in word:
                found.append(letter)
                rightLetter(letter)
            else:
                wrongLetter(letter)
            tries = tries - 1

        # determine how much to add to the score (if any)
        if found = toFind:
            win(word, tries)
            toAdd = len(word) + data.maxTries - tries
        else:
            loss(word)
            toAdd = 0

        # update in-game score
        score = score + toAdd
        printScore(score)

        exit = askExit()
        if exit is True:
            # write new score to file and quit
            updateScore(name, score)
            goodbye()
            return 0



# entrance point for the hangman project
if __name__=='__main__':
    main()
