import pygame
pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Rectangle():
    def __init__(self, colour, dimensions):
        self.colour = colour
        self.dimensions = dimensions

    def draw (self):
        pygame.draw.rect(screen,self.colour,self.dimensions)

rec_1 = Rectangle ((0,0,255), (105,200,50,90))
rec_2 = Rectangle ((180,200,75), (509,600,30,70))
rec_3 = Rectangle ((89,234,10), (700,400,70,100))

running = True
while running:
    rec_1.draw()
    rec_2.draw()
    rec_3.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    pygame.display.update()





