# Hangman Game
# -----------------------------------

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
				#print(word)
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
	
secret_word = 'apple'
letters_guessed = ['a', 'l', 'm', 'n', 'e']
print(get_guessed_word(secret_word, letters_guessed))