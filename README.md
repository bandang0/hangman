# hangman

###  `hangman`

Welcome to the `hangman` project. `hangman` is a hangman game to learn some vocabulary and have fun with randomly chosen words!

### Copying

`hangman` is released under the GNU GPLv3 License so feel free (as in freedom) and please contribute!

### Playing
Here are the commands to issue:

* `git clone https://github.com/bandang0/hangman` then
* `cd hangman`
* `python src/hangman.py`


### Scores file

`hangman` is a CLI program. It takes no arguments and interaction with the user serves as a guide through the game.

`hangman` registers the scores and names of the players who have already played in a file named `scores`. In order to have access to these scores, the file must be in the directory where you're playing, or else a brand new file will be created with scores back to zero (not touching all the other `scores` files elsewhere on the system, of course).
