import pygame

class Paddle:

	def __init__(self, x,y,width,height,speed,min_y,max_y):
		self.mX = x
		self.mY = y
		self.mWidth = width
		self.mHeight = height
		self.mSpeed = speed
		self.mMinY = min_y
		self.mMaxY = max_y

	def getX(self):
		return self.mX

	def getY(self):
		return self.mY

	def getWidth(self):
		return self.mWidth

	def getHeight(self):
		return self.mHeight

	def getSpeed(self):
		return self.mSpeed

	def getMinY(self):
		return self.mMinY

	def getMaxY(self):
		return self.mMaxY

	def getRightX(self):
		return self.mX + self.mWidth

	def getBottomY(self):
		return self.mY + self.mHeight

	def setPosition(self, y):
		if y >= self.mMinY and (y + self.mHeight) <= self.mMaxY:
			self.mY = y

	def moveUp(self, dt):
		newY = self.mY - self.mSpeed * dt
		if newY >= self.mMinY:
			self.mY = newY
		elif newY == self.mMinY:
			self.mY = self.mMinY

	def moveDown(self, dt):
		newY = self.mY + self.mSpeed * dt
		if (newY + self.mHeight) <= self.mMaxY:
			self.mY = newY
		elif (newY + self.mHeight) == self.mMaxY:
			self.mY = self.mMaxY - self.mHeight

	def draw(self, surface):
		pygame.draw.rect(surface, (255, 0, 0), (self.mX, self.mY, self.mWidth, self.mHeight), 0)