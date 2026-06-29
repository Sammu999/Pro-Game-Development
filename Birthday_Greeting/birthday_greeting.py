import pygame
import time
pygame.init()
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((255,255,255))
card = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Birthday_Greeting\card.jpg")
cake = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Birthday_Greeting\cake.jpg")
run = True
while run:
    screen.blit(cake,(0,0))
    pygame.display.update()
    time.sleep(3)
    screen.blit(card,(0,0))
    pygame.display.update()
    time.sleep(3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()