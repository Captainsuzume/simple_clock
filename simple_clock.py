#Captainsuzume 2018
#
#A simple clock written with the pygame library

import pygame
import time
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (250, 250, 250)

pygame.init()

# Set the width and height of the screen [width, height]
size = (600, 600)
screen = pygame.display.set_mode(size)

background = pygame.Surface(screen.get_size())
background = background.convert()

pygame.display.set_caption("Simple Clock")

done = False
clock = pygame.time.Clock()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # background image
    screen.fill(WHITE)

    pygame.draw.circle(screen,BLACK,[300,300],200,5)

    localtime = time.asctime(time.localtime(time.time()))

    #draws the quarters
    pygame.draw.line(screen, BLACK, [300, 100], [300, 120], 10)
    pygame.draw.line(screen, BLACK, [500, 300], [480, 300], 10)
    pygame.draw.line(screen, BLACK, [300, 500], [300, 480], 10)
    pygame.draw.line(screen, BLACK, [100, 300], [120, 300], 10)

    # draws the seconds of the quadrant
    for i in range(0,60,1):
        quadrant_x = 300 + 200 * math.sin(i * 0.0174532925 * 6)
        quadrant_y = 300 - 200 * math.cos(i * 0.0174532925 * 6)
        pygame.draw.line(screen, BLACK, [300, 300], [quadrant_x, quadrant_y], 2)

    #draws the rest of the hours
    for j in range(0,12,1):
        quadrant_x_h = 300 + 200 * math.sin(j * 0.0174532925 * 30)
        quadrant_y_h = 300 - 200 * math.cos(j * 0.0174532925 * 30)
        pygame.draw.line(screen, BLACK, [300, 300], [quadrant_x_h, quadrant_y_h], 6)

    pygame.draw.circle(screen, WHITE, [300, 300], 180, 0)

    #text part
    font = pygame.font.SysFont('Calibri', 40, True, False)
    hour12 = font.render("12", True, BLACK)
    screen.blit(hour12, [282, 70])
    hour1 = font.render("1", True, BLACK)
    screen.blit(hour1, [300, 70])
    hour3 = font.render("3", True, BLACK)
    screen.blit(hour3, [510, 290])
    hour6 = font.render("6", True, BLACK)
    screen.blit(hour6, [292, 510])
    hour9 = font.render("9", True, BLACK)
    screen.blit(hour9, [80, 290])

    hours = localtime[11:13]
    minutes = localtime[14:16]
    seconds =  localtime[17:19]

    # radian = angle * 0.0174532925

    #draws the hours
    coord_x_hrs = 300 + 100 * math.sin((int(hours) + int(minutes)/60) * 0.0174532925 * 30)
    coord_y_hrs = 300 - 100 * math.cos((int(hours) + int(minutes)/60) * 0.0174532925 * 30)
    pygame.draw.line(screen,BLACK,[300,300],[coord_x_hrs,coord_y_hrs],6)

    #draws the minutes
    coord_x_min = 300 + 200 * math.sin(int(minutes) * 0.0174532925 * 6)
    coord_y_min = 300 - 200 * math.cos(int(minutes) * 0.0174532925 * 6)
    pygame.draw.line(screen,BLACK,[300,300],[coord_x_min,coord_y_min],3)

    #draws the seconds
    coord_x_sec = 300 + 200 * math.sin(int(seconds) * 0.0174532925 * 6)
    coord_y_sec = 300 - 200 * math.cos(int(seconds) * 0.0174532925 * 6)
    pygame.draw.line(screen,BLACK,[300,300],[coord_x_sec,coord_y_sec],1)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()