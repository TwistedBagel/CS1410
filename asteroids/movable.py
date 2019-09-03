import math

class Movable():

	def __init__(self, x, y, dX, dY, worldWidth, worldHeight):
		self.mX = x
		self.mY = y
		self.mDX = dX
		self.mDY = dY
		self.mWorldWidth = worldWidth
		self.mWorldHeight = worldHeight
		self.mActive = True

	def getX(self):
		return self.mX

	def getY(self):
		return self.mY

	def getDX(self):
		return self.mDX

	def getDY(self):
		return self.mDY

	def getWorldWidth(self):
		return self.mWorldWidth

	def getWorldHeight(self):
		return self.mWorldHeight

	def getActive(self):
		return self.mActive

	def setActive(self, active):
		self.mActive = active

	def hits(self, other):
		if not self.getActive() or not other.getActive():
			return False

		x1, y1, r1 = self.getX(), self.getY(), self.getRadius()
		x2, y2, r2 = other.getX(), other.getY(), other.getRadius()

		ad = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
		md = r1 + r2

		if ad <= md:
			self.setActive(False)
			other.setActive(False)
			return True

		return False

	def getRadius(self):
		raise NotImplementedError

	def move(self, dt):
		self.mX += self.mDX * dt
		self.mY += self.mDY * dt

		self.mX %= self.mWorldWidth
		self.mY %= self.mWorldHeight

	def accelerate(self, delta_velocity):
		raise NotImplementedError

	def evolve(self, dt):
		raise NotImplementedError

	def draw(self, surface):
		raise NotImplementedError