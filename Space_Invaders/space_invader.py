import pygame
pygame.init()

WIDTH = 1000
HEIGHT = 600



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader")

space = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Space_Invaders\images\spaceb.png")
space = pygame.transform.scale(space,(WIDTH, HEIGHT))


red_ship = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Space_Invaders\images\spaceship1.png")
yellow_ship = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Space_Invaders\images\spaceship2.png")

red_ship = pygame.transform.scale(red_ship, (60, 60))
yellow_ship = pygame.transform.scale(yellow_ship, (60, 60))

red_ship = pygame.transform.rotate(red_ship, 90)   
yellow_ship = pygame.transform.rotate(yellow_ship, -90)

boundary = pygame.Rect(WIDTH/2-10,0,20,HEIGHT)
MAX_BULLETS = 3
BULLET_SPEED = 2


def red_movement(keys, rect):
    if keys[pygame.K_a] and rect.left > 0 :  # left
        rect.x -= 1
    if keys[pygame.K_d] and rect.right < boundary.left:  # right
        rect.x += 1
    if keys[pygame.K_w]and rect.top > 0:  # up
        rect.y -= 1
    if keys[pygame.K_s] and rect.bottom < HEIGHT:  # down
        rect.y += 1
    

def yellow_movement(keys, rect):
    if keys[pygame.K_LEFT] and rect.left > boundary.right:  # left
        rect.x -= 1
    if keys[pygame.K_RIGHT] and rect.right < WIDTH:  # right
        rect.x += 1
    if keys[pygame.K_UP] and rect.top > 0:  # up
        rect.y -= 1
    if keys[pygame.K_DOWN] and rect.bottom < HEIGHT:  # down
        rect.y += 1


def handle_bullets(red_bullets):
    for bullet in red_bullets:
        pygame.draw.rect(screen,(255,215,0), bullet)
        bullet.x += BULLET_SPEED

def game():
    red_bullets = []
    yellow_bullets = []
    red_rect = red_ship.get_rect()
    yellow_rect = yellow_ship.get_rect()

    red_rect.center = (WIDTH/4, HEIGHT/2)
    yellow_rect.center = (3*WIDTH/4, HEIGHT/2)
    running = True
    while running:
        screen.blit(space, (0, 0))
        pygame.draw.rect(screen,(0,255,255),boundary)
        screen.blit(red_ship, red_rect)
        screen.blit(yellow_ship, yellow_rect)

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red_rect.right,red_rect.y + red_rect.height/2 ,10,5)
                    red_bullets.append(bullet)

                
        keys_pressed = pygame.key.get_pressed()
        red_movement(keys_pressed, red_rect)
        yellow_movement(keys_pressed, yellow_rect)#
        handle_bullets(red_bullets)
        

        pygame.display.update()
                

    
game()

    

