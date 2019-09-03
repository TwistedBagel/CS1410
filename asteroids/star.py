from circle import Circle
import random

class Star(Circle):

	def __init__(self, x, y, width, height):
		Circle.__init__(self, x, y, 0, 0, 0, 2, width, height)
		self.mBrightness = random.randint(0, 255)

	def getBrightness(self):
		return self.mBrightness

	def setBrightness(self, new):
		if new >= 0 and new <= 255:
			self.mBrightness = new
			color = (new, new, new)
			self.setColor(color)

	def evolve(self, dt):
		change = random.choice([10, -10, 0])
		newBright = self.getBrightness() + change
		self.setBrightness(newBright)