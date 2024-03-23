import pygame
import random
import os

def shuffle():
    global current_song, current_index, _songs
    random_song = random.choice(_songs)
    current_song = os.path.basename(random_song)
    current_index = 5
    pygame.mixer.music.load(random_song)
    pygame.mixer.music.play()

pygame.init()
surface = pygame.display.set_mode((800, 798))
pygame.display.set_caption("Music player")
bg = pygame.image.load(r"C:\Users\Eva\Desktop\hello\University\LabWorks\Lab7\Music\bg.png")
_songs = ['C:\\Users\\Eva\\Desktop\\hello\\University\\LabWorks\\Lab7\Music\\haggstorm.mp3',
          'C:\\Users\\Eva\\Desktop\\hello\\University\\LabWorks\\Lab7\Music\\sweden.mp3',
          'C:\\Users\\Eva\\Desktop\\hello\\University\\LabWorks\\Lab7\Music\\aria_math.mp3',
          'C:\\Users\\Eva\\Desktop\\hello\\University\\LabWorks\\Lab7\\Music\\subwoofer_lullaby.mp3',]
done = False
playing = False
current_index = -1

font = pygame.font.Font(r"C:\Users\Eva\Desktop\hello\University\LabWorks\Lab7\Music\Minecraftia.ttf", 20)

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        surface.blit(bg, (0,0))

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            current_index = (current_index + 1) % len(_songs)
            pygame.mixer.music.load(_songs[current_index])
            pygame.mixer.music.play()
            pygame.time.delay(150)
        if pressed[pygame.K_LEFT]:
            current_index = (current_index - 1) % len(_songs)
            pygame.mixer.music.load(_songs[current_index])
            pygame.mixer.music.play()
            pygame.time.delay(150)
        if pressed[pygame.K_s]:
            shuffle()
            pygame.time.delay(150)
        if pressed[pygame.K_SPACE]:
            if playing:
                pygame.mixer.music.pause()
                playing = False
            else:
                pygame.mixer.music.unpause()
                playing = True
            pygame.time.delay(150)

        if current_index != 5:
            current_song = os.path.basename(_songs[current_index])
        text = font.render(current_song, True, (160, 160, 160))
        surface.blit(text, (177, 663))

        pygame.display.flip()
