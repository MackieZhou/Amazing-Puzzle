import pygame
pygame.init()


class puzzle2():
    """The 4*4 puzzle"""

    grid_len = 75
    square_len = grid_len * 4 // 5
    half_len = square_len // 2

    def __init__(self, color, x, y, win):
        """construct a square object;color is given as tuple (red, green, blue)
        """
        self.color = color
        self.win = win

        # x and y can be represented by GRID coordinates
        # from (1, 1) (1, 2)... to (3, 3)
        self.x = x
        self.y = y

    def draw(self):
        """create the pygame rectangle and draw the rectangle"""
        # (cor_x, cor_y) is the top-left corner of the square
        # convert GRID coordinates into GAME-WINDOW coordinates
        self.cor_x = 25 + (self.x-0.5)*puzzle2.grid_len - puzzle2.half_len
        self.cor_y = 25 + (self.y-0.5)*puzzle2.grid_len - puzzle2.half_len

        self.sq = pygame.Rect(self.cor_x, self.cor_y, puzzle2.square_len, puzzle2.square_len)
        pygame.draw.rect(self.win, self.color, self.sq)

    def move_left(self):
        pass

    def move_right(self):
        pass

    def move_up(self):
        pass

    def move_down(self):
        pass

    def coords(self):
        """return the tuple's coordinates"""
        return (self.x, self.y)
