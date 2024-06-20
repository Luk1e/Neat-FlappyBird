from constants import base_img


class Base:
    VELOCITY = 5
    WIDTH = base_img.get_width()
    IMG = base_img

    def __init__(self, y):
        """
        Create the object with params: y(int).
        """
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
        """
        method to move the floor
        """
        self.x2 -= self.VELOCITY
        self.x1 -= self.VELOCITY
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        """
        Method to draw the floor.
        """
        win.blit(self.IMG, (self.x2, self.y))
        win.blit(self.IMG, (self.x1, self.y))
