import pygame
pygame.init()


class Square():

    def __init__(self, color, center_x, center_y, length, win):
        """construct a square object;
        color is given as tuple (red, green, blue);
        length must be an EVEN number"""
        self.color = color
        self.length = length
        self.win = win
        half_len = length // 2
        corner_x = center_x - half_len
        corner_y = center_y - half_len
        self.sq = pygame.Rect(corner_x, corner_y, length, length)

    def draw(self):
        """draw the square"""
        pygame.draw.rect(self.win, self.color, self.sq)
