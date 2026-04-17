import pygame
import sys
from ball import Ball

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

clock = pygame.time.Clock()

# 🔴 Шар
ball = Ball(
    x=WIDTH // 2,
    y=HEIGHT // 2,
    radius=25,
    speed=20,
    width=WIDTH,
    height=HEIGHT
)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # қозғалу
    ball.move(keys)

    # фон
    screen.fill((255, 255, 255))

    # шар
    ball.draw(screen)

    pygame.display.flip()
    clock.tick(30)