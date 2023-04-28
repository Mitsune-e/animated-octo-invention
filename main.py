from sys import exit
import pygame
pygame.init()


size = width, height = 800, 400
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Explosions')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # quit the game
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
