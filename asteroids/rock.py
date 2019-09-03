from polygon import Polygon
import random
import math

class Rock(Polygon):

	def __init__(self, x, y, world_width, world_height):
		rotation = random.uniform(0.0, 359.9)
		Polygon.__init__(self, x, y, 0, 0, rotation, world_width, world_height)
		radius = random.uniform(20, 30)
		points = random.randint(5, 10)
		outline = self.createRandomPolygon(radius, points)
		self.setPolygon(outline)
		self.mSpinRate = random.uniform(-90, 90)
		dv = random.uniform(10, 20)
		self.accelerate(dv)
		self.setColor((0, 0, 255))

	def createRandomPolygon(self, radius, numPoints):
		outline = []
		for i in range(numPoints):
			degrees = i * 360 / numPoints
			angle = math.radians(degrees)
			distance = radius * random.uniform(0.7, 1.3)
			x = math.cos(angle) * distance
			y = math.sin(angle) * distance
			point = (x, y)
			outline.append(point)
		return outline

	def getSpinRate(self):
		return self.mSpinRate

	def setSpinRate(self, spinRate):
		self.mSpinRate = spinRate

	def evolve(self, dt):
		self.rotate(self.mSpinRate * dt)
		self.move(dt)