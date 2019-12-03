import pygame
pygame.init()


class puzzle1():
    """The 3*3 puzzle"""

    grid_len = 100
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
        # coords are in the GAME-WINDOW dimension
        self.cor_x = -25 + self.x * puzzle1.grid_len - puzzle1.half_len
        self.cor_y = -25 + self.y * puzzle1.grid_len - puzzle1.half_len

        self.sq = pygame.Rect(self.cor_x, self.cor_y, puzzle1.square_len, puzzle1.square_len)
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


def main():

    # the game window has a dimension of 350*350
    # the grid takes up 300*300
    # the margin on each side is 50
    win = pygame.display.set_mode(size=(350, 350))
    pygame.display.set_caption("Amazing Puzzle - Hard Level 9")

    # colors:
    grey = (40, 40, 40)
    black = (0, 0, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)

    # the two moving squares
    sq1X = 1
    sq1Y = 2
    sq1 = puzzle1(red, sq1X, sq1Y, win)
    sq2X = 1
    sq2Y = 3
    sq2 = puzzle1(blue, sq2X, sq2Y, win)

    # the two "goals" of the game are represented by two grey squares
    goal1 = puzzle1(grey, 1, 1, win)
    goal2 = puzzle1(grey, 3, 1, win)

    # the game loop!!!!!
    run = True
    crash = False  # crash when the two squares ovelap
    puzzlewin = False  # win when the grey squares are covered
    while run:
        pygame.time.delay(100)  # 1000 = 1 second

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # check if the user hits the arrow keys
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    sq1.move_left()
                    sq2.move_left()

                    # check if the two squares ovelap
                    if sq1.coords() == sq2.coords():
                        run = False
                        crash = True

                    # check is the user wins
                    elif (sq1.coords() == goal1.coords() and sq2.coords() == goal2.coords()) or\
                         (sq1.coords() == goal2.coords() and sq2.coords() == goal1.coords()):
                        run = False
                        puzzlewin = True

                elif event.key == pygame.K_RIGHT:
                    sq1.move_right()
                    sq2.move_right()

                    # check if the two squares ovelap
                    if sq1.coords() == sq2.coords():
                        run = False
                        crash = True

                    # check is the user wins
                    elif (sq1.coords() == goal1.coords() and sq2.coords() == goal2.coords()) or\
                         (sq1.coords() == goal2.coords() and sq2.coords() == goal1.coords()):
                        run = False
                        puzzlewin = True

                elif event.key == pygame.K_UP:
                    sq1.move_up()
                    sq2.move_up()

                    # check if the two squares ovelap
                    if sq1.coords() == sq2.coords():
                        run = False
                        crash = True

                    # check is the user wins
                    elif (sq1.coords() == goal1.coords() and sq2.coords() == goal2.coords()) or\
                         (sq1.coords() == goal2.coords() and sq2.coords() == goal1.coords()):
                        run = False
                        puzzlewin = True

                elif event.key == pygame.K_DOWN:
                    sq1.move_down()
                    sq2.move_down()

                    # check if the two squares ovelap
                    if sq1.coords() == sq2.coords():
                        run = False
                        crash = True

                    # check is the user wins
                    elif (sq1.coords() == goal1.coords() and sq2.coords() == goal2.coords()) or\
                         (sq1.coords() == goal2.coords() and sq2.coords() == goal1.coords()):
                        run = False
                        puzzlewin = True

        win.fill(black)

        # the background of the game (grid, walls, numbers)

        # draw everything:
        goal1.draw()
        goal2.draw()
        sq1.draw()
        sq2.draw()
        # update the display window
        pygame.display.update()

    # check if the two squares are on top of each other
    if crash:
        # display the "you lose you stupid" window
        pass

    # check is the user wins
    elif puzzlewin:
        # display the "you win" window
        pass

    pygame.quit()
    quit()


main()
