# makefile for the hangman project

# run application
run:
	python src/hangman.py

# remove compiled modules
clean:
	find . -name "*.pyc" -exec rm --force {} +
