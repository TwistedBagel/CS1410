from classes import Battery

class Energy(Battery):

	def only(self):
		print("energy only")

energy = Energy(10, True)
print(energy.capacity)
print(energy.rechargeable)
energy.only()