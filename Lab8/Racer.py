#imports
import pygame, sys
from pygame.locals import *
import random, time

#initializing pygame
pygame.init()

#setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

#initializing game screen
window_x = 400
window_y = 600

#initializing colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#setting up the display and name
pygame.display.set_caption('Racer')
game_window = pygame.display.set_mode((window_x, window_y))
game_window.fill(WHITE)

#initializing important variables
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0
COINS_GOAL = 3

#setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 12)
game_over = font.render("GAME OVER", True, BLACK)

#loading background
background = pygame.image.load(r"C:\Users\Eva\Desktop\hello\University\LabWorks\Lab8\images\AnimatedStreet.png")

#creating ENEMY class
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Eva\Desktop\hello\University\LabWorks\Lab8\images\enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, window_x - 40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, window_x  - 40), 0)

#creating PLAYER class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Eva\Desktop\hello\University\LabWorks\Lab8\images\player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 540)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < window_x:
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

#creating COIN class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\Eva\Desktop\hello\University\LabWorks\Lab8\images\coin.png")
        self.rect = self.image.get_rect()

    def spawn(self):
        self.rect.centerx = random.randint(40, window_x - 40)
        self.rect.centery = 540

#setting up Sprites
P1 = Player()
E1 = Enemy()

#creating Sprites Groups
coins = pygame.sprite.Group()
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

#spawning a coin
SPAWN_COIN = pygame.USEREVENT + 1
#increasing enemy's speed every second
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#game Loop
while True:
    #handling key events
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5
        if event.type == SPAWN_COIN:
            if len(coins) < 1: #spawning coins only when there are no coins on the road
                new_coin = Coin()
                new_coin.spawn()
                coins.add(new_coin)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #setting up the background and score text
    game_window.blit(background, (0,0))
    scores = font_small.render("score: " + str(SCORE), True, BLACK)
    coins_scores = font_small.render("coins: " + str(COINS_COLLECTED), True, BLACK)
    game_window.blit(scores, (5, 0))
    game_window.blit(coins_scores, (325, 0))

    #moving and re-drawing all Sprites
    for entity in all_sprites:
        game_window.blit(entity.image, entity.rect)
        entity.move()

    #handling enemy and player collision (game over situation)
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.music.stop()
          pygame.mixer.Sound(r"C:\Users\Eva\Desktop\hello\University\LabWorks\Lab8\sounds\crash_racer.wav").play()
          time.sleep(0.5)

          game_window.fill(RED)
          game_window.blit(game_over, (30,250))

          pygame.display.update()
          for entity in all_sprites:
                entity.kill()
          time.sleep(3)
          pygame.quit()
          sys.exit()

    #picking up the coins"
    for coin in coins:
        if pygame.sprite.spritecollideany(P1, coins):
            pygame.mixer.Sound(r"C:\Users\Eva\Desktop\hello\University\LabWorks\Lab8\sounds\pickedcoin.mp3").play()
            COINS_COLLECTED += 1
            coin.kill() #deleting the coin to avoid "infinite coin" bug

    coins.draw(game_window)
    pygame.display.update()
    FramePerSec.tick(FPS)
