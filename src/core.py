"""Core functions for the hangman project."""

# Provides:
#   listScores()
#   askName()
#   updateScore(name, oldscore, newscore)
#   addScore(name, score)
#   noComment(fileName, exclude = '#')

import data
import os
import string

def listScores():
    """List all the names and scores listed in the high scores file."""
    # Check for scores file
    if not os.path.isfile(data.scoreFile): # no scores file
        print "There is no high scores file, would you like to create one?",
        ans = raw_input()
        if ans == '' or ans[0] == 'y' or ans[0] == 'Y': # create scores file
            print "Creating scores file."
            newf = open(data.scoreFile, 'w')
            newf.write(data.newFileString)
            newf.close()
        else:
            print "Aborting file creation, exiting program."
            raise SystemExit("Exit for refusal of scores file creation.")

    # Print scores
    toPrint = noComment(data.scoreFile)

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
        if name == ''  or ' ' in name or name[0] not in string.letters:
            print "%r is not a valid name, " % name,
            print "the name must start with a letter and contain no spaces."
            name = raw_input()
        else:
            break

    # Get score
    print "Looking up your score..."
    allStr = noComment(data.scoreFile) # string with all names and scores

    if name not in allStr:  # no score for this name
        print "You have no score registered yet! Assigning you a score of 0..."
        return (name, 0, False)
    else:
        # find score as the string between the name and the end of file/\n
        beg = allStr.find(name, 0) + len(name) + 1
        if allStr.find('\n', beg) != -1:
            end = allStr.find('\n', beg)
        else:
            end = len(allStr) -1
    return (name, int(allStr[beg:end]), True)

def updateScore(name, oldscore, newscore):
    """Update the score of a registered player on the scores file."""
    print "\nUpdating scores file..."
    allStr = noComment(data.scoreFile) # containing all the non-commented lines

    # replace "name oldscore" by "name newscore" in allStr
    olds = "%s %d" % (name, oldscore)
    news = "%s %d" % (name, newscore)
    allStr = allStr.replace(olds, news, 1)

    # write to file
    with open(data.scoreFile, 'w') as sf:
        sf.write(data.newFileString)
        sf.write(allStr)

    print "Wrote your new score to scores file."

def addScore(name, score):
    """Add a non-registered player and his new score to the scores file."""
    print "\nUpdating scores file..."
    open(data.scoreFile, 'a').write("%s %d\n" % (name,score))

    print "Wrote your new score to the scores file."

def noComment(fileName, exclude = '#'):
    """Return string of all the non-commented lines of the file.

    This raises an IOError if the file is not found.

    """
    allStr = "" # string with all names and scores
    if not os.path.isfile(fileName):
        raise IOError("%r file not found while extracting non-comment lines.")
    else:
        sf = open(fileName, 'r')
        for line in sf: # populate string with names and scores
            if not exclude in line:
                allStr = allStr + line
        sf.close()

    return allStr
