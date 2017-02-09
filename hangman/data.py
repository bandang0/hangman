""" Global data for the hangman project."""

# Provides:
#   welcomeString
#   wordList
#   maxTries

import hangman

welcomeString = """
    Welcome to the hangman game project, version %s.
    Learn your vocabulary and have fun, right from the command line!

    Copyright (C) 2017 Raphaël Duque
    License: GNU GPLv3 <http://gnu.org/licenses/gpl.html>
    This is free software: you are free to change and redistribute it.
    There is NO WARRANTY, to the extent permitted by law.
    For more information, please see the README file.
    """ % __version__

# game data
wordList = {'feeling', 'sculptor', 'wonderful', 'sweetest', 'hedgerow'}
maxTries = 8
scoreFile = 'scores'
