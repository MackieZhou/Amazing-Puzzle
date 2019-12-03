from pygame_square import Square
import pygame
pygame.init()


def main():

    win = pygame.display.set_mode(size=(600, 600))
    pygame.display.set_caption("first game")

    cenX = 100
    cenY = 100  # x, y coordinates of the rectangle
    len = 100  # width and height of the rect
    vel = 200  # velocity of the reactangle

    # colors:
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)

    run = True
    while run:
        pygame.time.delay(100)  # 1000 = 1 second

        # get events from the queue:
        # get(eventtype=None) -> Eventlist
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Two key events in pygame: KEYDOWN and KEYUP.
            # These events have an attribute "key" which is
            # an integer representing a key on the keyboard
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cenX -= vel
                elif event.key == pygame.K_RIGHT:
                    cenX += vel
                elif event.key == pygame.K_UP:
                    cenY -= vel
                elif event.key == pygame.K_DOWN:
                    cenY += vel

        win.fill(black)
        sq1 = Square(red, cenX, cenY, len, win)
        sq1.draw()
        pygame.display.update()

    pygame.quit()
    quit()


main()
