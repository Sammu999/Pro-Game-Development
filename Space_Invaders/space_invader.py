import pygame
pygame.init()

WIDTH = 1330
HEIGHT = 800

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

RED_HIT = pygame.USEREVENT + 1
YELLOW_HIT = pygame.USEREVENT + 2

BULLET_LAUNCH = pygame.mixer.Sound(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Space_Invaders\sounds\Grenade.mp3")
SHIP_HIT = pygame.mixer.Sound(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Space_Invaders\sounds\gun.mp3")

red_lives = 10
yellow_lives = 10
font = pygame.font.SysFont(None, 40)

def red_movement(keys, rect):
    if keys[pygame.K_a] and rect.left > 0:
        rect.x -= 1
    if keys[pygame.K_d] and rect.right < boundary.left:
        rect.x += 1
    if keys[pygame.K_w] and rect.top > 0:
        rect.y -= 1
    if keys[pygame.K_s] and rect.bottom < HEIGHT:
        rect.y += 1

def yellow_movement(keys, rect):
    if keys[pygame.K_LEFT] and rect.left > boundary.right:
        rect.x -= 1
    if keys[pygame.K_RIGHT] and rect.right < WIDTH:
        rect.x += 1
    if keys[pygame.K_UP] and rect.top > 0:
        rect.y -= 1
    if keys[pygame.K_DOWN] and rect.bottom < HEIGHT:
        rect.y += 1

def handle_bullets(red_bullets, yellow_bullets, red_rect, yellow_rect):
    for bullet in yellow_bullets:
        pygame.draw.rect(screen,(255,0,0), bullet)
        bullet.x -= BULLET_SPEED
        
        if bullet.colliderect(red_rect):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
            print ("RED SPACESHIP HIT")
        elif bullet.x < 0:
            yellow_bullets.remove(bullet)


    for bullet in red_bullets:
        pygame.draw.rect(screen,(255,215,0), bullet)
        bullet.x += BULLET_SPEED
        
        if bullet.colliderect(yellow_rect):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            red_bullets.remove(bullet)


def game():
    red_bullets = []
    yellow_bullets = []
    red_rect = red_ship.get_rect()
    yellow_rect = yellow_ship.get_rect()
    red_rect.center = (WIDTH/4, HEIGHT/2)
    yellow_rect.center = (3*WIDTH/4, HEIGHT/2)
    red_lives = 10
    yellow_lives = 10


    running = True
    while running:
        screen.blit(space, (0, 0))
        pygame.draw.rect(screen,(0,255,255),boundary)
        screen.blit(red_ship, red_rect)
        screen.blit(yellow_ship, yellow_rect)

        red_text = font.render("Lives: " + str(red_lives), True, (255,255,255))
        yellow_text = font.render("Lives: " + str(yellow_lives), True, (255,255,255))

        screen.blit(red_text, (10, 10))
        screen.blit(yellow_text, (WIDTH - 150, 10))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red_rect.right, red_rect.centery - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_LAUNCH.play()

                if (event.key == pygame.K_RSHIFT) and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow_rect.left - 10, yellow_rect.centery - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_LAUNCH.play()


            if event.type == RED_HIT:
                red_lives -= 1
                SHIP_HIT.play()
                
            if event.type == YELLOW_HIT:
                yellow_lives -= 1
                SHIP_HIT.play()

        message = ""
        if red_lives == 0:
            message = "Yellow wins!"

        if yellow_lives == 0:
            message = "Red wins!"

        if message != "":
            message = font.render (message,True,(0,255,255))
            screen.blit(message,(WIDTH/2-message.get_width()/2, HEIGHT/2-message.get_height()/2))
            pygame.display.update()
            pygame.time.delay(5000)
            break
            
            
        


        keys_pressed = pygame.key.get_pressed()
        red_movement(keys_pressed, red_rect)
        yellow_movement(keys_pressed, yellow_rect)
        handle_bullets(red_bullets, yellow_bullets, red_rect, yellow_rect)
        pygame.display.update()
    game()
game()


    

