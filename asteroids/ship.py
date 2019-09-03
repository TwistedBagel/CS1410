from polygon import Polygon
from bullet import Bullet

class Ship(Polygon):

	def __init__(self, x, y, width, height):

		Polygon.__init__(self, x, y, 0, 0, 0, width, height)
		outline = [(10, 0), (-10, -10), (-5, 0), (-10, 10)]
		self.setPolygon(outline)
		self.setColor((0, 255, 0))

	def evolve(self, dt):
		self.move(dt)

	def fire(self):
		px, py = self.getPolygon()[0]
		x, y, = self.rotateAndTranslatePoint(px, py)
		dx, dy = 0, 0
		rotation = self.getRotation()
		width = self.getWorldWidth()
		height = self.getWorldHeight()
		b = Bullet(x, y, dx, dy, rotation, width, height)
		# b.setDX(b.getDX() + self.getDX())
		# b.setDY(b.getDY() + self.getDY())
		return b