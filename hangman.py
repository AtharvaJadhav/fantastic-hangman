# Hangman Game
# ------------

import string
import sys
import random

WORDLIST_FILENAME = "words.txt"

def load_words():
	"""
	Returns a list of valid words. Words are strings of lowercase letters.
	
	Depending on the size of the word list, this function may
	take a while to finish.
	"""
	#print("Loading word list from file...")
	# inFile: file
	inFile = open(WORDLIST_FILENAME, 'r')
	# line: string
	line = inFile.readline()
	# wordlist: list of strings
	wordlist = line.split()
	#print("  ", len(wordlist), "words loaded.")
	return wordlist

def choose_word(wordlist):
	"""
	wordlist (list): list of words (strings)
	
	Returns a word from wordlist at random
	"""
	return random.choice(wordlist)

wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
	'''
	secret_word: string, the word the user is guessing; assumes all letters are
	lowercase
	letters_guessed: list (of letters), which letters have been guessed so far;
	assumes that all letters are lowercase
	returns: boolean, True if all the letters of secret_word are in letters_guessed;
	False otherwise
	'''
	word = secret_word
	for i in range(0, len(letters_guessed)):
		for j in range(0, len(secret_word)):
			if letters_guessed[i] == secret_word[j]:
				word = word.replace(secret_word[j],'')
	if word == '':
		return True
	return False

def get_guessed_word(secret_word, letters_guessed):
	'''
	secret_word: string, the word the user is guessing
	letters_guessed: list (of letters), which letters have been guessed so far
	returns: string, comprised of letters, underscores (_), and spaces that represents
	  which letters in secret_word have been guessed so far.
	'''
	word = list(secret_word)
	for i in range(0, len(secret_word)):
		word[i] = '_ '
	for i in range(0, len(secret_word)):
		for j in range(0, len(letters_guessed)):
			if secret_word[i] == letters_guessed[j]:
				word[i] = letters_guessed[j] + ' '
	spam = ''.join(word)
	return spam

def get_available_letters(letters_guessed):
	'''
	letters_guessed: list (of letters), which letters have been guessed so far
	returns: string (of letters), comprised of letters that represents which letters have not
	  yet been guessed.
	'''
	alphabets = string.ascii_lowercase
	remaining_alphabets = alphabets
	for i in range(0, len(letters_guessed)):
		for j in range(26):
			if letters_guessed[i] == alphabets[j]:
				remaining_alphabets = remaining_alphabets.replace(alphabets[j], '')
	return remaining_alphabets

def hangman(secret_word):
	'''
	secret_word: string, the secret word to guess.
	
	Starts up an interactive game of Hangman.
	
	* At the start of the game, printing how many 
	  letters the secret_word contains and how many guesses s/he starts with.
	  
	* The user should start with 6 guesses

	* Before each round, you should display to the user how many guesses
	  s/he has left and the letters that the user has not yet guessed.
	
	* Asking the user to supply one guess per round.
	
	* Making sure that the user puts in a letter!
	
	* The user receives feedback immediately after each guess about whether
	  their guess appears in the computer's word.

	* After each guess, display to the user the partially guessed word so far.
	
	'''
	print('Welcome to the game Hangman!')
	print('I am thinking of a word that is ' + str(len(secret_word)) + ' letters long.')
	print('-----------------------------------------------')
	letters_guessed = []
	i = 10
	while True:
		letters_guessed.insert(0, input())
		#print(letters_guessed)
		print('You have ' + str(i) + ' guesses left')
		print('Available letters: ' + get_available_letters(letters_guessed))
		print(get_guessed_word(secret_word, letters_guessed))
		if is_word_guessed(secret_word, letters_guessed):
			print('Good Job! The secret word was ' + secret_word + '.')
			break
		if i == 0:
			print('You failed. The secret word was ' + secret_word + '.')
			break
		i = i - 1
	print('Would you like to play again? (y/n)')
	choice = input()
	if choice == 'y':
		secret_word = choose_word(wordlist)
		hangman(secret_word)
	elif choice == 'n':
		sys.exit()
	else:
		print('Please enter a valid choice. (y/n)')

if __name__ == "__main__":

	secret_word = choose_word(wordlist)
	#secret_word = 'apple'
	hangman(secret_word)
