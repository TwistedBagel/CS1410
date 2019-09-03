class Marker:

	def __init__(self, color):
		self.color = color
		self.ink = 10
		self.tip_size = .01
		self.erasable = True

blue_marker = Marker('blue')
green_marker = Marker('green')