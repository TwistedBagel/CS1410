import datetime
import sys

def milesPerGallon(miles, gallons):
	try:
		return miles / gallons
	except:
		return 0.0

def createNotebook():
	return []

def recordTrip(notebook, date, miles, gallons):
	tripDict = {'date': date, 'miles': miles, 'gallons': gallons}
	notebook.append(tripDict)

def listTrips(notebook):
	fancy = []
	for dct in notebook:
		fancyItem = "On {0}: {1} miles traveled using {2} gallons. Gas mileage: {3} MPG".format(
			dct['date'], dct['miles'], dct['gallons'], milesPerGallon(dct['miles'], dct['gallons'])
			)
		fancy.append(fancyItem)
	return fancy

def calculateMPG(notebook):
	gallons = []
	miles = []
	for i in notebook:
		gallons.append(i['gallons'])
		miles.append(i['miles'])
	return milesPerGallon(sum(miles), sum(gallons))

def formatMenu():
	return ['What would you like to do?', '[r] Record Gas Consumption', '[l] List Mileage History', '[c] Calculate Gas Mileage', '[q] Quit']

def formatMenuPrompt():
	return "Enter an option: "

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

def getDate():
	date = getUserString("Enter a date: ")
	return date

def getMiles():
	miles = getUserFloat("What is your miles? ")
	return miles

def getGallons():
	gallons = getUserFloat("What is your gallons? ")
	return gallons

def recordTripAction(notebook):
	date = getDate()
	miles = getMiles()
	gallons = getGallons()

	dct = {"date": date, "miles": miles, "gallons": gallons}
	notebook.append(dct)
	print("Trip was saved")

def listTripsAction(notebook):
	if len(notebook) == 0:
		print("You need to record stuff first!")
	else:
		trips = listTrips(notebook)
		for i in trips:
			print(i)

def calculateMPGAction(notebook):
	if len(notebook) == 0:
		print("You need to record stuff first!")
	else:
		trips = calculateMPG(notebook)
		print("Average mpg is: %s" % trips)

def quitAction(notebook):
	print("Program is closing down")
	sys.exit(0)

def applyAction(notebook, action):
	choices = {
		"r": recordTripAction,
		"l": listTripsAction,
		"c": calculateMPGAction,
		"q": quitAction,
	}

	if action not in choices:
		print("I'm sorry, that is not a valid option!")
	else:
		choices[action](notebook)

def main():
	notebook = []

	while True:

		for i in formatMenu():
			print(i)

		action = input("Enter an option ")
		applyAction(notebook, action)
		print()

if __name__ == "__main__":
	main()