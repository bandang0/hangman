"""Main module for the hangman project."""

# Provides:
#   main()

import data
from core import *
from interaction import *
import sys

# main function
def main():
    """The whole hangman game, from welcome to exit."""
    # welcome
    welcome()
    try:
        listScores()
        # user can exit if he does not create score file in listScores()
    except SystemExit:
        goodbye()
        sys.exit(1)
    # initialize player info: hasName == True if name is registered in scores
    # oldscore = score before game, newscore = score during and after game
    (name, oldscore, hasName) = askName()
    newscore = oldscore
    tellRules()
    printScore(newscore)

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
            answer = chooseLetter(guessed)
            guessed.append(answer)

            if answer == word:
                # found whole word
                found.append(answer)
                wholeWord(word)
                tries = tries - 1
                break

            if answer in word:
                # found one letter of the word
                found.append(answer)
                rightLetter(answer)
            else:
                tries = tries - 1
                wrongLetter(answer)


        # determine how much to add to the score (if any)
        if incl(toFind, found) or word in found:
            win(word, data.maxTries - tries)
            toAdd = len(word) + tries
        else:
            loss(word)
            toAdd = 0

        # update in-game score
        newscore = newscore + toAdd
        printScore(newscore)

        exit = askExit()
        if exit is True:
            # write new score to file and quit
            if hasName:
                # add score to entry in scores file
                updateScore(name, oldscore, newscore)
            else:
                #append name and score to scores file
                addScore(name, newscore)

            # exit
            goodbye()
            sys.exit(0)



# entrance point for the hangman game
if __name__ == '__main__':
    main()
