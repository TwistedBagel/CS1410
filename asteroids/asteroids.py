from ship import Ship
from rock import Rock
from star import Star
import random

class Asteroids:

	def __init__(self, width, height):
		self.width = width
		self.height = height

		self.ship = Ship(width / 2, height / 2, width, height)
		self.rocks = []
		self.bullets = []
		self.stars = []

		for i in range(10):
			x = random.uniform(0, width)
			y = random.uniform(0, height)
			rock = Rock(x, y, width, height)
			self.rocks.append(rock)

		for i in range(20):
			x = random.uniform(0, width)
			y = random.uniform(0, height)
			star = Star(x, y, width, height)
			self.stars.append(star)

		self.objects = self.getBullets() + self.getStars() + self.getRocks() + [self.getShip()]

	def getWorldWidth(self):
		return self.width

	def getWorldHeight(self):
		return self.height

	def getShip(self):
		return self.ship

	def getRocks(self):
		return self.rocks

	def getObjects(self):
		return self.objects

	def getBullets(self):
		return self.bullets

	def getStars(self):
		return self.stars

	def newRocks(self):
		coin = random.randint(0, 10000)
		if coin >= 9900 and len(self.rocks) < 10:
			x = random.uniform(0, self.width)
			y = random.uniform(0, self.height)
			rock = Rock(x, y, self.width, self.height)

			if self.getShip().hits(rock):
				self.newRocks()
			else:
				self.rocks.append(rock)

	def turnShipLeft(self, delta_rotation):
		self.getShip().rotate(-delta_rotation)

	def turnShipRight(self, dr):
		self.getShip().rotate(dr)

	def accelerateShip(self, dv):
		self.getShip().accelerate(dv)

	def evolveAllObjects(self, dt):
		for i in self.getObjects():
			i.evolve(dt)

	def collideShipAndBullets(self):
		for b in self.getBullets():
			self.getShip().hits(b)

	def collideShipAndRocks(self):
		for r in self.getRocks():
			self.getShip().hits(r)

	def collideRocksAndBullets(self):
		for r in self.getRocks():
			for b in self.getBullets():
				b.hits(r)

	def removeInactiveObjects(self):
		rocks = []
		for r in self.getRocks():
			if r.getActive():
				rocks.append(r)
		self.rocks = rocks

		bullets = []
		for b in self.getBullets():
			if b.getActive():
				bullets.append(b)
		self.bullets = bullets

		ship = []
		if self.getShip().getActive():
			ship.append(self.getShip())

		self.objects = self.getBullets() + self.getStars() + self.getRocks() + [self.getShip()]

	def evolve(self, dt):
		# self.newRocks()
		self.evolveAllObjects(dt)
		self.collideShipAndBullets()
		self.collideRocksAndBullets()
		self.collideShipAndRocks()
		self.removeInactiveObjects()

	def fire(self):
		if len(self.getBullets()) < 3 and self.getShip().getActive():
			b = self.getShip().fire()
			self.bullets.append(b)

	def superFire(self):
		if self.getShip().getActive():
			b = self.getShip().fire()
			self.bullets.append(b)

	def draw(self, surface):
		surface.fill((0, 0, 0))
		for i in self.getObjects():
			if i.getActive():
				i.draw(surface)