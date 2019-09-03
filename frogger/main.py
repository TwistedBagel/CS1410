import pygame
import game
import froggerlib
import random
import sys
from config import *

class PygameApp(game.Game):

	def __init__(self):
		game.Game.__init__(self, 'Frogger', SCREEN_WIDTH, SCREEN_HEIGHT, FRAME_RATE)

		self.stage1 = froggerlib.Stage(0, 10 * VG, SCREEN_WIDTH, VG)
		self.stage2 = froggerlib.Stage(0, 5 * VG, SCREEN_WIDTH, VG)
		self.road = froggerlib.Road(0, 6 * VG, SCREEN_WIDTH, 4 * VG)
		self.water = froggerlib.Water(0, VG, SCREEN_WIDTH, 4 * VG)
		self.frog = None

		self.homes = [
			froggerlib.Home(0, 0, VG, VG),
			froggerlib.Home(3 * VG, 0, VG, VG),
			froggerlib.Home(6 * VG, 0, VG, VG),
			froggerlib.Home(9 * VG, 0, VG, VG),
			froggerlib.Home(12 * VG, 0, VG, VG),
		]

		self.grasses = [
			froggerlib.Grass(VG, 0, VG * 2, VG),
			froggerlib.Grass(VG * 4, 0, VG * 2, VG),
			froggerlib.Grass(VG * 7, 0, VG * 2, VG),
			froggerlib.Grass(VG * 10, 0, VG * 2, VG),
		]

		self.restart()

		y = 9 * VG + PADDING
		x = 8 * VG + PADDING

		# The x and y values for the third and fourth row of cars
		# What the fuck is even going on here
		y2 = 7 * VG + PADDING
		x2 = 6 * VG + PADDING

		self.cars = [
			# First row of cars
			froggerlib.Car(0, y, CAR_WIDTH, FROG_SIZE, SCREEN_WIDTH, y, 4),
			froggerlib.Car(SCREEN_WIDTH//4 * 3, y, CAR_WIDTH, FROG_SIZE, SCREEN_WIDTH, y, 4),
			froggerlib.Car(SCREEN_WIDTH//4 * 2, y, CAR_WIDTH, FROG_SIZE, SCREEN_WIDTH, y, 4),
			froggerlib.Car(SCREEN_WIDTH//4, y, CAR_WIDTH, FROG_SIZE, SCREEN_WIDTH, y, 4),

			# Third row of cars
			froggerlib.Car(0, y2, CAR_WIDTH, FROG_SIZE, SCREEN_WIDTH, y2, 4),
			froggerlib.Car(SCREEN_WIDTH//4 * 3, y2, CAR_WIDTH, FROG_SIZE, SCREEN_WIDTH, y2, 4),
			froggerlib.Car(SCREEN_WIDTH//4 * 2, y2, CAR_WIDTH, FROG_SIZE, SCREEN_WIDTH, y2, 4),
			froggerlib.Car(SCREEN_WIDTH//4, y2, CAR_WIDTH, FROG_SIZE, SCREEN_WIDTH, y2, 4),
		]

		self.dozers = [
			# Second row of cars
			froggerlib.Dozer(SCREEN_WIDTH, x, CAR_WIDTH, FROG_SIZE, 0 - CAR_WIDTH, x, 2),
			froggerlib.Dozer(SCREEN_WIDTH//4 * 3, x, CAR_WIDTH, FROG_SIZE, 0 - CAR_WIDTH, x, 2),
			froggerlib.Dozer(SCREEN_WIDTH//4 * 2, x, CAR_WIDTH, FROG_SIZE, 0 - CAR_WIDTH, x, 2),
			froggerlib.Dozer(SCREEN_WIDTH//4, x, CAR_WIDTH, FROG_SIZE, 0 - CAR_WIDTH, x, 2),

			# Fourth row of cars
			froggerlib.Dozer(SCREEN_WIDTH, x2, CAR_WIDTH, FROG_SIZE, 0 - CAR_WIDTH, x2, 2),
			froggerlib.Dozer(SCREEN_WIDTH//4 * 3, x2, CAR_WIDTH, FROG_SIZE, 0 - CAR_WIDTH, x2, 2),
			froggerlib.Dozer(SCREEN_WIDTH//4 * 2, x2, CAR_WIDTH, FROG_SIZE, 0 - CAR_WIDTH, x2, 2),
			froggerlib.Dozer(SCREEN_WIDTH//4, x2, CAR_WIDTH, FROG_SIZE, 0 - CAR_WIDTH, x2, 2),
		]

		# x and y values for logs
		x = 4 * VG + PADDING
		y = 3 * VG + PADDING
		x2 = 2 * VG + PADDING
		y2 = VG + PADDING

		self.logs = [
			# First row of logs
			froggerlib.Log(0, x, CAR_WIDTH, FROG_SIZE, SCREEN_WIDTH, x, 5),
			froggerlib.Log(SCREEN_WIDTH//4 * 3, x, CAR_WIDTH, FROG_SIZE, SCREEN_WIDTH, x, 5),
			froggerlib.Log(SCREEN_WIDTH//4 * 2, x, CAR_WIDTH, FROG_SIZE, SCREEN_WIDTH, x, 5),
			froggerlib.Log(SCREEN_WIDTH//4, x, CAR_WIDTH, FROG_SIZE, SCREEN_WIDTH, x, 5),

			# Third row of logs
			froggerlib.Log(0, x2, CAR_WIDTH, FROG_SIZE, SCREEN_WIDTH, x2, 5),
			froggerlib.Log(SCREEN_WIDTH//4 * 3, x2, CAR_WIDTH, FROG_SIZE, SCREEN_WIDTH, x2, 5),
			froggerlib.Log(SCREEN_WIDTH//4 * 2, x2, CAR_WIDTH, FROG_SIZE, SCREEN_WIDTH, x2, 5),
			froggerlib.Log(SCREEN_WIDTH//4, x2, CAR_WIDTH, FROG_SIZE, SCREEN_WIDTH, x2, 5),
		]

		self.turtles = [
			# Second row of logs (jk its fucking turtles)
			froggerlib.Turtle(SCREEN_WIDTH, y, CAR_WIDTH, FROG_SIZE, 0 - CAR_WIDTH, y, 3),
			froggerlib.Turtle(SCREEN_WIDTH//4 * 3, y, CAR_WIDTH, FROG_SIZE, 0 - CAR_WIDTH, y, 3),
			froggerlib.Turtle(SCREEN_WIDTH//4 * 2, y, CAR_WIDTH, FROG_SIZE, 0 - CAR_WIDTH, y, 3),
			froggerlib.Turtle(SCREEN_WIDTH//4, y, CAR_WIDTH, FROG_SIZE, 0 - CAR_WIDTH, y, 3),

			# Fourth row of logs (fucking turtles again)
			froggerlib.Turtle(SCREEN_WIDTH, y2, CAR_WIDTH, FROG_SIZE, 0 - CAR_WIDTH, y2, 6),
			froggerlib.Turtle(SCREEN_WIDTH//4 * 3, y2, CAR_WIDTH, FROG_SIZE, 0 - CAR_WIDTH, y2, 6),
			froggerlib.Turtle(SCREEN_WIDTH//4 * 2, y2, CAR_WIDTH, FROG_SIZE, 0 - CAR_WIDTH, y2, 6),
			froggerlib.Turtle(SCREEN_WIDTH//4, y2, CAR_WIDTH, FROG_SIZE, 0 - CAR_WIDTH, y2, 6),
		]
		return

	def restart(self):
		x = COLS // 2 * HG + PADDING
		y = (ROWS - 1) * VG + PADDING

		# because i don't want to play the whole fucking thing just to test the water stages
		y2 = 5 * VG + PADDING
		
		self.frog = froggerlib.Frog(x, y, FROG_SIZE, FROG_SIZE, x, y, 8, HG, VG)

	def win(self):
		print("Congrats, you won this game")
		sys.exit(0)

	def dead(self):
		if self.frog.outOfBounds(SCREEN_WIDTH, SCREEN_HEIGHT):
			return True

		for c in self.cars:
			if c.hits(self.frog):
				return True

		for d in self.dozers:
			if d.hits(self.frog):
				return True

		for l in self.logs:
			l.supports(self.frog)

		for t in self.turtles:
			t.supports(self.frog)

		if self.water.hits(self.frog):
			return True

		for g in self.grasses:
			if g.hits(self.frog):
				return True

		for h in self.homes:
			if h.hits(self.frog):
				self.win()
				return True

		return False

	def game_logic(self, keys, newkeys, buttons, newbuttons, mouse_position, dt):
		if self.dead():
			if pygame.K_r in newkeys:
				self.restart()

			if pygame.K_q in newkeys:
				sys.exit(0)
			return

		x = mouse_position[0]
		y = mouse_position[1]

		if pygame.K_LEFT in newkeys:
			self.frog.left()

		if pygame.K_RIGHT in newkeys:
			self.frog.right()

		if pygame.K_UP in newkeys:
			self.frog.up()

		if pygame.K_DOWN in newkeys:
			self.frog.down()

		if pygame.K_q in newkeys:
			sys.exit(0)

		for c in self.cars:
			c.move()
			if c.atDesiredLocation():
				if c.getDesiredX() > 0:
					c.setX(0 - c.getWidth())
				else:
					c.setX(SCREEN_WIDTH)

		for d in self.dozers:
			d.move()
			if d.atDesiredLocation():
				if d.getDesiredX() > 0:
					d.setX(0 - d.getWidth())
				else:
					d.setX(SCREEN_WIDTH)

		for l in self.logs:
			l.move()
			if l.atDesiredLocation():
				if l.getDesiredX() > 0:
					l.setX(0 - l.getWidth())
				else:
					l.setX(SCREEN_WIDTH)

		for t in self.turtles:
			t.move()
			if t.atDesiredLocation():
				if t.getDesiredX() > 0:
					t.setX(0 - t.getWidth())
				else:
					t.setX(SCREEN_WIDTH)

		self.frog.move()

		return

	def px(self, x):
		return x * HG

	def py(self, y):
		return y * VG

	def draw_object(self, surface, obj, color):
		rect = pygame.Rect(
			obj.getX(),
			obj.getY(),
			obj.getWidth(),
			obj.getHeight()
		)
		pygame.draw.rect(surface, color, rect)

	def draw_stage(self, surface, stage):
		color = (255, 191, 250)
		self.draw_object(surface, stage, color)

	def draw_grass(self, surface, grass):
		color = (96, 128, 56)
		self.draw_object(surface, grass, color)

	def draw_homes(self, surface, home):
		color = (2, 185, 30)
		self.draw_object(surface, home, color)

	def draw_road(self, surface, road):
		color = (48, 48, 48)
		self.draw_object(surface, road, color)

	def draw_water(self, surface, water):
		color = (0, 191, 255)
		self.draw_object(surface, water, color)

	def draw_frog(self, surface):
		color = (0, 255, 0)
		self.draw_object(surface, self.frog, color)

	def draw_car(self, surface, car):
		color = (255, 0, 0)
		self.draw_object(surface, car, color)

	def draw_dozer(self, surface, dozer):
		color = (255, 204, 0)
		self.draw_object(surface, dozer, color)

	def draw_log(self, surface, log):
		color = (139, 69, 19)
		self.draw_object(surface, log, color)

	def draw_turtle(self, surface, turtle):
		color = (8, 185, 31)
		self.draw_object(surface, turtle, color)

	def draw_grid(self, surface):
		if not DEBUG:
			return

		for y in range(ROWS):
			for x in range(COLS):
				px = self.px(x)
				py = self.py(y)
				rect = pygame.Rect(px, py, HG, VG)
				pygame.draw.rect(surface, (255, 255, 0), rect, 1)

	def paint(self, surface):
		self.draw_stage(surface, self.stage1)
		self.draw_stage(surface, self.stage2)
		self.draw_road(surface, self.road)
		self.draw_water(surface, self.water)

		for c in self.cars:
			self.draw_car(surface, c)

		for d in self.dozers:
			self.draw_dozer(surface, d)

		for l in self.logs:
			self.draw_log(surface, l)

		for t in self.turtles:
			self.draw_turtle(surface, t)

		for g in self.grasses:
			self.draw_grass(surface, g)

		for h in self.homes:
			self.draw_homes(surface, h)

		self.draw_frog(surface)
		self.draw_grid(surface)
		return

def main():
	pygame.font.init()
	game = PygameApp()
	game.main_loop()

if __name__ == "__main__":
	main()