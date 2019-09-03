import random
import pygame

class Ball:

	def __init__(self, size, minX, maxX, minY, maxY, leftPaddleX, rightPaddleX):
		self.mX = minX
		self.mY = minY

		self.mSize = size

		self.mDX = 0
		self.mDY = 0

		self.mMinX = 100
		self.mMaxX = 900
		self.mMinY = 200
		self.mMaxY = 800

		self.mLeftPaddleX = leftPaddleX
		self.mLeftPaddleMinY = minY
		self.mLeftPaddleMaxY = maxY

		self.mRightPaddleX = rightPaddleX
		self.mRightPaddleMinY = minY
		self.mRightPaddleMaxY = maxY

	def getX(self):
		return self.mX

	def getY(self):
		return self.mY

	def getSize(self):
		return self.mSize

	def getDX(self):
		return self.mDX

	def getDY(self):
		return self.mDY

	def getMinX(self):
		return self.mMinX

	def getMaxX(self):
		return self.mMaxX

	def getMinY(self):
		return self.mMinY

	def getMaxY(self):
		return self.mMaxY

	def getLeftPaddleX(self):
		return self.mLeftPaddleX

	def getLeftPaddleMinY(self):
		return self.mLeftPaddleMinY

	def getLeftPaddleMaxY(self):
		return self.mLeftPaddleMaxY

	def getRightPaddleX(self):
		return self.mRightPaddleX

	def getRightPaddleMinY(self):
		return self.mRightPaddleMinY

	def getRightPaddleMaxY(self):
		return self.mRightPaddleMaxY

	def setPosition(self, x, y):
		if x > self.mMinX and x + self.mSize < self.mMaxX and y > self.mMinY and y + self.mSize < self.mMaxY:
			self.mX = x
			self.mY = y

	def setSpeed(self, dx, dy):
		self.mDX = dx
		self.mDY = dy

	def setLeftPaddleY(self, paddleMinY, paddleMaxY):
		if paddleMinY >= self.mMinY and paddleMaxY <= self.mMaxY and paddleMinY < paddleMaxY:
			self.mLeftPaddleMinY = paddleMinY
			self.mLeftPaddleMaxY = paddleMaxY

	def setRightPaddleY(self, paddleMinY, paddleMaxY):
		if paddleMinY >= self.mMinY and paddleMaxY <= self.mMaxY and paddleMinY < paddleMaxY:
			self.mRightPaddleMinY = paddleMinY
			self.mRightPaddleMaxY = paddleMaxY

	def checkTop(self, y):
		if y < self.mMinY:
			self.mDY = -self.mDY
			return ((self.mMinY - y) + self.mMinY)
		else:
			return y

	def checkBottom(self, y):
		if y + self.mSize > self.mMaxY:
			self.mDY = -self.mDY
			return ((self.mMaxY - y) + self.mMaxY) - self.mSize - self.mSize
		else:
			return y

	def checkLeft(self, x):
		if x < self.mMinX:
			self.mDX = 0
			self.mDY = 0
			return self.mMinX
		else:
			return x

	def checkRight(self, x):
		if x + self.mSize > self.mMaxX:
			self.mDX = 0
			self.mDY = 0
			return (self.mMaxX - self.mSize)
		else:
			return x

	def checkLeftPaddle(self, newX, newY):
		mid_y = (newY + self.mY) / 2
		if mid_y >= self.mLeftPaddleMinY and mid_y <= self.mLeftPaddleMaxY and newX <= self.mLeftPaddleX and self.mX >= self.mLeftPaddleX:
			dx = self.mLeftPaddleX - newX
			new_x = self.mLeftPaddleX + dx
			self.mDX = -self.mDX
			return new_x
		else:
			return newX
	
	def checkRightPaddle(self, newX, newY):
		midY = ((newY + self.mY + self.mSize) / 2)
		if midY >= self.mRightPaddleMinY and midY <= self.mRightPaddleMaxY and (newX + self.mSize) <= self.mRightPaddleX and (self.mX + self.mSize) >= self.mRightPaddleX:
			dx = self.mRightPaddleX - (newX + self.mSize)
			new_x = self.mRightPaddleX + dx
			self.mDX = -self.mDX
			print("****************************this was executed************************")
			return new_x			
		else:
			return newX

	def move(self, dt):
		new_x = self.mX + self.mDX * dt
		new_y = self.mY + self.mDY * dt

		new_y = self.checkTop(new_y)
		new_y = self.checkBottom(new_y)
		new_x = self.checkLeft(new_x)
		new_x = self.checkRight(new_x)
		new_x = self.checkLeftPaddle(new_x, new_y)
		new_x = self.checkRightPaddle(new_x, new_y)

		self.mX = new_x
		self.mY = new_y
		# self.mX = 100
		# self.mY = 100

	def serveLeft(self, x, minY, maxY, minDX, maxDX, minDY, maxDY):
		self.mX = x
		self.mY = random.uniform(minY, maxY)
		self.mDX = random.uniform(minDX, maxDX)
		self.mDY = random.uniform(minDY, maxDY)

	def serveRight(self, x, minY, maxY, minDX, maxDX, minDY, maxDY):
		self.mX = x
		self.mY = random.uniform(minY, maxY)
		self.mDX = random.uniform(-minDX, -maxDX)
		self.mDY = random.uniform(minDY, maxDY)

	def draw(self, surface):
		pygame.draw.rect(surface, (255, 255, 255), (self.mX, self.mY, self.mSize, self.mSize), 0)