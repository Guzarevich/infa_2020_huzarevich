import pygame
from pygame.draw import *


# После импорта библиотеки, необходимо её инициализировать:
pygame.init()

# И создать окно:
screen = pygame.display.set_mode((400, 400))

# здесь будут рисоваться фигуры
FPS = 30

x1 = 100; y1 = 100
x2 = 300; y2 = 200
N = 10
color = (255, 255, 255)
rect(screen, color, (x1, y1, x2 - x1, y2 - y1), 2)
h = (x2 - x1) // (N + 1)
x = x1 + h
for i in range(N):
    line(screen, color, (x, y1), (x, y2))
    x += h

# после чего, чтобы они отобразились на экране, экран нужно обновить:
pygame.display.update()
clock = pygame.time.Clock()

# Эту же команду нужно будет повторять, если на экране происходят изменения.

# Наконец, нужно создать основной цикл, в котором будут отслеживаться
# происходящие события.
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

# в конце необходимо выйти из программы
pygame.quit()
