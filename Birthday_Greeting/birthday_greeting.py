import pygame
import time
pygame.init()
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill((255,255,255))
card = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Birthday_Greeting\card.jpg")
card = pygame.transform.scale(card,(WIDTH, HEIGHT))
cake = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Birthday_Greeting\cake.jpg")
cake = pygame.transform.scale(cake,(WIDTH, HEIGHT))
gift = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Birthday_Greeting\gift.jpg")

gift = pygame.transform.scale(gift,(WIDTH, HEIGHT))
font = pygame.font.SysFont("arial",50)
text1 = font.render("Happy Birthday!",True,(0,0,255))


run = True
while run:
    screen.blit(cake,(0,0))
    pygame.display.update()
    time.sleep(3)
    screen.blit(card,(0,0))
    screen.blit(text1, (WIDTH/2-100,HEIGHT/2))
    pygame.display.update()
    time.sleep(3)
    screen.blit(gift,(0,0))
    pygame.display.update()
    time.sleep(3)



   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()