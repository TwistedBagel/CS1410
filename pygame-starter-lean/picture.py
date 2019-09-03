import pygame
import boat
import cloud
import sky

class Picture:
    def __init__(self, width, height):
        self.mWidth = width
        self.mHeight = height

        self.skycolor = (0, 230, 255)
        self.mastColor = (222, 184, 135)

        self.mBoat = boat.Boat(width, height, self.skycolor)
        self.mSky = sky.Sky(0, 0, width, height, self.skycolor)

    # move the circles down every frame according to how much time has passed
    # don't let the circles go off the window
    def evolve(self, dt):
        return

    # draws the current state of the system
    def draw(self, surface):
        self.mBoat.draw(surface)
        self.mSky.draw(surface)
        pygame.draw.arc(surface, (0, 0, 0), (50, 50, 100, 50), 10, 13, 2)
        rect = pygame.Rect(self.mWidth//2, self.mHeight//4, 40, 250)
        pygame.draw.rect(surface, self.mastColor, rect)
        return