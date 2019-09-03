import movable
import math

class Rotatable(movable.Movable):

	def __init__(self, x, y, dx, dy, rotation, world_width, world_height):
		movable.Movable.__init__(self, x, y, dx, dy, world_width, world_height)
		self.rotation = rotation

	def getRotation(self):
		return self.rotation

	def rotate(self, delta_rotation):
		self.rotation += delta_rotation
		
		self.rotation %= 360

	def splitDeltaVIntoXAndY(self, rotation, dv):
		theta = math.radians(rotation)

		x = math.cos(theta) * dv
		y = math.sin(theta) * dv

		return (x, y)

	def accelerate(self, dv):
		dx, dy = self.splitDeltaVIntoXAndY(self.getRotation(), dv)

		dx += self.getDX()
		dy += self.getDY()

		self.mDX = dx
		self.mDY = dy

	def rotatePoint(self, x, y):
		theta0 = math.atan2(y, x)
		theta1 = math.radians(self.getRotation())
		theta = theta0 + theta1
		distance = math.sqrt(x ** 2 + y ** 2)
		rx = math.cos(theta) * distance
		ry = math.sin(theta) * distance
		return rx, ry

	def translatePoint(self, x, y):
		x += self.mX
		y += self.mY
		return x, y

	def rotateAndTranslatePoint(self, x, y):
		rx, ry = self.rotatePoint(x, y)
		tx, ty = self.translatePoint(rx, ry)
		return tx, ty

	def rotateAndTranslatePointList(self, pointList):
		outline = []

		for x, y in pointList:
			point = self.rotateAndTranslatePoint(x, y)
			outline.append(point)

		return outline

if __name__ == "__main__":
	test()