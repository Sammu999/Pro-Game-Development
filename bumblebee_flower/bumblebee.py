import pygame
import random
pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bumblebee and the Flower")
bee = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\bumblebee_flower\bee.jpg")
flower = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\bumblebee_flower\flower.jpg")
bee = pygame.transform.scale(bee, (60, 60))
flower = pygame.transform.scale(flower, (80, 80))

bee_rect = bee.get_rect()
bee_rect.center = (WIDTH//2, HEIGHT//2)

flower_rect = flower.get_rect()
flower_rect.center = (random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50))
score = 0
font = pygame.font.SysFont(None, 48)

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((135, 206, 250)) 

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bee_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        bee_rect.x += 5
    if keys[pygame.K_UP]:
        bee_rect.y -= 5
    if keys[pygame.K_DOWN]:
        bee_rect.y += 5

    if bee_rect.colliderect(flower_rect):
        score += 1
        flower_rect.center = (random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50))

    screen.blit(bee, bee_rect)
    screen.blit(flower, flower_rect)

    score_text = font.render(f"Score: {score}",True, (0, 0, 0))
    screen.blit(score_text, (20, 20))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
