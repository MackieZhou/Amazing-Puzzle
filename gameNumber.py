import pygame
pygame.init()


class gameNumber():

    def_font = "arial"

    def __init__(self, text, size, color, pos, direction, puzzle):
        """create a BOLD but NOT ITALIC text object; text is a string;
        size is an integer; color is a tuple (r, g, b);
        pos is a tuple (x, y) -- the position of the box that the number is next to;
        direction is string -- must be 'left', 'right', 'up', or 'down';
        puzzle is integer -- must be 1, 2, or 3
        """
        self.text = text
        self.size = size
        self.color = color
        self.pos = pos

        # the coordinates of the grid next to the number
        x = self.pos[0]
        y = self.pos[1]

        # to check the puzzle you are creating numbers for
        # create numbers for puzzle 1
        if puzzle == 1:
            grid_len = 100
            pass

        # create numbers for puzzle 1
        elif puzzle == 2:
            grid_len = 75
            pass

        # create numbers for puzzle 1
        elif puzzle == 3:
            grid_len = 60
            # if the number is at the left side of the grid
            if direction == "left":
                x2 = 8
                y2 = 25 + (y-0.5)*grid_len - 10
            # if the number is at the right side of the grid
            elif direction == "right":
                x2 = 332
                y2 = 25 + (y-0.5)*grid_len - 10
            # if the number is above the grid
            elif direction == "up":
                x2 = 25 + (x-0.5)*grid_len - 1
                y2 = 3
            # if the number is at the bottom of the grid
            elif direction == "down":
                x2 = 25 + (x-0.5)*grid_len - 10
                y2 = 326

        self.coords = (x2, y2)
        fon = pygame.font.SysFont(gameNumber.def_font, self.size, True, False)
        self.sur = fon.render(self.text, True, self.color)

    def draw(self, win):
        """draw text on a certain window"""
        win.blit(self.sur, self.coords)
