import sys

def createIndex():
	return {}

def recordBook(index, isbn, title):
	index[isbn] = title

def findBook(index, isbn):
	if isbn in index:
		return index[isbn]
	else:
		return ''

def listBooks(index):
	lst = []
	c = 1
	for i in index:
		lst.append("%s) %s: %s" % (c, i, index[i]))
		c += 1
	return lst

def formatMenu():
	return ["What would you like to do?", "[r] Record a Book", "[f] Find a Book", "[l] List all Books", "[q] Quit"]

def formatMenuPrompt():
	return "Enter an option: "

def getUserChoice(string):
	while True:
		string = input(string).strip()
		if len(string) > 0:
			break
		else:
			pass
	return string

def getISBN():
	number = getUserChoice("Enter an ISBN Number: ")
	return number

def getTitle():
	title = getUserChoice("Enter a book title: ")
	return title

def recordBookAction(index):
	isbn = getISBN()
	title = getTitle()
	recordBook(index, isbn, title)

def findBookAction(index):
	isbn = getISBN()
	try:
		print(index[isbn])
	except:
		print("That ISBN does not exist.")

def listBooksAction(index):
	lst = listBooks(index)
	for i in lst:
		print(i)

def quitAction(index):
	print("The program will now close.")
	sys.exit(0)

def applyAction(index, choice):
	actions = {
		"r": recordBookAction,
		"f": findBookAction,
		"l": listBooksAction,
		"q": quitAction,
	}

	if choice not in actions:
		print("That is not a valid option.")
	else:
		actions[choice](index)

def main():
	index = {}
	
	while True:
		for i in formatMenu():
			print(i)
		choice = input(formatMenuPrompt())
		applyAction(index, choice)
		print()
		print()

if __name__ == '__main__':
	main()