import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sprite Charcter")

class Cars(pygame.sprite.Sprite):
    def __init__(self,img,size,x,y):
        pygame.sprite.Sprite.__init__(self)
        #super().__init__()
        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image,size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y = self.rect.y - 30


blue_car = Cars(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Car_Racing\blue_car.png",(20,60),200,300)
green_car = Cars(r"C:\Users\samra\Desktop\JetLearn\Pro-Game Development\Car_Racing\green_car.png",(25,60),450,500)

cars = pygame.sprite.Group()
cars.add(blue_car)
cars.add(green_car)

    

running = True
while running:
    screen.fill("blue")
    #screen.blit(blue_car.image,blue_car.rect)
    cars.draw(screen)
    cars.update()
    pygame.display.update()

    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()