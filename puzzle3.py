import pygame
pygame.init()


class puzzle3():
    """The 5*5 puzzle"""

    grid_len = 120
    square_len = grid_len * 3 // 5
    half_len = square_len // 2  # half the length of a colored square

    def __init__(self, color, x, y, win):
        """
        construct a square object; color is given as a tuple (red, green, blue);
        (x, y) represent the squares position on the game board, with top-left grid as (0, 0)
        and down-right grid as (5, 5); win is the window on which you want to draw the square
        """
        self.color = color
        self.win = win

        # x and y can be represented by GRID coordinates
        # from (1, 1) (1, 2)... to (5, 5)
        self.x = x
        self.y = y

    def draw(self):
        """create the pygame rectangle and draw the rectangle on a surface"""
        # (cor_x, cor_y) is the top-left corner of the square
        # convert GRID coordinates into GAME-WINDOW coordinates
        self.cor_x = 50 + (self.x-0.5)*puzzle3.grid_len - puzzle3.half_len
        self.cor_y = 50 + (self.y-0.5)*puzzle3.grid_len - puzzle3.half_len

        # create the rectangle and draw it
        self.sq = pygame.Rect(self.cor_x, self.cor_y, puzzle3.square_len, puzzle3.square_len)
        pygame.draw.rect(self.win, self.color, self.sq)

    def move_left(self):
        """move the square to the left (according to the game board design)"""
        # x = 1
        if self.x == 1 and self.y == 1:
            self.x = 1
            self.y = 1
        elif self.x == 1 and self.y == 2:
            self.x = 1
            self.y = 2
        elif self.x == 1 and self.y == 3:
            self.x = 3
            self.y = 1
        elif self.x == 1 and self.y == 4:
            self.x = 1
            self.y = 4
        elif self.x == 1 and self.y == 5:
            self.x = 1
            self.y = 5

        # x = 2
        elif self.x == 2 and self.y == 1:
            self.x = 2
            self.y = 1
        elif self.x == 2 and self.y == 2:
            self.x = 2
            self.y = 2
        elif self.x == 2 and self.y == 3:
            self.x = 1
            self.y = 3
        elif self.x == 2 and self.y == 4:
            self.x = 2
            self.y = 4
        elif self.x == 2 and self.y == 5:
            self.x = 2
            self.y = 5

        # x = 3
        elif self.x == 3 and self.y == 1:
            self.x = 3
            self.y = 1
        elif self.x == 3 and self.y == 2:
            self.x = 2
            self.y = 2
        elif self.x == 3 and self.y == 3:
            self.x = 2
            self.y = 3
        elif self.x == 3 and self.y == 4:
            self.x = 2
            self.y = 4
        elif self.x == 3 and self.y == 5:
            self.x = 2
            self.y = 5

        # x = 4
        elif self.x == 4 and self.y == 1:
            self.x = 3
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
        elif self.x == 4 and self.y == 5:
            self.x = 3
            self.y = 5

        # x = 5
        elif self.x == 5 and self.y == 1:
            self.x = 4
            self.y = 1
        elif self.x == 5 and self.y == 2:
            self.x = 4
            self.y = 2
        elif self.x == 5 and self.y == 3:
            self.x = 4
            self.y = 3
        elif self.x == 5 and self.y == 4:
            self.x = 4
            self.y = 4
        elif self.x == 5 and self.y == 5:
            self.x = 5
            self.y = 5

    def move_right(self):
        """move the square to the right (according to the game board design)"""
        # x = 1
        if self.x == 1 and self.y == 1:
            self.x = 1
            self.y = 1
        elif self.x == 1 and self.y == 2:
            self.x = 1
            self.y = 2
        elif self.x == 1 and self.y == 3:
            self.x = 2
            self.y = 3
        elif self.x == 1 and self.y == 4:
            self.x = 1
            self.y = 4
        elif self.x == 1 and self.y == 5:
            self.x = 1
            self.y = 5

        # x = 2
        elif self.x == 2 and self.y == 1:
            self.x = 2
            self.y = 1
        elif self.x == 2 and self.y == 2:
            self.x = 3
            self.y = 2
        elif self.x == 2 and self.y == 3:
            self.x = 3
            self.y = 3
        elif self.x == 2 and self.y == 4:
            self.x = 3
            self.y = 4
        elif self.x == 2 and self.y == 5:
            self.x = 3
            self.y = 5

        # x = 3
        elif self.x == 3 and self.y == 1:
            self.x = 4
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
        elif self.x == 3 and self.y == 5:
            self.x = 4
            self.y = 5

        # x = 4
        elif self.x == 4 and self.y == 1:
            self.x = 5
            self.y = 1
        elif self.x == 4 and self.y == 2:
            self.x = 5
            self.y = 2
        elif self.x == 4 and self.y == 3:
            self.x = 5
            self.y = 3
        elif self.x == 4 and self.y == 4:
            self.x = 5
            self.y = 4
        elif self.x == 4 and self.y == 5:
            self.x = 4
            self.y = 5

        # x = 5
        elif self.x == 5 and self.y == 1:
            self.x = 5
            self.y = 3
        elif self.x == 5 and self.y == 2:
            self.x = 2
            self.y = 1
        elif self.x == 5 and self.y == 3:
            self.x = 5
            self.y = 1
        elif self.x == 5 and self.y == 4:
            self.x = 2
            self.y = 5
        elif self.x == 5 and self.y == 5:
            self.x = 5
            self.y = 5

    def move_up(self):
        """move up the square (according to the game board design)"""
        # x = 1
        if self.x == 1 and self.y == 1:
            self.x = 5
            self.y = 5
        elif self.x == 1 and self.y == 2:
            self.x = 1
            self.y = 1
        elif self.x == 1 and self.y == 3:
            self.x = 1
            self.y = 2
        elif self.x == 1 and self.y == 4:
            self.x = 1
            self.y = 3
        elif self.x == 1 and self.y == 5:
            self.x = 1
            self.y = 4

        # x = 2
        elif self.x == 2 and self.y == 1:
            self.x = 5
            self.y = 2
        elif self.x == 2 and self.y == 2:
            self.x = 2
            self.y = 1
        elif self.x == 2 and self.y == 3:
            self.x = 2
            self.y = 3
        elif self.x == 2 and self.y == 4:
            self.x = 2
            self.y = 4
        elif self.x == 2 and self.y == 5:
            self.x = 2
            self.y = 4

        # x = 3
        elif self.x == 3 and self.y == 1:
            self.x = 1
            self.y = 3
        elif self.x == 3 and self.y == 2:
            self.x = 3
            self.y = 1
        elif self.x == 3 and self.y == 3:
            self.x = 3
            self.y = 3
        elif self.x == 3 and self.y == 4:
            self.x = 3
            self.y = 4
        elif self.x == 3 and self.y == 5:
            self.x = 3
            self.y = 5

        # x = 4
        elif self.x == 4 and self.y == 1:
            self.x = 4
            self.y = 1
        elif self.x == 4 and self.y == 2:
            self.x = 4
            self.y = 2
        elif self.x == 4 and self.y == 3:
            self.x = 4
            self.y = 2
        elif self.x == 4 and self.y == 4:
            self.x = 4
            self.y = 4
        elif self.x == 4 and self.y == 5:
            self.x = 4
            self.y = 5

        # x = 5
        elif self.x == 5 and self.y == 1:
            self.x = 5
            self.y = 1
        elif self.x == 5 and self.y == 2:
            self.x = 5
            self.y = 2
        elif self.x == 5 and self.y == 3:
            self.x = 5
            self.y = 3
        elif self.x == 5 and self.y == 4:
            self.x = 5
            self.y = 4
        elif self.x == 5 and self.y == 5:
            self.x = 5
            self.y = 4

    def move_down(self):
        """move down the square (according to the game board design)"""
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
            self.x = 1
            self.y = 5
        elif self.x == 1 and self.y == 5:
            self.x = 4
            self.y = 5

        # x = 2
        elif self.x == 2 and self.y == 1:
            self.x = 2
            self.y = 2
        elif self.x == 2 and self.y == 2:
            self.x = 2
            self.y = 2
        elif self.x == 2 and self.y == 3:
            self.x = 2
            self.y = 3
        elif self.x == 2 and self.y == 4:
            self.x = 2
            self.y = 5
        elif self.x == 2 and self.y == 5:
            self.x = 5
            self.y = 4

        # x = 3
        elif self.x == 3 and self.y == 1:
            self.x = 3
            self.y = 2
        elif self.x == 3 and self.y == 2:
            self.x = 3
            self.y = 2
        elif self.x == 3 and self.y == 3:
            self.x = 3
            self.y = 3
        elif self.x == 3 and self.y == 4:
            self.x = 3
            self.y = 4
        elif self.x == 3 and self.y == 5:
            self.x = 3
            self.y = 5

        # x = 4
        elif self.x == 4 and self.y == 1:
            self.x = 4
            self.y = 1
        elif self.x == 4 and self.y == 2:
            self.x = 4
            self.y = 3
        elif self.x == 4 and self.y == 3:
            self.x = 4
            self.y = 3
        elif self.x == 4 and self.y == 4:
            self.x = 4
            self.y = 4
        elif self.x == 4 and self.y == 5:
            self.x = 1
            self.y = 5

        # x = 5
        elif self.x == 5 and self.y == 1:
            self.x = 5
            self.y = 1
        elif self.x == 5 and self.y == 2:
            self.x = 5
            self.y = 2
        elif self.x == 5 and self.y == 3:
            self.x = 5
            self.y = 3
        elif self.x == 5 and self.y == 4:
            self.x = 5
            self.y = 5
        elif self.x == 5 and self.y == 5:
            self.x = 1
            self.y = 1

    def coords(self):
        """return the tuple's coordinates"""
        return (self.x, self.y)
