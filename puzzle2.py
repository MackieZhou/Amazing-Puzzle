import pygame
pygame.init()


class puzzle2():
    """The 5*5 puzzle"""

    grid_len = 150
    square_len = grid_len * 3//5
    half_len = square_len // 2

    def __init__(self, color, x, y, win):
        """construct a square object;color is given as tuple (red, green, blue)
        """
        self.color = color
        self.win = win

        # x and y can be represented by GRID coordinates
        # from (1, 1) (1, 2)... to (5, 5)
        self.x = x
        self.y = y

    def draw(self):
        """create the pygame rectangle and draw the rectangle"""
        # (cor_x, cor_y) is the top-left corner of the square
        # convert GRID coordinates into GAME-WINDOW coordinates
        self.cor_x = 50 + (self.x-0.5)*puzzle2.grid_len - puzzle2.half_len
        self.cor_y = 50 + (self.y-0.5)*puzzle2.grid_len - puzzle2.half_len

        # create the rectangle and draw it
        self.sq = pygame.Rect(self.cor_x, self.cor_y, puzzle2.square_len, puzzle2.square_len)
        pygame.draw.rect(self.win, self.color, self.sq)

    def move_left(self):
        if self.x == 1 and self.y == 1:
            self.x = 2
            self.y = 4
        elif self.x == 1 and self.y == 2:
            self.x = 1
            self.y = 2
        elif self.x == 1 and self.y == 3:
            self.x = 1
            self.y = 3
        elif self.x == 1 and self.y == 4:
            self.x = 2
            self.y = 1

        # x = 2
        elif self.x == 2 and self.y == 1:
            self.x = 2
            self.y = 1
        elif self.x == 2 and self.y == 2:
            self.x = 1
            self.y = 2
        elif self.x == 2 and self.y == 3:
            self.x = 2
            self.y = 3
        elif self.x == 2 and self.y == 4:
            self.x = 2
            self.y = 4

        # x = 3
        elif self.x == 3 and self.y == 1:
            self.x = 3
            self.y = 1
        elif self.x == 3 and self.y == 2:
            self.x = 3
            self.y = 2
        elif self.x == 3 and self.y == 3:
            self.x = 2
            self.y = 3
        elif self.x == 3 and self.y == 4:
            self.x = 3
            self.y = 4

        # x = 4
        elif self.x == 4 and self.y == 1:
            self.x = 4
            self.y = 1
        elif self.x == 4 and self.y == 2:
            self.x = 4
            self.y = 2
        elif self.x == 4 and self.y == 3:
            self.x = 3
            self.y = 3
        elif self.x == 4 and self.y == 4:
            self.x = 3
            self.y = 4

    def move_right(self):
        # x = 1
        if self.x == 1 and self.y == 1:
            self.x = 1
            self.y = 1
        elif self.x == 1 and self.y == 2:
            self.x = 2
            self.y = 2
        elif self.x == 1 and self.y == 3:
            self.x = 1
            self.y = 3
        elif self.x == 1 and self.y == 4:
            self.x = 1
            self.y = 4

        # x = 2
        elif self.x == 2 and self.y == 1:
            self.x = 2
            self.y = 1
        elif self.x == 2 and self.y == 2:
            self.x = 2
            self.y = 2
        elif self.x == 2 and self.y == 3:
            self.x = 3
            self.y = 3
        elif self.x == 2 and self.y == 4:
            self.x = 2
            self.y = 4

        # x = 3
        elif self.x == 3 and self.y == 1:
            self.x = 3
            self.y = 1
        elif self.x == 3 and self.y == 2:
            self.x = 3
            self.y = 2
        elif self.x == 3 and self.y == 3:
            self.x = 4
            self.y = 3
        elif self.x == 3 and self.y == 4:
            self.x = 4
            self.y = 4

        # x = 4
        elif self.x == 4 and self.y == 1:
            self.x = 4
            self.y = 1
        elif self.x == 4 and self.y == 2:
            self.x = 3
            self.y = 1
        elif self.x == 4 and self.y == 3:
            self.x = 1
            self.y = 1
        elif self.x == 4 and self.y == 4:
            self.x = 1
            self.y = 4

    def move_up(self):
        # x = 1
        if self.x == 1 and self.y == 1:
            self.x = 4
            self.y = 3
        elif self.x == 1 and self.y == 2:
            self.x = 1
            self.y = 1
        elif self.x == 1 and self.y == 3:
            self.x = 1
            self.y = 2
        elif self.x == 1 and self.y == 4:
            self.x = 1
            self.y = 3

        # x = 2
        elif self.x == 2 and self.y == 1:
            self.x = 1
            self.y = 4
        elif self.x == 2 and self.y == 2:
            self.x = 2
            self.y = 1
        elif self.x == 2 and self.y == 3:
            self.x = 2
            self.y = 3
        elif self.x == 2 and self.y == 4:
            self.x = 2
            self.y = 3

        # x = 3
        elif self.x == 3 and self.y == 1:
            self.x = 4
            self.y = 2
        elif self.x == 3 and self.y == 2:
            self.x = 3
            self.y = 1
        elif self.x == 3 and self.y == 3:
            self.x = 3
            self.y = 2
        elif self.x == 3 and self.y == 4:
            self.x = 3
            self.y = 4

        # x = 4
        elif self.x == 4 and self.y == 1:
            self.x = 3
            self.y = 4
        elif self.x == 4 and self.y == 2:
            self.x = 4
            self.y = 1
        elif self.x == 4 and self.y == 3:
            self.x = 4
            self.y = 3
        elif self.x == 4 and self.y == 4:
            self.x = 4
            self.y = 4

    def move_down(self):
        # x = 1
        if self.x == 1 and self.y == 1:
            self.x = 1
            self.y = 2
        elif self.x == 1 and self.y == 2:
            self.x = 1
            self.y = 3
        elif self.x == 1 and self.y == 3:
            self.x = 1
            self.y = 4
        elif self.x == 1 and self.y == 4:
            self.x = 4
            self.y = 4

        # x = 2
        elif self.x == 2 and self.y == 1:
            self.x = 2
            self.y = 2
        elif self.x == 2 and self.y == 2:
            self.x = 2
            self.y = 2
        elif self.x == 2 and self.y == 3:
            self.x = 2
            self.y = 4
        elif self.x == 2 and self.y == 4:
            self.x = 1
            self.y = 1

        # x = 3
        elif self.x == 3 and self.y == 1:
            self.x = 3
            self.y = 2
        elif self.x == 3 and self.y == 2:
            self.x = 3
            self.y = 3
        elif self.x == 3 and self.y == 3:
            self.x = 3
            self.y = 3
        elif self.x == 3 and self.y == 4:
            self.x = 4
            self.y = 1

        # x = 4
        elif self.x == 4 and self.y == 1:
            self.x = 4
            self.y = 2
        elif self.x == 4 and self.y == 2:
            self.x = 4
            self.y = 2
        elif self.x == 4 and self.y == 3:
            self.x = 4
            self.y = 3
        elif self.x == 4 and self.y == 4:
            self.x = 4
            self.y = 4

    def coords(self):
        """return the tuple's coordinates"""
        return (self.x, self.y)
