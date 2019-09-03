from rotatable import Rotatable
import pygame

class Circle(Rotatable):

	def __init__(self, x, y, dx, dy, rotation, radius, world_width, world_height):
		Rotatable.__init__(self, x, y, dx, dy, rotation, world_width, world_height)
		self.mRadius = radius
		self.mColor = (255, 0, 0)

	def getRadius(self):
		return self.mRadius

	def getColor(self):
		return self.mColor

	def setRadius(self, new):
		if new >= 1:
			self.mRadius = new
		else:
			return

	def setColor(self, new):
		self.mColor = new

	def draw(self, surface):
		pygame.draw.circle(surface, self.mColor, (int(self.mX), int(self.mY)), int(self.mRadius), 0)