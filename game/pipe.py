import random

import pygame

from constants import pipe_img


class Pipe:
    """
    represents a pipe object
    """
    GAP = 200
    VEL = 5

    def __init__(self, x):
        """
        creating main object with parameters: x(int) and y(int), returns none.
        """
        self.x = x
        self.height = 0

        # set derfault values for the top and bottom of the pipe
        self.top = 0
        self.bottom = 0

        self.PIPE_TOP = pygame.transform.flip(pipe_img, False, True)
        self.PIPE_BOTTOM = pipe_img
        self.passed = False
        self.set_height()

    def set_height(self):
        """
        settin height of pipe according the distance from the top of screen
        """
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP

    def collide(self, bird, win):
        """
        This method returns  if a point is colliding with the pipe
        """
        bird_mask = bird.get_mask()

        top = pygame.mask.from_surface(self.PIPE_TOP)

        bottom = pygame.mask.from_surface(self.PIPE_BOTTOM)

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        """
        Check if bird hit pipe
        """
        point_bottom = bird_mask.overlap(bottom, bottom_offset)
        point_top = bird_mask.overlap(top, top_offset)

        if point_bottom or point_top:
            return True

        return False

    def move(self):
        """
        method to move pipe based on vel
        """
        self.x -= self.VEL

    def draw(self, win):
        """
        method to draw  the top and bottom of the pipe.
        the method takes win as argument( pygame window/surface)
        """
        # draw top
        win.blit(self.PIPE_TOP, (self.x, self.top))
        # draw bottom
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))
