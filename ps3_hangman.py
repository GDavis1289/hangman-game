# Hangman game
#

# -----------------------------------

import random

WORDLIST_FILENAME = "C:/Users/gdavi/Desktop/Programming/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            count += 1
        else:
            return False

    if count == len(secretWord):
        return True
    else:
        return False  
        


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    wordGuessed = []
    for letter in secretWord:
        if letter in lettersGuessed:
            wordGuessed.append(letter)
        if letter not in lettersGuessed:
            wordGuessed.append('_')
    return " ".join(wordGuessed)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    listAlphabet = list(alphabet)
    for letter in alphabet:
        if letter in lettersGuessed:
            listAlphabet.remove(letter)
    return "".join(listAlphabet)
    

hanger=['''
             _____
            |     |
                  |
                  |
                  |
                 _|_''', '''
             _____
            |     |
            O     |
                  |
                  |
                 _|_''', '''
             _____
            |     |
            O     |
            |     |
                  |
                 _|_''',
                  '''
             _____
            |     |
            O     |
            |     |
            |     |
                 _|_''','''
             _____
            |     |
            O     |
            |     |
            |     |
                 _|_''', '''
             _____
            |     |
            O     |
           /|     |
            |     |
                 _|_''', '''
             _____
            |     |
            O     |
           /|\    |
            |     |
                 _|_''', ''' 
             _____
            |     |
            O     |
           /|\    |
            |     |
           /     _|_''', '''
             _____
            |     |
            O     |
           /|\    |
            |     |
           / \   _|_''','''
   ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
   ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆    

                 O      
      ~LOSER~   /|\   ~LOSER~        
                 |    
                / \ 

   ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆
   ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆''']



def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    mistakesMade = 8
    word = getGuessedWord
    lettersGuessed = []
    while mistakesMade > 0:
        print('------------')
        print('You have ' + str(mistakesMade) + ' guesses left.')
        
        lettersRemaining = getAvailableLetters(lettersGuessed)
        
        print('Available letters: ' + lettersRemaining)
        
        letter_guess = input('Please guess a letter: ')
        guessInLowerCase = letter_guess.lower()
        
        if guessInLowerCase not in lettersGuessed:
            lettersGuessed.append(guessInLowerCase)
            word = getGuessedWord(secretWord, lettersGuessed)
                    
            if guessInLowerCase in secretWord:
                print('Good guess: ' + word)
            else:
                mistakesMade -= 1
                print('Oops! That letter is not in my word: ' + word)
                if mistakesMade == 7:
                    print(hanger[1])
                if mistakesMade == 6:
                    print(hanger[2])
                if mistakesMade == 5:
                    print(hanger[3])
                if mistakesMade == 4:
                    print(hanger[4])
                if mistakesMade == 3:
                    print(hanger[5])
                if mistakesMade == 2:
                    print(hanger[6])
                if mistakesMade == 1:
                    print(hanger[7])
 
                if mistakesMade < 1:
                    print('------------')
                    print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')
                    print(hanger[9])
                    break
                
            didYouWin = isWordGuessed(secretWord, lettersGuessed)
            
            if didYouWin is True:
                print('------------')
                print('Congratulations, you won!')
                break
        else:
            print('Oops! You\'ve already guessed that letter: ' + word)


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

