import pygame

from constants import load_images
import random

class Bird:
    """
    This class represent the main flappy bird
    """
    MAX_ROTATION = 25
    IMGS = []
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
        """
        Create the object with params x(int) and y(int)
        """
        self.IMGS = load_images(random.randint(1, 6))
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        """
        Method to jump up
        """
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        """
        Method to move the bird
        """
        self.tick_count += 1

        # for downward acceleration
        displacement = self.vel * (self.tick_count) + 0.5 * (3) * (self.tick_count) ** 2  # calculate displacement

        # terminal velocity
        if displacement >= 16:
            displacement = (displacement / abs(displacement)) * 16

        if displacement < 0:
            displacement -= 2

        self.y = self.y + displacement

        if displacement < 0 or self.y < self.height + 50:  # tilt up
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:  # tilt down
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    def draw(self, win):
        """
        Method to draw the bird
        """
        self.img_count += 1

        if self.img_count <= self.ANIMATION_TIME:
            self.img = self.IMGS[0]
        elif self.img_count <= self.ANIMATION_TIME * 2:
            self.img = self.IMGS[1]
        elif self.img_count <= self.ANIMATION_TIME * 3:
            self.img = self.IMGS[2]
        elif self.img_count <= self.ANIMATION_TIME * 4:
            self.img = self.IMGS[1]
        elif self.img_count == self.ANIMATION_TIME * 4 + 1:
            self.img = self.IMGS[0]
            self.img_count = 0

        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME * 2

        from util import displayRotateCenter
        displayRotateCenter(win, self.img, (self.x, self.y), self.tilt)

    def get_mask(self):
        """
        get the mask of the bird
        """
        return pygame.mask.from_surface(self.img)
