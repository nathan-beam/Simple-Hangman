import sys,os,random

class Hangman:	
	
	def __init__(self):
		"""Constructor to create the appropriate game variables"""
		self.word = self.generateWord()
		self.counter = 0
		self.gameOver = False
		self.correctLetters = []
		self.incorrectLetters = []
		
	def run(self):
		"""Driver function for the game. Prints the board while the
		player is playing and checks for winstate after each guess"""
		self.clearScreen()
		while(not self.gameOver):
			self.printBoard()
			guess = input("Enter the letter to guess: ")
			if(len(guess) == 1):
				self.tryGuess(guess)
			self.checkWin()
		print("Thanks for playing!")
		
		
	def generateWord(self):
		"""Grabs a random word from the supplied dictionary"""
		filename = sys.path[0] + '/dictionary.txt'
		words = open(filename).read().splitlines()
		word = random.choice(words)
		return word
		
	def tryGuess(self, guess):
		"""Handles a single-letter guess for a letter in the word"""
		if guess in self.word:
			if guess not in self.correctLetters:
				self.correctLetters.append(guess)
		else:
			if guess not in self.incorrectLetters:
				self.counter += 1
				self.incorrectLetters.append(guess)

			
	def checkWin(self):
		"""Checks if the user has either run 
		out of guesses or guessed the word"""
		self.clearScreen()
		if self.counter == 6:
			self.printHangman();
			self.gameOver = True
			print("You Lose")
			print("The word was", self.word)
		elif (self.allLettersGuessed()):
			self.printHangman();
			self.gameOver = True
			print("You win!")
			print("The word was", self.word)
			
	def printBoard(self):
		"""Prints the guessed letters and fills in 
		successfully guessed blanks in the word"""
		self.printHangman()
		print("Word: " ,end="")
		for c in self.word:
			if c in self.correctLetters:
				print(c,end=" ")
			else:
				print("_ ",end="")
		print("")
		print("Guesses: " ,end="")
		for c in self.incorrectLetters:
			print(c,end="")
		print("")

		
	def allLettersGuessed(self):
		"""Returns true if all letters in the word are successfully guessed"""
		for c in self.word:
			if c not in self.correctLetters:
				return False
		return True
	
	def printHangman(self):
		"""Prints the hangman figure to indicate guesses left"""
		print("  |--|")
		print("  |  |")
		if(self.counter>0):
			print("  O  |")
		else:
			print("     |")
		
		if(self.counter > 3):
			print(" /|\\ |")
		elif(self.counter > 2):
			print(" /|  |")
		elif(self.counter > 1):
			print("  |  |")
		else:
			print("     |")
			
		if(self.counter > 5):
			print(" / \\ |")
		elif(self.counter > 4):
			print(" /   |")
		else:
			print("     |")
		print("     |")
		print("___________")
		print("")

	def clearScreen(self):
		"""Clears the screen to refresh the board"""
		os.system('cls')

def main():
	"""Main function. Will generate hangman games until the user decides to stop"""
	playAgain = "y"
	while playAgain == "y":
		hm = Hangman()
		hm.run()
		playAgain = input("Play Again? y/n:")
			
main()