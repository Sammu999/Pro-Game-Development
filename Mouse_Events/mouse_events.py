import pygame
import random
pygame.init()
HEIGHT = 800
WIDTH = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mouse Events")
screen.fill((0,0,0))

run = True
while run:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen,(255,255,255),pos,5)

        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255,0,0))

        if event.type == pygame.MOUSEBUTTONUP:
            screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

    pygame.display.update()
pygame.quit()



