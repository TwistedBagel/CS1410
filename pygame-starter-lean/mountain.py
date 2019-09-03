import pygame

class Mountain:

	def __init__(self, point_list, thickness, color):
		self.points = point_list
		self.color = color
		self.thickness = thickness

	def draw(self, surface):
		pygame.draw.polygon(surface, self.color, self.points, self.thickness)