import pygame
import os

pygame.init()

screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Music Player")

music_folder = "music"
tracks = os.listdir(music_folder)
index = 0

def play_music():
    global index
    if len(tracks) == 0:
        print("No files!")
        return

    file_path = os.path.join(music_folder, tracks[index])
    print("Playing:", file_path)

    os.startfile(file_path)  # ең стабильный вариант

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_music()

            elif event.key == pygame.K_n:
                index = (index + 1) % len(tracks)

            elif event.key == pygame.K_b:
                index = (index - 1) % len(tracks)

            elif event.key == pygame.K_q:
                running = False

    screen.fill((200, 200, 200))
    pygame.display.flip()

pygame.quit()