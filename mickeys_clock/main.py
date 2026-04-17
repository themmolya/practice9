import pygame
import sys
import datetime

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

bg = pygame.image.load("images/mickeyclock.jpeg")
bg = pygame.transform.scale(bg, (500, 500))

left_hand = pygame.image.load("images/left_hand.png").convert_alpha()
right_hand = pygame.image.load("images/right_hand.png").convert_alpha()

# орташа размер
left_hand = pygame.transform.scale(left_hand, (75, 160))
right_hand = pygame.transform.scale(right_hand, (65, 130))

center = pygame.math.Vector2(WIDTH // 2, HEIGHT // 2)

def blit_rotate(surface, image, pos, originPos, angle):
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    offset = pygame.math.Vector2(pos) - image_rect.center

    rotated_offset = offset.rotate(angle)  # 🔥 МІНЕ ОСЫ ЖЕР ДҰРЫС
    rotated_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    rotated_image = pygame.transform.rotate(image, -angle)  # 🔥 ЖӘНЕ ОСЫ
    rotated_rect = rotated_image.get_rect(center=rotated_center)

    surface.blit(rotated_image, rotated_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg, (0, 0))

    now = datetime.datetime.now()
    sec = now.second
    minute = now.minute

    # 🔥 ДҰРЫС БАҒЫТ
    sec_angle = sec * 6
    min_angle = minute * 6

    blit_rotate(
        screen,
        left_hand,
        center,
        (left_hand.get_width() // 2, left_hand.get_height()),
        sec_angle
    )

    blit_rotate(
        screen,
        right_hand,
        center,
        (right_hand.get_width() // 2, right_hand.get_height()),
        min_angle
    )

    pygame.display.flip()
    clock.tick(60)