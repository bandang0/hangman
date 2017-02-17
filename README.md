# hangman

#### Preamble

This is a very simple hangman game. The aim of this repository is to be
a complete Python project: correctly packaged, well documented and written
software.

It serves as a first fully grown project, and ambitions to be only the first of many.


###  `hangman`

Welcome to the `hangman` project. `hangman` is a hangman game to learn some vocabulary and have fun with randomly chosen words!

### Copying

`hangman` is released under the GNU GPLv3 License so feel free (as in freedom) and please contribute!

### Installation
Multiple ways (all with root privileges):

* `git clone https://github.com/bandang0/hangman` then
`cd hangman`
`python src/hangman.py` (as of v1.0)

* `git clone https://github.com/bandang0/hangman` then
`cd hangman`
`make install` (as of v1.5)

* `pip install hangman` (as of v1.8)


### Usage

v1.0 of `hangman` is a CLI program. It takes no arguments and interaction with the user serves as a guide through the game.

`hangman` registers the scores and names of the players who have already played in a file named `scores`. In order to have access to these scores, the file must be in the directory where you're playing, or else a brand new file will be created with scores back to zero (not touching all the other `scores` files elsewhere on the system, of course).
