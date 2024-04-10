import pygame

pygame.init()

fps = 60
timer = pygame.time.Clock()
WIDTH = 800
HEIGHT = 600
active_size = 0
active_color = 'white'
active_tool = 'line'

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Paint")
painting = []


def draw_menu():
    pygame.draw.rect(screen, 'gray', [0, 0, WIDTH, 70])
    pygame.draw.line(screen, 'black', (0, 70), (WIDTH, 70), 3)

    line_brush = pygame.draw.rect(screen, 'black', [10, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (35, 35), 5)

    eraser_brush = pygame.draw.rect(screen, 'black', [70, 10, 50, 50])
    pygame.draw.circle(screen, 'red', (95, 35), 5)

    rectangle_figure = pygame.draw.rect(screen, 'black', [130, 10, 50, 50])
    pygame.draw.rect(screen, 'white', pygame.Rect(145, 25, 20, 20))

    circle_figure = pygame.draw.rect(screen, 'black', [190, 10, 50, 50])
    pygame.draw.circle(screen, 'white', (215, 35), 20)

    brush_list = [line_brush, eraser_brush, rectangle_figure, circle_figure]

    blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 35, 10, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 35, 35, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 60, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 60, 35, 25, 25])
    teal = pygame.draw.rect(screen, (0, 255, 255), [WIDTH - 85, 10, 25, 25])
    purple = pygame.draw.rect(screen, (255, 0, 255), [WIDTH - 85, 35, 25, 25])
    grey = pygame.draw.rect(screen, (128, 128, 128), [WIDTH - 110, 10, 25, 25])
    black = pygame.draw.rect(screen, (0, 0, 0), [WIDTH - 110, 35, 25, 25])

    color_rect = [blue, red, green, yellow, teal, purple, grey, black]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0),
                (0, 255, 255), (255, 0, 255), (128, 128, 128), (0, 0, 0)]

    return brush_list, color_rect, rgb_list

def draw_painting(paints):
    for paint in paints:
        color, pos, size, shape = paint
        if shape == 'circle':
            pygame.draw.circle(screen, color, pos, size, 1)
        elif shape == 'line':
            pygame.draw.circle(screen, color, pos, size)
        elif shape == 'rectangle':
            x, y = pos
            pygame.draw.rect(screen, color, (x, y, size, size))


run = True
while run:
    timer.tick(fps)
    screen.fill('white')

    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    if mouse[1] > 70:
        if active_tool == 'line':
            pygame.draw.circle(screen, active_color, mouse, active_size)
        elif active_tool == 'rectangle':
            pygame.draw.rect(screen, active_color, (mouse[0], mouse[1], active_size, active_size))
        elif active_tool == 'circle':
            pygame.draw.circle(screen, active_color, mouse, active_size, 2)
    if left_click and mouse[1] > 70:
        painting.append((active_color, mouse, active_size, active_tool))

    draw_painting(painting)

    brushes, colors, rgbs = draw_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[0].collidepoint(event.pos):
                    active_size = 15
                    active_tool = 'line'  
                elif brushes[1].collidepoint(event.pos):
                    active_color = 'white'
                    active_tool = 'line'
                elif brushes[2].collidepoint(event.pos):
                    active_tool = 'rectangle'
                elif brushes[3].collidepoint(event.pos):
                    active_tool = 'circle'

            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]

    pygame.display.flip()
