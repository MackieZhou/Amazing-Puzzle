from gameNumber import gameNumber
from gameText import gameText
from puzzle1 import puzzle1
from puzzle2 import puzzle2
from puzzle3 import puzzle3
import pygame
pygame.init()


def createsq(choice, win):
    """check the puzzle the user wants to play and create squares"""

    # color of the two static grey squares
    grey = (50, 50, 50)
    # color of the two colored moving squares
    yellow = (254, 208, 134)
    blue = (160, 234, 251)

    # the user wants to play the 3*3 puzzle
    if choice == 1:
        sq1 = puzzle1(yellow, 1, 2, win)
        sq2 = puzzle1(blue, 1, 3, win)
        goal1 = puzzle1(grey, 1, 1, win)
        goal2 = puzzle1(grey, 3, 1, win)
        return sq1, sq2, goal1, goal2

    # the user wants to play the 4*4 puzzle
    if choice == 2:
        sq1 = puzzle2(yellow, 1, 2, win)
        sq2 = puzzle2(blue, 1, 3, win)
        goal1 = puzzle2(grey, 1, 1, win)
        goal2 = puzzle2(grey, 3, 1, win)
        return sq1, sq2, goal1, goal2

    # the user wants to play the 5*5 puzzle
    if choice == 3:
        sq1 = puzzle3(yellow, 1, 2, win)
        sq2 = puzzle3(blue, 1, 3, win)
        goal1 = puzzle3(grey, 1, 1, win)
        goal2 = puzzle3(grey, 3, 1, win)
        return sq1, sq2, goal1, goal2


def main():
    """create a pygame window for the game;
    game-selection loop and game loop included."""
    # the game window has a dimension of 700*700
    # the grid takes up 600*600
    # the margin on each side is 50
    win = pygame.display.set_mode(size=(700, 700))
    pygame.display.set_caption("The Amazing Puzzle")

    # the main page background picture
    bc1 = pygame.image.load("bc1.jpg")
    bc1_rect = pygame.Rect(0, 0, 700, 700)
    win.blit(bc1, bc1_rect, bc1_rect)

    # music:
    pygame.mixer.music.load("Xmas.wav")
    pygame.mixer.music.stop()
    pygame.mixer.music.play(-1)
    crash_sound = pygame.mixer.Sound("lose.wav")
    move_sound = pygame.mixer.Sound("move.wav")
    win_sound = pygame.mixer.Sound("win.wav")
    click_sound = pygame.mixer.Sound("Toom_Click.wav")
    pygame.mixer.music.set_volume(0.5)

    # colors:
    white = (255, 255, 255)  # color of the numbers
    black = (0, 0, 0)  # background color
    blue = (80, 80, 255)
    grid_color = (40, 50, 40)
    yellow = (247, 231, 171)
    blue1 = (145, 154, 184)
    blue2 = (106, 123, 181)
    pink = (234, 211, 220)
    darkblue = (31, 24, 49)

    # the loop for the user to choose puzzle/guide
    choose = True  # True -- still need to choose
    choice = 0
    while choose:
        # draw the things on the front page of the game
        title = gameText("The AMAZING Puzzle", 50, white, (140, 100), (140, 100, 0, 0), darkblue)

        # the game buttons
        game1 = gameText("Level 9", 32, darkblue, (125, 290), (125, 290, 0, 0), yellow)
        game2 = gameText("Level 99", 32, darkblue, (310, 290), (310, 290, 0, 0), pink)
        game3 = gameText("Level 999", 32, darkblue, (490, 290), (490, 290, 0, 0), blue1)
        rule = gameText('Guide', 27, white, (600, 540), (600, 540, 0, 0), blue2)

        # draw everything
        title.draw(win)
        game1.draw(win)
        game2.draw(win)
        game3.draw(win)
        rule.draw(win)

        # update display to show the drawings
        pygame.display.update()

        choice = 0
        for event in pygame.event.get():
            # check if the user wants to quit the game
            if event.type == pygame.QUIT:
                choose = False
                pygame.quit()
                quit()

            # check if the user click on anywhere in the window
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                # check if the user chooses puzzle1
                if (95 <= click[0] <= 245) & (260 <= click[1] <= 360):
                    choice += 1
                    choose = False
                    pygame.mixer.Sound.play(click_sound)
                # check if the user chooses puzzle2
                if (280 <= click[0] <= 445) & (260 <= click[1] <= 360):
                    choice += 2
                    choose = False
                    pygame.mixer.Sound.play(click_sound)
                # check if the user chooses puzzle3
                if (460 <= click[0] <= 640) & (260 <= click[1] <= 360):
                    choice += 3
                    choose = False
                    pygame.mixer.Sound.play(click_sound)
                # check if the user chooses rules
                if (580 <= click[0] <= 685) & (520 <= click[1] <= 595):
                    choice += 4
                    choose = False
                    pygame.mixer.Sound.play(click_sound)

    # if the user clicks the guide button
    if choice == 4:
        pygame.display.set_caption("Guide")

        # the guide page background picture
        bc2 = pygame.image.load("guide.jpg")
        bc2_rect = pygame.Rect(0, 0, 700, 700)
        win.blit(bc2, bc2_rect, bc2_rect)

        # the rules/instructions on the guide page
        t1 = 'How to win?'
        t2 = 'Let the yellow and blue squares overlap the two static grey squares.'
        t3 = 'How to play?'
        t4 = '-- Choose a difficulty level from level 9, 99, and 999.'
        t5 = '-- Control the movement of the yellow square and the blue square'
        t6 = '   by hitting the left, right, up, or down arrow keys on your keyboard.'
        t7 = 'Rules'
        t8 = '1. The two squares move together (i.e. if you hit the up arrow'
        t9 = '    key, both squares will move up a grid)'
        t10 = '2. NO MOVEMENT when hitting a wall. If only one of the squares is'
        t11 = '    stopped by the wall, the other one will move normally (this is'
        t12 = '    a strategy you can use to only move one square).'
        t13 = '3. The squares will be transported by  numbers around the game'
        t14 = '    board. All the numbers appear in pairs and they are like'
        t15 = '    channels between grids. If you move a colored square out'
        t16 = '    of the board from one number, the square will reappear in'
        t17 = '    the other grid surrounded by the same number.'
        t18 = '4. Squares won\'t OVERLAP!! If your movement is going to make them'
        t19 = '    overlap, they won\'t move and the crash sound will be played.'

        rule1 = gameText(t1, 22, white, (70, 30), (50, 80, 0, 0), black)
        rule2 = gameText(t2, 22, white, (70, 60), (50, 110, 0, 0), black)
        rule3 = gameText(t3, 22, white, (70, 120), (50, 140, 0, 0), black)
        rule4 = gameText(t4, 22, white, (70, 150), (50, 170, 0, 0), black)
        rule5 = gameText(t5, 22, white, (70, 180), (50, 200, 0, 0), black)
        rule6 = gameText(t6, 22, white, (70, 210), (50, 230, 0, 0), black)
        rule7 = gameText(t7, 22, white, (70, 270), (50, 260, 0, 0), black)
        rule8 = gameText(t8, 22, white, (70, 300), (50, 290, 0, 0), black)
        rule9 = gameText(t9, 22, white, (70, 330), (50, 320, 0, 0), black)
        rule10 = gameText(t10, 22, white, (70, 360), (50, 350, 0, 0), black)
        rule11 = gameText(t11, 22, white, (70, 390), (50, 380, 0, 0), black)
        rule12 = gameText(t12, 22, white, (70, 420), (50, 410, 0, 0), black)
        rule13 = gameText(t13, 22, white, (70, 450), (50, 440, 0, 0), black)
        rule14 = gameText(t14, 22, white, (70, 480), (50, 470, 0, 0), black)
        rule15 = gameText(t15, 22, white, (70, 510), (50, 500, 0, 0), black)
        rule16 = gameText(t16, 22, white, (70, 540), (50, 530, 0, 0), black)
        rule17 = gameText(t17, 22, white, (70, 570), (50, 560, 0, 0), black)
        rule18 = gameText(t18, 22, white, (70, 600), (50, 590, 0, 0), black)
        rule19 = gameText(t19, 22, white, (70, 630), (50, 590, 0, 0), black)
        quitbut = gameText('BACK', 22, white, (5, 670), (0, 665, 70, 35), blue)

        rule1.draw(win)
        rule2.draw(win)
        rule3.draw(win)
        rule4.draw(win)
        rule5.draw(win)
        rule6.draw(win)
        rule7.draw(win)
        rule8.draw(win)
        rule9.draw(win)
        rule10.draw(win)
        rule11.draw(win)
        rule12.draw(win)
        rule13.draw(win)
        rule14.draw(win)
        rule15.draw(win)
        rule16.draw(win)
        rule17.draw(win)
        rule18.draw(win)
        rule19.draw(win)
        quitbut.draw(win)
        pygame.display.update()

        # check for events
        while True:
            for event in pygame.event.get():
                # check if the user wants to quit the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                # check if the user clicks anywhere on this page
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # get the position of the mouse
                    click = pygame.mouse.get_pos()
                    # if the user clicks the button
                    if (0 <= click[0] <= 60) & (665 <= click[1] <= 700):
                        pygame.mixer.Sound.play(click_sound)
                        main()

    # if instead the user clicks the game 1/2/3 button
    # create the 2 colored moving squares & 2 grey static squares
    sq1, sq2, goal1, goal2 = createsq(choice, win)

    # the main game loop!!!!!
    run = True
    crash = False  # crash when the two squares ovelap
    puzzlewin = False  # win when the grey squares are covered
    moved = False
    while run:

        # get the positions of the two squares before move
        # in case the two squares crash -- need to back to the last move
        sq1_x, sq1_y = sq1.coords()[0], sq1.coords()[1]
        sq2_x, sq2_y = sq2.coords()[0], sq2.coords()[1]

        for event in pygame.event.get():
            # check if the user wants to close the window
            if event.type == pygame.QUIT:
                run = False

            # check if the user hits the arrow keys
            elif event.type == pygame.KEYDOWN:
                # left button hit
                if event.key == pygame.K_LEFT:
                    sq1.move_left()
                    sq2.move_left()
                    moved = True
                # right button hit
                elif event.key == pygame.K_RIGHT:
                    sq1.move_right()
                    sq2.move_right()
                    moved = True
                # up button hit
                elif event.key == pygame.K_UP:
                    sq1.move_up()
                    sq2.move_up()
                    moved = True
                # down button hit
                elif event.key == pygame.K_DOWN:
                    sq1.move_down()
                    sq2.move_down()
                    moved = True

        # check if the two squares ovelap
        if sq1.coords() == sq2.coords():
            run = False
            crash = True

        # check if the user wins
        elif (sq1.coords() == goal1.coords() and sq2.coords() == goal2.coords()) or\
             (sq1.coords() == goal2.coords() and sq2.coords() == goal1.coords()):
            run = False
            puzzlewin = True

        # refill the window to black in each loop
        win.fill(black)

        # draw things for puzzle1
        if choice == 1:
            pygame.display.set_caption("Super Hard - Level 9")

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
            wall_ver_1 = pygame.image.load("bg2.jpg")
            wall_ver_1_rect = pygame.Rect(46, 246, 8, 208)
            win.blit(wall_ver_1, wall_ver_1_rect, wall_ver_1_rect)
            wall_ver_2_rect = pygame.Rect(246, 46, 8, 608)
            win.blit(wall_ver_1, wall_ver_2_rect, wall_ver_2_rect)
            wall_ver_3_rect = pygame.Rect(446, 46, 8, 408)
            win.blit(wall_ver_1, wall_ver_3_rect, wall_ver_3_rect)
            wall_ver_4_rect = pygame.Rect(646, 46, 8, 208)
            win.blit(wall_ver_1, wall_ver_4_rect, wall_ver_4_rect)
            # walls - horizontal
            wall_hor_1_rect = pygame.Rect(446, 446, 208, 8)
            win.blit(wall_ver_1, wall_hor_1_rect, wall_hor_1_rect)
            wall_hor_2_rect = pygame.Rect(246, 646, 408, 8)
            win.blit(wall_ver_1, wall_hor_2_rect, wall_hor_2_rect)

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
            n3_2 = gameNumber("3", size, white, (3, 2), "right", game)
            n3_2.draw(win)
            n4_1 = gameNumber("4", size, white, (3, 1), "up", game)
            n4_1.draw(win)
            n4_2 = gameNumber("4", size, white, (1, 1), "left", game)
            n4_2.draw(win)

        # draw thing for puzzle2
        elif choice == 2:
            pygame.display.set_caption("Super Super Hard - Level 99")

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
            bg_2_rect = pygame.Rect(196, 50, 14, 150)
            win.blit(bg_1, bg_2_rect, bg_2_rect)
            bg_3_rect = pygame.Rect(346, 50, 14, 300)
            win.blit(bg_1, bg_3_rect, bg_3_rect)
            bg_4_rect = pygame.Rect(210, 346, 150, 14)
            win.blit(bg_1, bg_4_rect, bg_4_rect)
            bg_5_rect = pygame.Rect(196, 346, 14, 300)
            win.blit(bg_1, bg_5_rect, bg_5_rect)
            bg_6_rect = pygame.Rect(496, 50, 14, 311)
            win.blit(bg_1, bg_6_rect, bg_6_rect)
            bg_7_rect = pygame.Rect(500, 346, 150, 14)
            win.blit(bg_1, bg_7_rect, bg_7_rect)
            bg_8_rect = pygame.Rect(350, 496, 300, 14)
            win.blit(bg_1, bg_8_rect, bg_8_rect)
            bg_9_rect = pygame.Rect(346, 496, 14, 150)
            win.blit(bg_1, bg_9_rect, bg_9_rect)
            bg_10_rect = pygame.Rect(646, 50, 14, 150)
            win.blit(bg_1, bg_10_rect, bg_10_rect)
            bg_11_rect = pygame.Rect(500, 646, 150, 14)
            win.blit(bg_1, bg_11_rect, bg_11_rect)

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

        # draw thing for puzzle2
        elif choice == 3:
            pygame.display.set_caption("Super Super Super Hard - Level 999")

            # draw everything:
            # background grid - vertical
            pygame.draw.line(win, grid_color, (50, 50), (50, 650), 4)
            pygame.draw.line(win, grid_color, (170, 50), (170, 650), 4)
            pygame.draw.line(win, grid_color, (290, 50), (290, 650), 4)
            pygame.draw.line(win, grid_color, (410, 50), (410, 650), 4)
            pygame.draw.line(win, grid_color, (530, 50), (530, 650), 4)
            pygame.draw.line(win, grid_color, (650, 50), (650, 650), 4)
            # background grid - horizontal
            pygame.draw.line(win, grid_color, (50, 50), (650, 50), 4)
            pygame.draw.line(win, grid_color, (50, 170), (650, 170), 4)
            pygame.draw.line(win, grid_color, (50, 290), (650, 290), 4)
            pygame.draw.line(win, grid_color, (50, 410), (650, 410), 4)
            pygame.draw.line(win, grid_color, (50, 530), (650, 530), 4)
            pygame.draw.line(win, grid_color, (50, 650), (650, 650), 4)

            # walls - vertical
            wall_ver_1 = pygame.image.load("bg2.jpg")
            wall_ver_1_rect = pygame.Rect(46, 46, 8, 248)
            win.blit(wall_ver_1, wall_ver_1_rect, wall_ver_1_rect)
            wall_ver_2_rect = pygame.Rect(46, 406, 8, 248)
            win.blit(wall_ver_1, wall_ver_2_rect, wall_ver_2_rect)
            wall_ver_3_rect = pygame.Rect(166, 46, 8, 248)
            win.blit(wall_ver_1, wall_ver_3_rect, wall_ver_3_rect)
            wall_ver_4_rect = pygame.Rect(166, 406, 8, 248)
            win.blit(wall_ver_1, wall_ver_4_rect, wall_ver_4_rect)
            wall_ver_5_rect = pygame.Rect(286, 46, 8, 128)
            win.blit(wall_ver_1, wall_ver_5_rect, wall_ver_5_rect)
            wall_ver_6_rect = pygame.Rect(406, 166, 8, 128)
            win.blit(wall_ver_1, wall_ver_6_rect, wall_ver_6_rect)
            wall_ver_7_rect = pygame.Rect(526, 526, 8, 128)
            win.blit(wall_ver_1, wall_ver_7_rect, wall_ver_7_rect)
            wall_ver_8_rect = pygame.Rect(646, 526, 8, 128)
            win.blit(wall_ver_1, wall_ver_8_rect, wall_ver_8_rect)
            # # walls - horizontal
            wall_ver_1_rect = pygame.Rect(406, 46, 248, 8)
            win.blit(wall_ver_1, wall_ver_1_rect, wall_ver_1_rect)
            wall_hor_2_rect = pygame.Rect(406, 166, 248, 8)
            win.blit(wall_ver_1, wall_hor_2_rect, wall_hor_2_rect)
            wall_hor_3_rect = pygame.Rect(166, 286, 248, 8)
            win.blit(wall_ver_1, wall_hor_3_rect, wall_hor_3_rect)
            wall_hor_4_rect = pygame.Rect(526, 286, 128, 8)
            win.blit(wall_ver_1, wall_hor_4_rect, wall_hor_4_rect)
            wall_hor_5_rect = pygame.Rect(166, 406, 488, 8)
            win.blit(wall_ver_1, wall_hor_5_rect, wall_hor_5_rect)
            wall_hor_6_rect = pygame.Rect(286, 526, 248, 8)
            win.blit(wall_ver_1, wall_hor_6_rect, wall_hor_6_rect)
            wall_hor_7_rect = pygame.Rect(286, 646, 128, 8)
            win.blit(wall_ver_1, wall_hor_7_rect, wall_hor_7_rect)

            # draw the numbers
            size = 40
            game = 3
            n1_1 = gameNumber("1", size, white, (1, 3), "left", game)
            n1_1.draw(win)
            n1_2 = gameNumber("1", size, white, (3, 1), "up", game)
            n1_2.draw(win)
            n2_1 = gameNumber("2", size, white, (1, 5), "down", game)
            n2_1.draw(win)
            n2_2 = gameNumber("2", size, white, (4, 5), "down", game)
            n2_2.draw(win)
            n3_1 = gameNumber("3", size, white, (2, 5), "down", game)
            n3_1.draw(win)
            n3_2 = gameNumber("3", size, white, (5, 4), "right", game)
            n3_2.draw(win)
            n4_1 = gameNumber("4", size, white, (2, 1), "up", game)
            n4_1.draw(win)
            n4_2 = gameNumber("4", size, white, (5, 2), "right", game)
            n4_2.draw(win)
            n5_1 = gameNumber("5", size, white, (1, 1), "up", game)
            n5_1.draw(win)
            n5_2 = gameNumber("5", size, white, (5, 5), "down", game)
            n5_2.draw(win)
            n6_1 = gameNumber("6", size, white, (5, 1), "right", game)
            n6_1.draw(win)
            n6_2 = gameNumber("6", size, white, (5, 3), "right", game)
            n6_2.draw(win)

        # draw other things
        goal1.draw()
        goal2.draw()

        # if the two squares ovelap, do not display them on the surface
        if not crash:
            sq1.draw()
            sq2.draw()

        # update the display window in each loop
        pygame.display.update()

        # check if the two squares are on top of each other
        if crash:
            # play sound effect
            pygame.mixer.Sound.play(crash_sound)
            # move the squares back to their last position
            sq1.x, sq1.y = sq1_x, sq1_y
            sq2.x, sq2.y = sq2_x, sq2_y
            sq1.draw()
            sq2.draw()
            pygame.display.update()

            crash = False
            run = True
            moved = False

        # check if the user wins
        elif puzzlewin:
            # play sound effect
            pygame.mixer.Sound.play(win_sound)
            pygame.time.delay(1000)
            main()

        elif moved:
            # play sound effect
            pygame.mixer.Sound.play(move_sound)
            moved = False

    # quit pygame
    pygame.quit()
    # quit python
    quit()


main()
