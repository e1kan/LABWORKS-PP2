import pygame

pygame.init()
a = int(input("Select the width of the display: "))
b = int(input("Select the length of the display: "))
surface = pygame.display.set_mode((a, b))
pygame.display.set_caption("Crazy Circle")
x, y = a//2, b//2
done = False

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and y - 25 >= 0: y -= 20
        if pressed[pygame.K_DOWN] and y + 25 <= b: y += 20
        if pressed[pygame.K_LEFT] and x - 25 >= 0: x -= 20
        if pressed[pygame.K_RIGHT] and x + 25 <= a: x += 20

        surface.fill((255, 255, 255))

        pygame.draw.circle(surface, (255, 0, 0), (x, y), 25, 0)
        pygame.display.flip()
        clock.tick(20)
