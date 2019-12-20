import pygame
pygame.init()


class gameText():
    """create a text object with a rectangle background under it"""

    def __init__(self, text, textSize, textcolor, textpos, bgSize, bgcolor):
        """text is a string; txtSize is an integer;
        textpos is a tuple (x, y) which represent the location
        where you will draw you text;
        text color and bgcolor are tuple (red, green, blue);
        bgSize is a tuple (x, y, width, length),
        where (x, y) represents the top-left corner of the bg rectangle,
        NOTE that if you don't want a background, make width&length = 0;
        win is the window on which you want to draw this text object"""

        self.txt = text
        self.textcolor = textcolor
        self.textSize = textSize
        self.textpos = textpos

        self.bgcolor = bgcolor

        # create the text surface and render it
        font = pygame.font.SysFont("arial", self.textSize, True, False)
        self.text = font.render(self.txt, True, self.textcolor)

        self.bg = pygame.Rect(bgSize[0], bgSize[1], bgSize[2], bgSize[3])

    def draw(self, win):
        """draw the text and its bg on a window"""
        # first draw a bg rectangle
        pygame.draw.rect(win, self.bgcolor, self.bg)
        # then draw the text
        win.blit(self.text, self.textpos)
