from gameNumber import gameNumber
from gameText import gameText
from puzzle1 import puzzle1
from puzzle2 import puzzle2
from puzzle3 import puzzle3
import pygame
pygame.init()


def createsq(choice, win):
    """check the puzzle the user wants to play and create squares"""

    grey = (60, 60, 60)
    red = (255, 0, 0)
    blue = (0, 0, 255)

    if choice == 1:
        sq1 = puzzle1(red, 1, 2, win)
        sq2 = puzzle1(blue, 1, 3, win)
        goal1 = puzzle1(grey, 1, 1, win)
        goal2 = puzzle1(grey, 3, 1, win)
        return sq1, sq2, goal1, goal2

    if choice == 2:
        sq1 = puzzle2(red, 1, 2, win)
        sq2 = puzzle2(blue, 1, 3, win)
        goal1 = puzzle2(grey, 1, 1, win)
        goal2 = puzzle2(grey, 3, 1, win)
        return sq1, sq2, goal1, goal2

    if choice == 3:
        sq1 = puzzle3(red, 1, 2, win)
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
    grey = (60, 60, 60)  # color of the two "goals"
    white = (255, 255, 255)  # color of the numbers
    black = (0, 0, 0)  # background color
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    aqua = (0, 255, 255)
    grid_color = (40, 60, 40)
    gold = (100, 100, 0)

    # the loop for the user to choose a puzzle
    choose = True
    choice = 0
    while choose:
        # draw the things on the front page of the game
        title = gameText("The AMAZING Puzzle", 50, aqua, (140, 150), (150, 150, 400, 60), black)

        # the game buttons
        game1 = gameText("Level 9", 32, red, (135, 300), (100, 300, 150, 40), gold)
        game2 = gameText("Level 99", 32, green, (300, 300), (275, 300, 150, 40), gold)
        game3 = gameText("Level 999", 32, blue, (470, 300), (450, 300, 150, 40), gold)
        rule = gameText('Guide', 32, white, (310, 505), (280, 500, 140, 40), gold)

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

            if event.type == pygame.QUIT:
                choose = False
                pygame.quit()
                quit()

            # check if the user click on anywhere in the window
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = pygame.mouse.get_pos()
                # check if the user chooses each puzzle
                # print(click)

                # check if the user chooses puzzle1
                if (100 <= click[0] <= 250) & (300 <= click[1] <= 340):
                    choice += 1
                    choose = False
                    pygame.mixer.Sound.play(click_sound)
                # check if the user chooses puzzle2
                if (275 <= click[0] <= 425) & (300 <= click[1] <= 340):
                    choice += 2
                    choose = False
                    pygame.mixer.Sound.play(click_sound)
                # check if the user chooses puzzle3
                if (450 <= click[0] <= 600) & (300 <= click[1] <= 340):
                    choice += 3
                    choose = False
                    pygame.mixer.Sound.play(click_sound)
                # check if the user chooses rules
                if (280 <= click[0] <= 420) & (500 <= click[1] <= 540):
                    choice += 4
                    choose = False
                    pygame.mixer.Sound.play(click_sound)

    if choice == 4:
        pygame.display.set_caption("Guide")

        T1 = 'How to win?'
        t11 = 'Let the red and blue square overlap the two static grey squares.'
        T2 = 'How to play?'
        t21 = '- Choose a difficulty level from level 9, 99, and 999.'
        t22 = '- Control the movement of the red square and the blue square'
        t23 = ' by hitting the **left, right, up, or down arrow keys** on your keyboard.'
        T3 = 'Rules'
        r11 = '1. The two squares move together (i.e. when you hit up arrow'
        r12 = '   key, both squares will move up a grid)'
        r21 = '2. Stop when hitting a wall. If only one of the square is stoped'
        r22 = '   by the wall, the other one will move normally (this is a '
        r23 = '   strategy you can use to only move one square).'
        r31 = '3. The squares will be **transported by the numbers** around the '
        r32 = '   game board. All the numbers appear in pairs and they are like'
        r33 = '   a channel between two grids. If you move a colored square out'
        r34 = '   r of the board from one number, the square will reappear in '
        r35 = '   the other grid represented by the same number.'
        r41 = '4. No overlap of the two squares.'

        rule1 = gameText(T1, 20, white, (75, 80), (50, 80, 600, 25), black)
        rule2 = gameText(t11, 20, white, (75, 110), (50, 110, 600, 25), black)
        rule3 = gameText(T2, 20, white, (75, 140), (50, 140, 600, 25), black)
        rule4 = gameText(t21, 20, white, (75, 170), (50, 170, 600, 25), black)
        rule5 = gameText(t22, 20, white, (75, 200), (50, 200, 600, 25), black)
        rule6 = gameText(t23, 20, white, (75, 230), (50, 230, 600, 25), black)
        rule7 = gameText(T3, 20, white, (75, 260), (50, 260, 600, 25), black)
        rule8 = gameText(r11, 20, white, (75, 290), (50, 290, 600, 25), black)
        rule9 = gameText(r12, 20, white, (75, 320), (50, 320, 600, 25), black)
        rule10 = gameText(r21, 20, white, (75, 350), (50, 350, 600, 25), black)
        rule11 = gameText(r22, 20, white, (75, 380), (50, 380, 600, 25), black)
        rule12 = gameText(r23, 20, white, (75, 410), (50, 410, 600, 25), black)
        rule13 = gameText(r31, 20, white, (75, 440), (50, 440, 600, 25), black)
        rule14 = gameText(r32, 20, white, (75, 470), (50, 470, 600, 25), black)
        rule15 = gameText(r33, 20, white, (75, 500), (50, 500, 600, 25), black)
        rule16 = gameText(r34, 20, white, (75, 530), (50, 530, 600, 25), black)
        rule17 = gameText(r35, 20, white, (75, 560), (50, 560, 600, 25), black)
        rule18 = gameText(r41, 20, white, (75, 590), (50, 590, 600, 25), black)

        win.fill(black)
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

        pygame.display.update()
        pygame.time.wait(1500)  # 1000 = 1 second
        main()

    # create the 2 colored moving squares & 2 grey static squares
    sq1, sq2, goal1, goal2 = createsq(choice, win)

    # print(choice)

    # the game loop!!!!!
    run = True
    crash = False  # crash when the two squares ovelap
    puzzlewin = False  # win when the grey squares are covered
    moved = False
    while run:

        # get the original position of the two squares in each loop
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

        # check is the user wins
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
        sq1.draw()
        sq2.draw()

        # update the display window in each loop
        pygame.display.update()

        # check if the two squares are on top of each other
        if crash:
            # play sound effect
            pygame.mixer.Sound.play(crash_sound)

            # display the "you lose you stupid" window
            youlose = gameText("Oops... The two squares cannot overlap",
                               25, red, (150, 300), (100, 295, 500, 40), grey)
            back = gameText("back to the last move",
                            25, red, (250, 350), (200, 345, 350, 40), grey)
            youlose.draw(win)
            back.draw(win)
            pygame.display.update()
            pygame.time.wait(1700)  # 1000 = 1 second

            # move the squares back to their last position
            sq1.x, sq1.y = sq1_x, sq1_y
            sq2.x, sq2.y = sq2_x, sq2_y
            sq1.draw()
            sq2.draw()
            pygame.display.update()

            crash = False
            run = True

        # check if the user wins
        elif puzzlewin:
            # play sound effect
            pygame.mixer.Sound.play(win_sound)

            # display the "you win" window
            youwin = gameText("Congrats! You Win!!", 40, red, (190, 300), (150, 300, 400, 50), grey)
            youwin.draw(win)
            pygame.display.update()
            pygame.time.wait(1500)  # 1000 = 1 second
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
