"""Main module for the hangman project."""

# Provides:
#   main()

import data# import data
from core import *
from interaction import *

# main function
def main():
    """The whole hangman game, from welcome to exit."""
    # welcome and initialize player info
    welcome()
    try:    # user can exit if he does not create score file in listScores()
        listScores()
    except SystemExit:
        goodbye()
        return 0
    (name, score) = askName()
    tellRules()
    printScore(score)

    # enter the sequence of games
    while True:
        # choose word for game and initialize tries
        word = chooseWord()
        guessed = list()
        found = list()
        toFind = letters(word)
        tries = data.maxTries

        # play the actual game with this word
        while tries > 0 and not incl(toFind, found):
            printState(word, found)
            showTries(tries)
            letter = chooseLetter(guessed)
            guessed.append(letter)
            if letter in word:
                found.append(letter)
                rightLetter(letter)
            else:
                wrongLetter(letter)
            tries = tries - 1

        # determine how much to add to the score (if any)
        if incl(toFind, found):
            win(word, data.maxTries - tries)
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
