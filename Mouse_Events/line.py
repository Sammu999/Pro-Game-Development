import pygame

pygame.init()

screen=pygame.display.set_mode((800, 600))

WHITE=(255, 255, 255)
BLACK=(0, 0, 0)

screen.fill(WHITE)

start_pos=None
end_pos=None

running=True
while running:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = pygame.mouse.get_pos()
            #end_pos = start_pos

        # elif event.type == pygame.MOUSEMOTION:
        #     screen.fill(WHITE)
        #     if start_pos is not None:
        #      end_pos = pygame.mouse.get_pos()

        elif event.type == pygame.MOUSEBUTTONUP:
            end_pos = pygame.mouse.get_pos()

            if start_pos is not None:
                pygame.draw.line(screen, BLACK, start_pos, end_pos, 3)

    pygame.display.update()

pygame.quit()