import pygame
import random

class Cloud:

	def __init__(self, width, height, amount):
		self.width = width
		self.height = height
		self.amount = amount
		self.minX = 0
		self.maxX = width
		self.minY = 0
		self.maxY = height // 2
		self.colors = [
			(220, 220, 220),
			(128, 128, 128),
			(255, 255, 255),
			(169, 169, 169),
			(112, 128, 144),
		]
		self.x = random.randrange(self.minX, self.maxX)
		self.y = random.randrange(self.minY, self.maxY)
		self.radius = random.randrange(20, 30)
		self.color = random.choice(self.colors)

	def draw(self, surface):
		pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius, 0)