""" Interaction with user functions for the hangman project."""
# Provides:
#   welcome()
#   goodbye()
#   rightLetter(letter)
#   wrongLetter(letter)
#   askExit()
#   showTries(tries)
#   printScores(score)
#   win(word, tries)
#   loss(word)
#   chooseLetter(guessed)
#   printState(word, found)
#   tellRules()

import __init__
import string
import data

def welcome():
    """Welcome the user to the game."""
    print """
        Welcome to the hangman game project, version %s.
        Learn your vocabulary and have fun, right from the command line!

        Copyright (C) 2017 %s
        License: GNU GPLv3 <http://gnu.org/licenses/gpl.html>
        This is free software: you are free to change and redistribute it.
        There is NO WARRANTY, to the extent permitted by law.
        For more information, please see the README file.
        """ % (__init__.__version__, __init__.__author__)

def goodbye():
    print "So sad to see you go, see you later!"

def rightLetter(letter):
    print "Congrats, %r is one of the letters of the word!" % letter

def wrongLetter(letter):
    print "Sorry, %r is not one of the letters we're looking for." % letter

def askExit():
    """Ask whether to exit the program or not."""
    print "Would you like to continue playing?",
    ans = raw_input()
    if ans =='' or ans[0] == 'y' or ans[0] == 'Y':
        return False
    else:
        return True

def showTries(tries):
    print "You still have %d tries left." % tries

def printScore(score):
    print "You're current score is %d points." % score

def win(word, tries):
    print "Nice! You guessed the word %r in %d tries!" % (word, tries)

def loss(word):
    print "Sorry buddy you have not more tries left, the word was %r." % word

def chooseLetter(guessed):
    print "Go ahead, guess a letter.",
    ans = raw_input()

    while True:
        if ans == '' or ans[0] not in string.letters:
            print "%r is not valid input, type in just a letter." % ans ,
            ans = raw_input()
            continue

        if ans[0] in guessed:
            print "These are the letters you've already tried: ",
            for i in range(len(guessed)):
                print "%s, " % guessed[i] ,
            print "\nYou already tried %r! Pick another one." % ans[0] ,
            ans = raw_input()
            continue

        else:
            break

    return ans[0]

def printState(word, found):
    """Prints the word with only the found letters."""
    toPrint = ''
    for i in range(len(word)):
        if word[i] in found:
            toPrint = toPrint + word[i]
        else:
            toPrint = toPrint + '*'

    print "Here's the word so far: %s" % toPrint

def tellRules():
    print """
    This is hangman! I'm going to pick a word and you're going to have %d tries
    to guess the letters in the word. Along the way I'll show you the letters
    you've already tried and the letters you've already guessed in the word.
    """ % data.maxTries
