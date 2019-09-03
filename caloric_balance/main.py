from caloric_balance import CaloricBalance
import sys

def formatMenu():
	return ['What would you like to do?', '[f] Record Food Consumption', '[a] Record Physical Activity', '[q] Quit']

def formatMenuPrompt():
	return "Enter an option: "

def formatActivityMenu():
	return ['Choose an activity to record', '[j] Jump rope', '[r] Running', '[s] Sitting', '[w] Walking']

def getUserString(string):
	while True:
		string = input(string).strip()
		if len(string) > 0:
			break
		else:
			pass
	return string

def getUserFloat(num):
	while True:
		num = input(num).strip()
		try:
			num = float(num)
			if num <= 0:
				pass
			else:
				break
		except:
			print("you can't convert that string to a float")
	return num

def createCaloricBalance():
	gender = getUserString("M or F? ")
	age = getUserFloat("Age? ")
	height = getUserFloat("Height in inches? ")
	weight = getUserFloat("Weight in pounds? ")
	return CaloricBalance(gender, age, height, weight)

def recordActivityAction(cb):
	for i in formatActivityMenu():
		print(i)

	choice = getUserString("Enter an option: ")
	activity = 0

	if choice == "j":
		# possible options are .074, .08, .089
		activity = .08
	elif choice == "r":
		# options are .115, .095, .087
		activity = .095
	elif choice == "s":
		# options are .009
		activity = .009
	elif choice == "w":
		# options are .065, .036, .037
		activity = .036
	else:
		print("That is not a valid option")
		return
	time = getUserFloat("How long? ")
	cb.recordActivity(activity, time)
	print("Good job! Your new caloric balance is {0}".format(cb.getBalance()))

def eatFoodAction(cb):
	consumed = getUserFloat("How many calories did you consume? ")
	cb.eatFood(consumed)
	print("Success! Your new caloric balance is {0}".format(cb.getBalance()))

def quitAction(cb):
	print("The program is now terminating.")
	sys.exit(0)

def applyAction(cb, choice):
	choices = {
	'f': eatFoodAction,
	'a': recordActivityAction,
	'q': quitAction,
	}

	if choice not in choices:
		print("I'm sorry, that is not a valid option")
	else:
		choices[choice.lower()](cb)

def main():
	cb = createCaloricBalance()

	while True:

		for i in formatMenu():
			print(i)

		action = input("Enter an option ")
		applyAction(cb, action)
		print()

if __name__ == '__main__':
	main()