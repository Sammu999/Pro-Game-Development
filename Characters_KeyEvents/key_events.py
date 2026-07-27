import pygame

WIDTH = 800
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH,HEIGHT))
space = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Characters_KeyEvents\images\space.png")
space = pygame.transform.scale(space,(WIDTH,HEIGHT))

rocket_rect = pygame.Rect(WIDTH/2,HEIGHT/2,50,100)
rocket = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Characters_KeyEvents\images\rocket.png")
rocket = pygame.transform.scale(rocket,(50,100))

run=True

while run:
    screen.blit(space,(0,0))
    screen.blit(rocket,(rocket_rect.x,rocket_rect.y))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rocket_rect.y = rocket_rect.y - 10
        


pygame.quit()