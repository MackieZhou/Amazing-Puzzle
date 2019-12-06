from gameNumber import gameNumber
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


def main():

    # the game window has a dimension of 350*350
    # the grid takes up 300*300
    # the margin on each side is 50
    win = pygame.display.set_mode(size=(700, 700))
    pygame.display.set_caption("Amazing Puzzle - Level 99")

    # colors:
    grey = (60, 60, 60)  # color of the two "goals"
    white = (255, 255, 255)  # color of the numbers
    black = (0, 0, 0)  # background color
    red = (255, 0, 0)
    blue = (0, 0, 255)
    grid_color = (40, 60, 40)

    # the two moving squares
    sq1X = 1
    sq1Y = 2
    sq1 = puzzle2(red, sq1X, sq1Y, win)
    sq2X = 1
    sq2Y = 3
    sq2 = puzzle2(blue, sq2X, sq2Y, win)

    # the two "goals" of the game
    goal1 = puzzle2(grey, 1, 1, win)
    goal2 = puzzle2(grey, 3, 1, win)

    # the game loop!!!!!
    run = True
    crash = False  # crash when the two squares ovelap
    puzzlewin = False  # win when the grey squares are covered
    while run:

        for event in pygame.event.get():
            # Quit condition
            if event.type == pygame.QUIT:
                run = False

            # check if the user hits the arrow keys
            elif event.type == pygame.KEYDOWN:
                # left button hit
                if event.key == pygame.K_LEFT:
                    sq1.move_left()
                    sq2.move_left()
                # right button hit
                elif event.key == pygame.K_RIGHT:
                    sq1.move_right()
                    sq2.move_right()
                # up button hit
                elif event.key == pygame.K_UP:
                    sq1.move_up()
                    sq2.move_up()
                # down button hit
                elif event.key == pygame.K_DOWN:
                    sq1.move_down()
                    sq2.move_down()

        # check if the two squares ovelap in each loop
        if sq1.coords() == sq2.coords():
            run = False
            crash = True
        # check if the user wins in each loop
        elif (sq1.coords() == goal1.coords() and sq2.coords() == goal2.coords()) or\
             (sq1.coords() == goal2.coords() and sq2.coords() == goal1.coords()):
            run = False
            puzzlewin = True

        # refill the window to black in each loop
        win.fill(black)

        # draw everything:
        # background grid - vertical
        pygame.draw.line(win, grid_color, (50, 50), (50, 650), 6)
        pygame.draw.line(win, grid_color, (200, 50), (200, 650), 6)
        pygame.draw.line(win, grid_color, (350, 50), (350, 650), 6)
        pygame.draw.line(win, grid_color, (500, 50), (500, 650), 6)
        pygame.draw.line(win, grid_color, (650, 50), (650, 650), 6)

        # background grid - horizontal
        pygame.draw.line(win, grid_color, (50, 50), (650, 50), 6)
        pygame.draw.line(win, grid_color, (50, 200), (650, 200), 6)
        pygame.draw.line(win, grid_color, (50, 350), (650, 350), 6)
        pygame.draw.line(win, grid_color, (50, 500), (650, 500), 6)
        pygame.draw.line(win, grid_color, (50, 650), (650, 650), 6)

        # walls - vertical
        bg_1 = pygame.image.load("bg2.jpg")
        bg_1_rect = pygame.Rect(46, 200, 14, 300)
        win.blit(bg_1, bg_1_rect, bg_1_rect)
        bg_2 = pygame.image.load("bg2.jpg")
        bg_2_rect = pygame.Rect(196, 50, 14, 150)
        win.blit(bg_2, bg_2_rect, bg_2_rect)
        bg_3 = pygame.image.load("bg2.jpg")
        bg_3_rect = pygame.Rect(346, 50, 14, 300)
        win.blit(bg_3, bg_3_rect, bg_3_rect)
        bg_4 = pygame.image.load("bg2.jpg")
        bg_4_rect = pygame.Rect(210, 346, 150, 14)
        win.blit(bg_4, bg_4_rect, bg_4_rect)
        bg_5 = pygame.image.load("bg2.jpg")
        bg_5_rect = pygame.Rect(196, 346, 14, 300)
        win.blit(bg_5, bg_5_rect, bg_5_rect)
        bg_6 = pygame.image.load("bg2.jpg")
        bg_6_rect = pygame.Rect(496, 50, 14, 311)
        win.blit(bg_6, bg_6_rect, bg_6_rect)
        bg_7 = pygame.image.load("bg2.jpg")
        bg_7_rect = pygame.Rect(500, 346, 150, 14)
        win.blit(bg_7, bg_7_rect, bg_7_rect)
        bg_8 = pygame.image.load("bg2.jpg")
        bg_8_rect = pygame.Rect(350, 496, 300, 14)
        win.blit(bg_8, bg_8_rect, bg_8_rect)
        bg_9 = pygame.image.load("bg2.jpg")
        bg_9_rect = pygame.Rect(346, 496, 14, 150)
        win.blit(bg_9, bg_9_rect, bg_9_rect)
        bg_10 = pygame.image.load("bg2.jpg")
        bg_10_rect = pygame.Rect(646, 50, 14, 150)
        win.blit(bg_10, bg_10_rect, bg_10_rect)
        bg_11 = pygame.image.load("bg2.jpg")
        bg_11_rect = pygame.Rect(500, 646, 150, 14)
        win.blit(bg_11, bg_11_rect, bg_11_rect)

        # draw the numbers
        size = 30
        game = 2
        n1_1 = gameNumber("1", size, white, (1, 1), "left", game)
        n1_1.draw(win)
        n1_2 = gameNumber("2", size, white, (1, 4), "left", game)
        n1_2.draw(win)
        n2_1 = gameNumber("6", size, white, (1, 4), "down", game)
        n2_1.draw(win)
        n2_2 = gameNumber("1", size, white, (2, 4), "down", game)
        n2_2.draw(win)
        n3_1 = gameNumber("3", size, white, (3, 4), "down", game)
        n3_1.draw(win)
        n3_2 = gameNumber("4", size, white, (4, 2), "right", game)
        n3_2.draw(win)
        n4_1 = gameNumber("5", size, white, (4, 3), "right", game)
        n4_1.draw(win)
        n4_2 = gameNumber("6", size, white, (4, 4), "right", game)
        n4_2.draw(win)
        n5_1 = gameNumber("5", size, white, (1, 1), "up", game)
        n5_1.draw(win)
        n5_2 = gameNumber("2", size, white, (2, 1), "up", game)
        n5_2.draw(win)
        n6_1 = gameNumber("4", size, white, (3, 1), "up", game)
        n6_1.draw(win)
        n6_2 = gameNumber("3", size, white, (4, 1), "up", game)
        n6_2.draw(win)

        # draw other things
        goal1.draw()
        goal2.draw()
        sq1.draw()
        sq2.draw()

        # update the display window in each loop
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
