import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Infinite Fruit Catcher")
clock = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 80, 80)

font = pygame.font.SysFont("Segoe UI", 40)

# INSERT IMAGE PATHS HERE
background_img = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Fruit_Catcher\images\cartoon_bg.jpg")
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

basket_img = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Fruit_Catcher\images\basket.png")
apple_img = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Fruit_Catcher\images\apple.png")
banana_img = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Fruit_Catcher\images\banana.png")
orange_img = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Fruit_Catcher\images\orange.png")
strawberry_img = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Fruit_Catcher\images\strawberry.png")
watermelon_img = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Fruit_Catcher\images\watermelon.png")
grape_img = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Fruit_Catcher\images\grape.png")
bomb_img = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Fruit_Catcher\images\bomb.png")

apple_img = pygame.transform.scale(apple_img, (50, 50))
banana_img = pygame.transform.scale(banana_img, (50, 50))
orange_img = pygame.transform.scale(orange_img, (50, 50))
strawberry_img = pygame.transform.scale(strawberry_img, (50, 50))
watermelon_img = pygame.transform.scale(watermelon_img, (50, 50))
grape_img = pygame.transform.scale(grape_img, (50, 50))


fruit_images = [apple_img,banana_img,orange_img,strawberry_img,watermelon_img,grape_img]

basket_img = pygame.transform.scale(basket_img, (120, 80))
bomb_img = pygame.transform.scale(bomb_img, (60, 60))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = basket_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.y = HEIGHT - 120

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= 8
        if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - self.rect.width:
            self.rect.x += 8

class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice(fruit_images)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, WIDTH - 80)
        self.rect.y = -100
        self.speed = 6

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()

class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = bomb_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, WIDTH - 80)
        self.rect.y = -100
        self.speed = 6

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()

all_sprites = pygame.sprite.Group()
falling_objects = pygame.sprite.Group()
bombs = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

spawn_timer = 0
spawn_interval = 40
score = 0
game_over = False

def spawn_object():
    if random.randint(1, 7) == 1:
        bomb = Bomb()
        all_sprites.add(bomb)
        falling_objects.add(bomb)
        bombs.add(bomb)
    else:
        fruit = Fruit()
        all_sprites.add(fruit)
        falling_objects.add(fruit)

def reset_game():
    global score, game_over
    score = 0
    game_over = False
    all_sprites.empty()
    falling_objects.empty()
    bombs.empty()
    all_sprites.add(player)
    player.rect.centerx = WIDTH // 2

running = True
reset_game()

while running:
    clock.tick(FPS)

    if not game_over:
        all_sprites.update()

        spawn_timer += 1
        if spawn_timer >= spawn_interval:
            spawn_object()
            spawn_timer = 0

        hits = pygame.sprite.spritecollide(player, falling_objects, False)
        for obj in hits:
            if obj in bombs:
                game_over = True
            else:
                score += 1
            obj.kill()

    screen.blit(background_img, (0, 0))
    all_sprites.draw(screen)

    score_text = font.render(str(score), True, BLACK)
    screen.blit(score_text, (WIDTH - 80, 20))

    if game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.fill(BLACK)
        overlay.set_alpha(180)
        screen.blit(overlay, (0, 0))

        title = font.render("GAME OVER", True, RED)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//2 - 80))

        final_score = font.render("Score: " + str(score), True, WHITE)
        screen.blit(final_score, (WIDTH//2 - final_score.get_width()//2, HEIGHT//2))

        hint = font.render("Press R to Restart", True, WHITE)
        screen.blit(hint, (WIDTH//2 - hint.get_width()//2, HEIGHT//2 + 80))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_over:
                if event.key == pygame.K_r:
                    reset_game()
                if event.key == pygame.K_ESCAPE:
                    running = False

pygame.quit()
