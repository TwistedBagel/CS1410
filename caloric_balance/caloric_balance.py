class CaloricBalance:

	def __init__(self, gender, age, height, weight):
		self.gender = gender
		self.age = age
		self.height = height
		self.weight = weight
		self.balance = -self.getBMR(self.gender, self.age, self.height, self.weight)

	def getBMR(self, gender, age, height, weight):
		if gender == "f":
			return 655 + (4.7 * height) + (4.35 * weight) - (4.7 * age)
		elif gender == 'm':
			return 66 + (12.7 * height) + (6.23 * weight) - (6.8 * age)
		else:
			return 0.0

	def getBalance(self):
		return self.balance

	def recordActivity(self, caloric_burn, minutes):
		perMinute = caloric_burn * self.weight
		totalBurn = perMinute * minutes
		self.balance -= totalBurn

	def eatFood(self, calories):
		self.balance += calories