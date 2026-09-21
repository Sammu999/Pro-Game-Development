import pygame
import random
pygame.init()
WIDTH = 600
HEIGHT = 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Lane Dodger")
clock = pygame.time.Clock()
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 80, 80)
GREY = (40, 40, 40)
font_small = pygame.font.SysFont("Segoe UI", 28)
font_large = pygame.font.SysFont("Segoe UI", 64)

road_img = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Car_Racing\road_bg.png")
blue_car_img = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Car_Racing\blue_car.png")
red_car_img = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Car_Racing\red_car.png")
yellow_car_img = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Car_Racing\yellow_car.png")
green_car_img = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Car_Racing\green_car.png")
explosion_img = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Car_Racing\explosion.png")
smoke_img = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Car_Racing\smoke.png")
road_img = pygame.transform.scale(road_img, (WIDTH, HEIGHT))
car_width = 70
car_height = 130

blue_car_img = pygame.transform.scale(blue_car_img, (car_width, car_height))
red_car_img = pygame.transform.scale(red_car_img, (car_width, car_height))
red_car_img = pygame.transform.rotate(red_car_img, 180)
yellow_car_img = pygame.transform.scale(yellow_car_img, (car_width, car_height))
yellow_car_img = pygame.transform.rotate(yellow_car_img, 180)
green_car_img = pygame.transform.scale(green_car_img, (car_width, car_height))
green_car_img = pygame.transform.rotate(green_car_img, 180)
explosion_img = pygame.transform.scale(explosion_img, (100, 100))
smoke_img = pygame.transform.scale(smoke_img, (80, 80))

enemy_images = [red_car_img, yellow_car_img,green_car_img]
lane_width = WIDTH // 3
lane_y = HEIGHT - 150   
lane_x_positions = [lane_width * 0.5 - car_width // 2 + 30,lane_width * 1.5 - car_width // 2 + 15,lane_width * 2.5 - car_width // 2]

player_lane = 1
player_rect = blue_car_img.get_rect()
player_rect.centerx = lane_x_positions[player_lane]
player_rect.centery = lane_y

road_y1 = 0
road_y2 = -HEIGHT
road_speed = 6

enemies = []
spawn_timer = 0
spawn_interval = 40   

score = 0
lives = 5             
game_over = False
explosion_timer = 0
smoke_timer = 0

def spawn_enemy():
    lane = random.randint(0, 2)
    img = random.choice(enemy_images)
    rect = img.get_rect()
    rect.centerx = lane_x_positions[lane]
    rect.y = -150
    base_min = 8
    base_max = 12
    speed = random.randint(base_min + score // 300,base_max + score // 300)
    enemies.append([img, rect, speed])

def reset_game():
    global enemies, score, lives, game_over
    global explosion_timer, smoke_timer, player_lane
    enemies = []
    score = 0
    lives = 5
    game_over = False
    explosion_timer = 0
    smoke_timer = 0
    player_lane = 1
    player_rect.centerx = lane_x_positions[player_lane]
    player_rect.centery = lane_y


running = True
reset_game()

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_LEFT and player_lane > 0:
                    player_lane -= 1
                    player_rect.centerx = lane_x_positions[player_lane]

                if event.key == pygame.K_RIGHT and player_lane < 2:
                    player_lane += 1
                    player_rect.centerx = lane_x_positions[player_lane]
            else:
                if event.key == pygame.K_r:
                    reset_game()
                if event.key == pygame.K_ESCAPE:
                    running = False

    road_y1 += road_speed
    road_y2 += road_speed
    if road_y1 >= HEIGHT:
        road_y1 = -HEIGHT
    if road_y2 >= HEIGHT:
        road_y2 = -HEIGHT

    if not game_over:
        score += 1

        spawn_timer += 1
        if spawn_timer >= spawn_interval:
            spawn_enemy()
            spawn_timer = 0
        for enemy in enemies[:]:
            enemy[1].y += enemy[2]
            if enemy[1].top > HEIGHT:
                enemies.remove(enemy)
        for enemy in enemies[:]:
            if enemy[1].colliderect(player_rect):
                enemies.remove(enemy)
                lives -= 1
                explosion_timer = 20
                smoke_timer = 40
                if lives <= 0:
                    game_over = True

    screen.blit(road_img, (0, road_y1))
    screen.blit(road_img, (0, road_y2))

    for enemy in enemies:
        screen.blit(enemy[0], enemy[1])

    screen.blit(blue_car_img, player_rect)

    if explosion_timer > 0:
        exp_rect = explosion_img.get_rect(center=player_rect.center)
        screen.blit(explosion_img, exp_rect)
        explosion_timer -= 1

    if smoke_timer > 0:
        sm_rect = smoke_img.get_rect(center=(player_rect.centerx, player_rect.centery + 40))
        screen.blit(smoke_img, sm_rect)
        smoke_timer -= 1

    hud = pygame.Rect(0, 0, WIDTH, 50)
    pygame.draw.rect(screen, GREY, hud)
    score_text = font_small.render("Score: " + str(score), True, WHITE)
    lives_text = font_small.render("Lives: " + str(lives), True, WHITE)
    screen.blit(score_text, (20, 10))
    screen.blit(lives_text, (WIDTH - 150, 10))
    if game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.fill(BLACK)
        overlay.set_alpha(180)
        screen.blit(overlay, (0, 0))

        title = font_large.render("GAME OVER", True, RED)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//2 - 100))

        final_score = font_small.render("Final Score: " + str(score), True, WHITE)
        screen.blit(final_score, (WIDTH//2 - final_score.get_width()//2, HEIGHT//2))

        hint = font_small.render("Press R to Restart", True, GREY)
        screen.blit(hint, (WIDTH//2 - hint.get_width()//2, HEIGHT//2 + 60))
    pygame.display.update()
pygame.quit()





