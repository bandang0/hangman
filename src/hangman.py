"""Main module for the hangman project."""

# Provides:
#   main()

import sys
import random
import data
import core
import interaction


# main function
def main():
    """The whole hangman game, from welcome to exit."""
    # welcome
    print interaction.welcome
    try:
        core.listScores()
        # user can exit if he does not create score file in listScores()
    except SystemExit:
        print interaction.goodbye
        sys.exit(1)
    # initialize player info: hasName == True if name is registered in scores
    # oldscore = score before game, newscore = score during and after game
    (name, oldscore, hasName) = core.askName()
    newscore = oldscore
    print interaction.rules
    print interaction.scoreLine % newscore

    # enter the sequence of games
    while True:
        # choose word for game and initialize tries
        word = random.choice(data.wordList)
        guessed = set()
        found = set()
        toFind = set(word)
        tries = data.maxTries

        # play the actual game with this word
        while tries > 0 and not toFind.issubset(found):
            interaction.printState(word, found)
            print interaction.showTries % tries
            answer = interaction.chooseLetter(guessed)
            guessed.add(answer)

            if answer == word:
                # found whole word
                found.add(answer)
                print interaction.wholeWord % word
                tries = tries - 1
                break

            if answer in word:
                # found one letter of the word
                found.add(answer)
                print interaction.rightLetter % answer
            else:
                tries = tries - 1
                print interaction.wrongLetter % answer

        # determine how much to add to the score (if any)
        if toFind.issubset(found) or word in found:
            print interaction.win % (word, data.maxTries - tries)
            toAdd = len(word) + tries
        else:
            print interaction.loss % word
            toAdd = 0

        # update in-game score
        newscore = newscore + toAdd
        print interaction.scoreLine % newscore

        exit = interaction.askExit()
        if exit is True:
            # write new score to file and quit
            if hasName:
                # add score to entry in scores file
                core.updateScore(name, oldscore, newscore)
            else:
                #append name and score to scores file
                core.addScore(name, newscore)

            # exit
            print interaction.goodbye
            sys.exit(0)

# entrance point for the hangman game
if __name__ == '__main__':
    main()
