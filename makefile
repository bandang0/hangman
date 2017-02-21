# makefile for the hangman project

# run application
run:
	python src/hangman.py

# remove compiled modules
clean-pyc:
	find . -name "*.pyc" -exec rm --force {} +

# remove scores files
clean-score:
	find . -name "scores" -exec rm --force {} +

# remove compiled documentation
clean-doc:
	
