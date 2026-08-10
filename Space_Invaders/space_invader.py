import pygame
pygame.init()

WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode ((WIDTH,HEIGHT))
pygame.display.set_caption ("Space Invader")
space = pygame.image.load (r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Space_Invaders\images\spaceb.png")
space = pygame.transform.scale(space,(WIDTH,HEIGHT))

running = True
while running:
    screen.blit(space,(0,0))
    pygame.display.update()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
    

