import pygame
import sys
import datetime
import math

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

center = (WIDTH // 2, HEIGHT // 2)

def draw_hand(length, angle, color):
    x = center[0] + length * math.sin(math.radians(angle))
    y = center[1] - length * math.cos(math.radians(angle))
    pygame.draw.line(screen, color, center, (x, y), 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))

    now = datetime.datetime.now()
    sec = now.second
    minute = now.minute

    sec_angle = sec * 6
    min_angle = minute * 6

    pygame.draw.circle(screen, (0, 0, 0), center, 200, 2)

    # 🔥 САНДАР
    font = pygame.font.SysFont(None, 30)

    for i in range(1, 13):
        angle = i * 30
        x = center[0] + 170 * math.sin(math.radians(angle))
        y = center[1] - 170 * math.cos(math.radians(angle))

        text = font.render(str(i), True, (0, 0, 0))
        rect = text.get_rect(center=(x, y))
        screen.blit(text, rect)

    draw_hand(150, sec_angle, (255, 0, 0))
    draw_hand(100, min_angle, (0, 0, 255))

    pygame.display.flip()
    clock.tick(1)