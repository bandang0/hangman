"""Core functions for the hangman project."""

# Provides:
#   listScores()
#   askName()
#   chooseWord()
#   letters(word)
#   updateScore(name, score)
#   incl(toFind, found)

import data
import random
import os
import string

def listScores():
    """List all the names and scores listed in the high scores file."""
    # Check for scores file
    if not os.path.isfile('./' + data.scoreFile): # no scores file
        print "There is no high scores file, would you like to create one?",
        ans = raw_input()
        if ans == '' or ans[0] == 'y' or ans[0] == 'Y': # create scores file
            print "Creating scores file."
            newf = open(data.scoreFile, 'w')
            newf.write(data.newFileString)
            newf.close()
        else:
            print "Aborting file creation, exiting program."
            raise SystemExit

    # Print scores
    toPrint = ""
    with open(data.scoreFile, 'r') as sf:
        for line in sf: # add names and scores to output
            if not '#' in line:   # don't add comment lines
                toPrint = toPrint + line + '\n'

    if len(toPrint) == 0:   # no scores yet
        print "There are no scores registered yet."
    else:
        print "Here are the registered players and their scores:\n" + toPrint

def askName():
    """Get name of player and corresponding score if any."""
    # Get name
    print "What is your name?",
    name = raw_input()
    while True:
        if name == '' or name[0] not in string.letters or ' ' in name:
            print "%r is not a valid name, " %name,
            print "the name must start with a letter." % name
            name = raw_input()
        else:
            break

    # Get score
    print "Looking up your score..."
    allStr = "" # string with all names and scores
    with open(data.scoreFile, 'r') as sf:
        for line in sf: # populate string with nales and scores
            if not '#' in line:
                allStr = allStr + line

    if name not in allStr:  # no score for this name
        print "You have no score registered yet! Assigning you a score of 0..."
        return (name, 0)
    else:
        # find score as the string between the name and the end of file/\n
        beg = allStr.find(name, 0) + len(name) + 1
        if allStr.find('\n', beg) != -1:
            end = allStr.find('\n', beg)
        else:
            end = len(allStr) -1
    return (name, int(allStr[beg:end]))


def chooseWord():
    return random.choice(data.wordList)


def letters(word):
    return list(set(word))


def updateScore(name, score):
    return 0

def incl(toFind, found):
    """Verify toFind (as a unordered set) is included in found."""
    rtn = True
    for k in toFind:
        rtn = rtn and k in found
        if not rtn:
            return False
    return True
