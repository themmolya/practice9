import pygame
import os

pygame.mixer.init()

music_folder = "music"
tracks = os.listdir(music_folder)
index = 0

def play():
    global index
    if len(tracks) == 0:
        print("No music files!")
        return

    file_path = os.path.join(music_folder, tracks[index])
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def next_track():
    global index
    index = (index + 1) % len(tracks)
    play()

def prev_track():
    global index
    index = (index - 1) % len(tracks)
    play()

def get_track_name():
    if len(tracks) == 0:
        return "No track"
    return tracks[index]

def get_position():
    return pygame.mixer.music.get_pos() // 1000