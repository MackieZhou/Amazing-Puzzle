from gameNumber import gameNumber
from gameText import gameText
import pygame
pygame.init()


class puzzle1():
    """The 3*3 puzzle"""

    grid_len = 200
    square_len = grid_len * 3 // 5
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
        self.cor_x = 50 + (self.x-0.5)*puzzle1.grid_len - puzzle1.half_len
        self.cor_y = 50 + (self.y-0.5)*puzzle1.grid_len - puzzle1.half_len

        self.sq = pygame.Rect(self.cor_x, self.cor_y, puzzle1.square_len, puzzle1.square_len)
        pygame.draw.rect(self.win, self.color, self.sq)

    def move_left(self):
        # x = 1
        if self.x == 1 and self.y == 1:
            self.x = 3
            self.y = 1
        elif self.x == 1 and self.y == 2:
            self.x = 1
            self.y = 2
        elif self.x == 1 and self.y == 3:
            self.x = 3
            self.y = 3
        # x = 2
        elif self.x == 2 and self.y == 1:
            self.x = 2
            self.y = 1
        elif self.x == 2 and self.y == 2:
            self.x = 2
            self.y = 2
        elif self.x == 2 and self.y == 3:
            self.x = 2
            self.y = 3
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

    def move_right(self):
        # x = 1
        if self.x == 1 and self.y == 1:
            self.x = 1
            self.y = 1
        elif self.x == 1 and self.y == 2:
            self.x = 1
            self.y = 2
        elif self.x == 1 and self.y == 3:
            self.x = 1
            self.y = 3
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
        # x = 3
        elif self.x == 3 and self.y == 1:
            self.x = 3
            self.y = 1
        elif self.x == 3 and self.y == 2:
            self.x = 2
            self.y = 1
        elif self.x == 3 and self.y == 3:
            self.x = 1
            self.y = 3

    def move_up(self):
        # x = 1
        if self.x == 1 and self.y == 1:
            self.x = 1
            self.y = 3
        elif self.x == 1 and self.y == 2:
            self.x = 1
            self.y = 1
        elif self.x == 1 and self.y == 3:
            self.x = 1
            self.y = 2
        # x = 2
        elif self.x == 2 and self.y == 1:
            self.x = 3
            self.y = 2
        elif self.x == 2 and self.y == 2:
            self.x = 2
            self.y = 1
        elif self.x == 2 and self.y == 3:
            self.x = 2
            self.y = 2
        # x = 3
        elif self.x == 3 and self.y == 1:
            self.x = 1
            self.y = 1
        elif self.x == 3 and self.y == 2:
            self.x = 3
            self.y = 1
        elif self.x == 3 and self.y == 3:
            self.x = 3
            self.y = 3

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
            self.y = 1
        # x = 2
        elif self.x == 2 and self.y == 1:
            self.x = 2
            self.y = 2
        elif self.x == 2 and self.y == 2:
            self.x = 2
            self.y = 3
        elif self.x == 2 and self.y == 3:
            self.x = 2
            self.y = 3
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

    def coords(self):
        """return the tuple's coordinates"""
        return (self.x, self.y)


def main():

    # the game window has a dimension of 700*700
    # the grid takes up 300*300
    # the margin on each side is 50
    win = pygame.display.set_mode(size=(700, 700))
    pygame.display.set_caption("Amazing Puzzle - Hard Level 9")

    # colors:
    grey = (60, 60, 60)
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    grid_color = (40, 60, 40)

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

        # get the original position of the two squares in each loop
        # in case the two squares crash -- need to back to the last move
        sq1_x, sq1_y = sq1.coords()[0], sq1.coords()[1]
        sq2_x, sq2_y = sq2.coords()[0], sq2.coords()[1]

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

        # check if the two squares ovelap
        if sq1.coords() == sq2.coords():
            run = False
            crash = True

        # check is the user wins
        elif (sq1.coords() == goal1.coords() and sq2.coords() == goal2.coords()) or\
             (sq1.coords() == goal2.coords() and sq2.coords() == goal1.coords()):
            run = False
            puzzlewin = True

        # refill the window to black in each loop
        win.fill(black)
                
        # draw everything:
        # background grid - vertical
        pygame.draw.line(win, grid_color, (50, 50), (50, 650), 4)
        pygame.draw.line(win, grid_color, (250, 50), (250, 650), 4)
        pygame.draw.line(win, grid_color, (450, 50), (450, 650), 4)
        pygame.draw.line(win, grid_color, (650, 50), (650, 650), 4)
        # background grid - horizontal
        pygame.draw.line(win, grid_color, (50, 50), (650, 50), 4)
        pygame.draw.line(win, grid_color, (50, 250), (650, 250), 4)
        pygame.draw.line(win, grid_color, (50, 450), (650, 450), 4)
        pygame.draw.line(win, grid_color, (50, 650), (650, 650), 4) 
        
        # walls - vertical
        wall_ver_1 = pygame.image.load("bg.jpg")
        wall_ver_1_rect = pygame.Rect(46, 246, 8, 208)
        win.blit(wall_ver_1, wall_ver_1_rect, wall_ver_1_rect)
        wall_ver_2_rect = pygame.Rect(246, 46, 8, 608)
        win.blit(wall_ver_1, wall_ver_2_rect, wall_ver_2_rect)
        wall_ver_3_rect = pygame.Rect(446, 46, 8, 408)
        win.blit(wall_ver_1, wall_ver_3_rect, wall_ver_3_rect)
        wall_ver_4_rect = pygame.Rect(646, 46, 8, 208)
        # # walls - horizontal
        wall_ver_1_rect = pygame.Rect(446, 446, 208, 8)
        win.blit(wall_ver_1, wall_ver_1_rect, wall_ver_1_rect)
        wall_hor_2_rect = pygame.Rect(246, 646, 408, 8)               
                
        # draw the numbers
        size = 40
        game = 1
        n1_1 = gameNumber("1", size, white, (1, 3), "left", game)
        n1_1.draw(win)
        n1_2 = gameNumber("1", size, white, (3, 3), "right", game)
        n1_2.draw(win)
        n2_1 = gameNumber("2", size, white, (1, 1), "up", game)
        n2_1.draw(win)
        n2_2 = gameNumber("2", size, white, (1, 3), "down", game)
        n2_2.draw(win)
        n3_1 = gameNumber("3", size, white, (2, 1), "up", game)
        n3_1.draw(win)
        n3_2 = gameNumber("3", size, white, (3, 1), "right", game)
        n3_2.draw(win)
        n4_1 = gameNumber("4", size, white, (3, 1), "up", game)
        n4_1.draw(win)
        n4_2 = gameNumber("4", size, white, (1, 1), "left", game)
        n4_2.draw(win)

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
            youlose = gameText("Oops... The two squares cannot overlap",
                               25, red, (150, 300), (100, 295, 500, 40), grey)
            back = gameText("back to the last move",
                            25, red, (250, 350), (200, 345, 350, 40), grey)
            youlose.draw(win)
            back.draw(win)
            pygame.display.update()
            pygame.time.wait(1500)  # 1000 = 1 second

            # move the squares back to their last position
            sq1.x, sq1.y = sq1_x, sq1_y
            sq2.x, sq2.y = sq2_x, sq2_y
            sq1.draw()
            sq2.draw()
            pygame.display.update()

            crash = False
            run = True
    
    # check if the user wins
    if puzzlewin:
        # display the "you win" window
        youwin = gameText("Congrats! You Win!!", 40, red, (190, 300), (150, 300, 400, 50), grey)
        youwin.draw(win)
        pygame.display.update()
        pygame.time.wait(1500)  # 1000 = 1 second

    pygame.quit()
    quit()
                
main()
