import pygame
pygame.init()



WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))

bg_image = pygame.image.load(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Recycle_Marathon\images\bg_image.png")

class Bin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load (r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Recycle_Marathon\images\bin.png")
        self.rect = self.image.get_rect()

bin = Bin()


running = True
while running:

    screen.blit(bg_image,(0,0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()




