import pygame
pygame.init()


class puzzle3():
    """The 5*5 puzzle"""

    grid_len = 60
    square_len = grid_len * 3 // 5
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
        self.cor_x = 25 + (self.x-0.5)*puzzle3.grid_len - puzzle3.half_len
        self.cor_y = 25 + (self.y-0.5)*puzzle3.grid_len - puzzle3.half_len

        # create the rectangle and draw it
        self.sq = pygame.Rect(self.cor_x, self.cor_y, puzzle3.square_len, puzzle3.square_len)
        pygame.draw.rect(self.win, self.color, self.sq)

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_up(self):
        self.y -= 1

    def move_down(self):
        self.y += 1

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
    grey = (60, 60, 60)
    black = (0, 0, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    light_grey = (150, 150, 150)

    # the two moving squares
    sq1X = 1
    sq1Y = 2
    sq1 = puzzle3(red, sq1X, sq1Y, win)
    sq2X = 1
    sq2Y = 3
    sq2 = puzzle3(blue, sq2X, sq2Y, win)

    # the two "goals" of the game are represented by two grey squares
    goal1 = puzzle3(grey, 1, 1, win)
    goal2 = puzzle3(grey, 3, 1, win)

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

        # draw everything:
        # background grid - vertical
        pygame.draw.line(win, light_grey, (25, 25), (25, 325), 3)
        pygame.draw.line(win, light_grey, (85, 25), (85, 325), 3)
        pygame.draw.line(win, light_grey, (145, 25), (145, 325), 3)
        pygame.draw.line(win, light_grey, (205, 25), (205, 325), 3)
        pygame.draw.line(win, light_grey, (265, 25), (265, 325), 3)
        pygame.draw.line(win, light_grey, (325, 25), (325, 325), 3)
        # background grid - horizontal
        pygame.draw.line(win, light_grey, (25, 25), (325, 25), 3)
        pygame.draw.line(win, light_grey, (25, 85), (325, 85), 3)
        pygame.draw.line(win, light_grey, (25, 145), (325, 145), 3)
        pygame.draw.line(win, light_grey, (25, 205), (325, 205), 3)
        pygame.draw.line(win, light_grey, (25, 265), (325, 265), 3)
        pygame.draw.line(win, light_grey, (25, 325), (325, 325), 3)
        # walls - vertical
        wall_ver_1 = pygame.image.load("wall_ver.jpg")
        wall_ver_1_rect = pygame.Rect(23, 23, 7, 126)
        win.blit(wall_ver_1, wall_ver_1_rect, wall_ver_1_rect)
        wall_ver_2 = pygame.image.load("wall_ver.jpg")
        wall_ver_2_rect = pygame.Rect(23, 203, 7, 126)
        win.blit(wall_ver_2, wall_ver_2_rect, wall_ver_2_rect)
        wall_ver_3 = pygame.image.load("wall_ver.jpg")
        wall_ver_3_rect = pygame.Rect(83, 23, 7, 126)
        win.blit(wall_ver_3, wall_ver_3_rect, wall_ver_3_rect)
        wall_ver_4 = pygame.image.load("wall_ver.jpg")
        wall_ver_4_rect = pygame.Rect(83, 203, 7, 126)
        win.blit(wall_ver_4, wall_ver_4_rect, wall_ver_4_rect)
        wall_ver_5 = pygame.image.load("wall_ver.jpg")
        wall_ver_5_rect = pygame.Rect(143, 23, 7, 66)
        win.blit(wall_ver_5, wall_ver_5_rect, wall_ver_5_rect)
        wall_ver_6 = pygame.image.load("wall_ver.jpg")
        wall_ver_6_rect = pygame.Rect(203, 83, 7, 66)
        win.blit(wall_ver_6, wall_ver_6_rect, wall_ver_6_rect)
        wall_ver_7 = pygame.image.load("wall_ver.jpg")
        wall_ver_7_rect = pygame.Rect(263, 263, 7, 66)
        win.blit(wall_ver_7, wall_ver_7_rect, wall_ver_7_rect)
        wall_ver_8 = pygame.image.load("wall_ver.jpg")
        wall_ver_8_rect = pygame.Rect(323, 263, 7, 66)
        win.blit(wall_ver_8, wall_ver_8_rect, wall_ver_8_rect)
        # walls - horizontal
        wall_hor_1 = pygame.image.load("wall_hor.jpg")
        wall_hor_1_rect = pygame.Rect(203, 23, 126, 7)
        win.blit(wall_hor_1, wall_hor_1_rect, wall_hor_1_rect)
        wall_hor_2 = pygame.image.load("wall_hor.jpg")
        wall_hor_2_rect = pygame.Rect(203, 83, 126, 7)
        win.blit(wall_hor_2, wall_hor_2_rect, wall_hor_2_rect)
        wall_hor_3 = pygame.image.load("wall_hor.jpg")
        wall_hor_3_rect = pygame.Rect(83, 143, 126, 7)
        win.blit(wall_hor_3, wall_hor_3_rect, wall_hor_3_rect)
        wall_hor_4 = pygame.image.load("wall_hor.jpg")
        wall_hor_4_rect = pygame.Rect(263, 143, 66, 7)
        win.blit(wall_hor_4, wall_hor_4_rect, wall_hor_4_rect)
        wall_hor_5 = pygame.image.load("wall_hor.jpg")
        wall_hor_5_rect = pygame.Rect(83, 203, 246, 7)
        win.blit(wall_hor_5, wall_hor_5_rect, wall_hor_5_rect)
        wall_hor_6 = pygame.image.load("wall_hor.jpg")
        wall_hor_6_rect = pygame.Rect(143, 263, 126, 7)
        win.blit(wall_hor_6, wall_hor_6_rect, wall_hor_6_rect)
        wall_hor_7 = pygame.image.load("wall_hor.jpg")
        wall_hor_7_rect = pygame.Rect(143, 323, 66, 7)
        win.blit(wall_hor_7, wall_hor_7_rect, wall_hor_7_rect)
        # draw other things
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
