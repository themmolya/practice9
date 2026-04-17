import pygame
from player import play, stop, next_track, prev_track, get_track_name, get_position

pygame.init()

screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play()
            elif event.key == pygame.K_s:
                stop()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_b:
                prev_track()
            elif event.key == pygame.K_q:
                running = False

    screen.fill((30, 30, 30))

    # Трек аты
    track_text = font.render("Track: " + get_track_name(), True, (255, 255, 255))
    screen.blit(track_text, (20, 50))

    # Уақыт
    pos = get_position()
    time_text = font.render("Time: " + str(pos) + " sec", True, (200, 200, 200))
    screen.blit(time_text, (20, 120))

    # Кнопкалар
    help_text = font.render("P-Play S-Stop N-Next B-Back Q-Quit", True, (150,150,150))
    screen.blit(help_text, (20, 200))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()