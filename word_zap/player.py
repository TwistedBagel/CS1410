import random

class Player:

	def __init__(self, name):
		self.name = name
		self.letters = []

		for i in range(7):
			self.drawLetter()

	def getName(self):
		return self.name

	def getLetters(self):
		return self.letters

	def drawLetter(self):
		letters = 'aaaaaaaaabbccddddeeeeeeeeeeeeffggghhiiiiiiiiijkllllmmnnnnnnooooooooppqrrrrrrssssttttttuuuuvvwwxyyz'
		rando = random.choice(letters)
		self.letters.append(rando)
		return rando

	def printLetters(self):
		string = ''
		for i in self.letters:
			string += '%s ' % i
		string = string.strip()
		return string

	def checkWord(self, word):
		letters = self.letters[:]

		for char in word:
			if char in letters:
				letters.remove(char)
			else:
				return False

		self.letters = letters
		return True

players = [Player("Mars"), Player("joe"), Player("Steve")]

def turn(p):
	print("Its %s's turn" % p.getName())
	print(p.printLetters())
	word = input("Enter a word: ")
	p.checkWord(word)
	p.drawLetter()
	print(p.printLetters())

def getNextPlayer(index, players):
	try:
		return (index + 1) % len(players)
	except:
		return 0

def cyclePlayers(i, playersList):
	print(playersList[i % len(playersList)].getName())
	i += 1

def testIndex():
	index = 0
	player = players[index]

	for i in range(5):
		player = getNextPlayer(index, players)
		print(index)
		print("Should be player %s" % players[index].getName())

def test():
	# i = 0
	# player = players[i]
	# for i in range(10):
	# 	# turn(player)
	# 	print(player.getName())
	# 	player = getNextPlayer(i, players)

	index = 0
	for i in range(10):
		player = players[index]
		turn(player)
		index = getNextPlayer(index, players)

if __name__ == "__main__":
	# test()
	# testIndex()
	while True:
		cyclePlayers(0, players)
