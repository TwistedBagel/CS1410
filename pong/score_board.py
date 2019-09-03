import pygame
from text import Text

class ScoreBoard:

	def __init__(self, x, y, width, height):
		self.mX = x
		self.mY = y
		self.mWidth = width
		self.mHeight = height
		self.mLeftScore = 0
		self.mRightScore = 0
		self.mServeStatus = 1

	def getX(self):
		return self.mX

	def getY(self):
		return self.mY

	def getWidth(self):
		return self.mWidth

	def getHeight(self):
		return self.mHeight

	def getLeftScore(self):
		return self.mLeftScore

	def getRightScore(self):
		return self.mRightScore

	def getServeStatus(self):
		return self.mServeStatus

	def isGameOver(self):
		if self.mServeStatus == 3 or self.mServeStatus == 4:
			return True
		else:
			return False

	def scoreLeft(self):
		if not self.isGameOver():
			self.mLeftScore += 1
			if self.mLeftScore == 9:
				self.mServeStatus = 3

	def scoreRight(self):
		if not self.isGameOver():
			self.mRightScore += 1
			if self.mRightScore == 9:
				self.mServeStatus = 4

	def swapServe(self):
		if not self.isGameOver():
			if self.mServeStatus == 1:
				self.mServeStatus = 2
			elif self.mServeStatus == 2:
				self.mServeStatus = 1

	def draw(self, surface):
		string = "Left: %s || Right: %s" % (self.mLeftScore, self.mRightScore)
		t = Text(string, self.mX, self.mY)