import pygame
from pygame.draw import *


pygame.init()

screen = pygame.display.set_mode((400, 400))

#set фон work display
screen.fill((224, 224, 224))

FPS = 30

# face
circle(screen, (0, 0, 0), (200, 200), 100)
circle(screen, (255, 255, 51), (200, 200), 99)

# right eye
circle(screen, (0, 0, 0), (160, 180), 20)
circle(screen, (255, 0, 0), (160, 180), 19)
circle(screen, (0, 0, 0), (160, 180), 7)

# left eye
circle(screen, (0, 0, 0), (240, 180), 15)
circle(screen, (255, 0, 0), (240, 180), 14)
circle(screen, (0, 0, 0), (240, 180), 7)

# mouth
rect(screen, (0, 0, 0), [150,250, 100,17])

# left eye-brown
polygon(screen, (0, 0, 0), [(120,100), (195,175), (185,175), (110,110)])

# right eye-brown
polygon(screen, (0, 0, 0), [(210,160), (300,140), (310,149), (220,169)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()
