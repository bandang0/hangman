""" Interaction with user functions for the hangman project."""

# Provides:
#   welcome
#   goodbye
#   rightLetter(letter)
#   wrongLetter(letter)
#   wholeWord(word)
#   askExit()
#   showTries(tries)
#   printScore(score)
#   win(word, tries)
#   loss(word)
#   chooseLetter(guessed)
#   printState(word, found)
#   rules

import data
import string

welcome = """
        Welcome to the hangman game project, version %s.
        Learn your vocabulary and have fun, right from the command line!

        Copyright (C) 2017 %s
        License: GNU GPLv3 <http://gnu.org/licenses/gpl.html>
        This is free software: you are free to change and redistribute it.
        There is NO WARRANTY, to the extent permitted by law.
        For more information, please see the README file.
        """ % (data.version, data.author)

goodbye = "\nSee you later!"

rightLetter = "Congrats, %r is one of the letters of the word!"

wrongLetter = "Sorry, %r didn't work"

wholeWord = "Nice! You guessed the whole word %r!"

def askExit():
    """Ask whether to exit the program or not."""
    print "Would you like to continue playing?",
    ans = raw_input()
    if ans =='' or ans[0] == 'y' or ans[0] == 'Y':
        print "\nGreat! New word please!"
        return False
    else:
        return True

showTries = "You still have %d tries left."

scoreLine = "You're current score is %d points."

win = "\nBravo! You guessed the word %r in %d tries!"

loss = "Sorry buddy you have not more tries left, the word was %r."

def chooseLetter(guessed):
    print "Go ahead, guess a letter or a word)!",
    ans = raw_input()

    while True:
        if ans == '' or not set(ans).issubset(set(string.letters)):
            print "%r is not valid input, type in just letters." % ans ,
            ans = raw_input()
            continue

        if ans in guessed:
            print "These are your previous tries: ",
            for i in guessed:
                print "%r, " % i
            print "\nYou already tried %r! Pick another one." % ans ,
            ans = raw_input()
            continue

        else:
            break

    return ans

def printState(word, found):
    """Prints the word with only the found letters."""
    toPrint = ''
    for i in word:
        if i in found:
            toPrint = toPrint + i
        else:
            toPrint = toPrint + '*'

    print "\nHere's the word so far: %s" % toPrint

rules = """
    This is hangman! I'm going to pick a word and you're going to have %d tries
    to guess the letters in the word. You can also try to guess the entire
    word. Along the way I'll show you the letters you've already tried and the
    letters you've already guessed in the word.
    """ % data.maxTries
