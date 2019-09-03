import pygame
import cloud
import mountain

class Sky:

	def __init__(self, x, y, width, height, color):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.skyHeight = self.height//3 * 2
		self.color = color
		self.mCloud = cloud.Cloud(width, height, 10)
		self.sunColor = (255, 255, 0)
		self.mountainColor = (59, 47, 71)
		self.mMountainList = [
			mountain.Mountain([[0, self.skyHeight], [100, self.height//3], [200, self.skyHeight]], 0, self.mountainColor),
			mountain.Mountain([[150, self.skyHeight], [250, self.height//2], [350, self.skyHeight]], 0, self.mountainColor),
		]

	def draw(self, surface):
		rect = pygame.Rect(0, 0, self.width, self.skyHeight)
		pygame.draw.rect(surface, self.color, rect)
		pygame.draw.circle(surface, self.sunColor, (self.width - 100, 100), 30, 0)
		self.mCloud.draw(surface)

		for m in self.mMountainList:
			m.draw(surface)