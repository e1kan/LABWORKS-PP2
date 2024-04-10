def draw_painting(paints, x):
    for i in range(len(paints)):
        if x == 'line':
            pygame.draw.circle(screen, paints[i][0], paints[i][1], paints[i][2])
        if x == 'circle':
            pygame.draw.circle(screen, paints[i][0], paints[i][1], paints[i][2])
        if x == 'rectangle':
            pygame.draw.rect(screen, paints[i][0], paints[i][1], paints[i][2])

run = True
while run:
    timer.tick(fps)
    screen.fill('white')

    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    if mouse[1] > 70:
        pygame.draw.circle(screen, active_color, mouse, active_size)
    if left_click and mouse[1] > 70:
        painting.append((active_color, mouse, active_size))
    draw_painting(painting, mode)

    brushes, colors, rgbs = draw_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[0].collidepoint(event.pos):
                    active_size = 15
                    mode = 'line'
                if brushes[1].collidepoint(event.pos):
                    active_color = 'white'
                    mode = 'line'
                if brushes[2].collidepoint(event.pos):
                    mode = 'rectangle'
                if brushes[3].collidepoint(event.pos):
                    mode = 'circle'


            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgbs[i]


    pygame.display.flip()