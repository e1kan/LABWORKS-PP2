import pygame

def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()


def play_previous_song():
    global _songs
    _songs = [_songs[-1]] + [_songs[:-1]]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()

pygame.init()
surface = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Music player")
bg = pygame.image.load(r"C:\Users\Eva\Desktop\hello\University\LabWorks\Lab7\Music\bg.png")
_songs = [r'C:\Users\Eva\Desktop\hello\University\LabWorks\Lab7\Music\haggstorm.mp3',
          r'C:\Users\Eva\Desktop\hello\University\LabWorks\Lab7\Music\sweden.mp3',
          r'C:\Users\Eva\Desktop\hello\University\LabWorks\Lab7\Music\aria_math.mp3',
          r'C:\Users\Eva\Desktop\hello\University\LabWorks\Lab7\Music\subwoofer_lullaby.mp3',]
done = False
playing = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        surface.blit(bg, (0,0))

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]: play_next_song()
        if pressed[pygame.K_LEFT]: play_previous_song()
        if pressed[pygame.K_SPACE] and not playing:
               playing = True
               pygame.mixer.music.play()
        if pressed[pygame.K_SPACE] and playing:
               playing = False
               pygame.mixer.music.stop()


        pygame.display.flip()
