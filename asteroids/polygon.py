from rotatable import Rotatable
import pygame
import math

class Polygon(Rotatable):

	def __init__(self, x, y, dx, dy, rotation, world_width, world_height):
		Rotatable.__init__(self, x, y, dx, dy, rotation, world_width, world_height)
		self.__polygon = []
		self.__color = (255, 255, 255)

	def getPolygon(self):
		return self.__polygon

	def getColor(self):
		return self.__color

	def setPolygon(self, polygon):
		self.__polygon = polygon

	def setColor(self, color):
		self.__color = color

	def draw(self, surface):
		pointList = self.rotateAndTranslatePointList(self.getPolygon())
		pygame.draw.polygon(surface, self.getColor(), pointList)
		#pygame.draw.circle(surface, (255, 255, 0), (int(self.getX()), int(self.getY())), int(self.getRadius()), 1)

	def getRadius(self):
		if len(self.getPolygon()) == 0:
			return 0
		else:
			total = 0
			for x, y in self.getPolygon():
				# print("------------origin is %s and point is %s" % ((self.mX, self.mY), (i[0], i[1])))
				total += math.sqrt(x**2 + y**2)

			# print("############## dists says: %s" % (dists))

			avg = total / len(self.getPolygon())
			return avg