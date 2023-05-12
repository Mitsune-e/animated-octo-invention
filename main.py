from sys import exit
import pygame
import wall
import floor
pygame.init()


size = width, height = 780, 832
speed = [2, 2]
background_color = "WHITE"

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Explosions')
clock = pygame.time.Clock()


testwall = wall.Wall(52, 52)
wall_surface = pygame.Surface((testwall.tile.widht, testwall.tile.height))
wall_surface.fill(testwall.tile.bgcolor)

testfloor = floor.Floor(52, 52)
floor_surface = pygame.Surface((testfloor.tile.widht, testfloor.tile.height))
floor_surface.fill(testfloor.tile.bgcolor)


def drawrightwall():
    i = 0
    x = 0
    for i in range(16):
        screen.blit(wall_surface, (728, x))
        i += 1
        x += 52


def drawleftwall():
    i = 0
    x = 0
    for i in range(16):
        screen.blit(wall_surface, (0, x))
        i += 1
        x += 52


def drawupperwall():
    i = 0
    y = 0
    # draw left wall collumn
    for i in range(16):
        screen.blit(wall_surface, (y, 0))
        i += 1
        y += 52


def drawbottomwall():
    i = 0
    y = 0
    # draw left wall collumn
    for i in range(16):
        screen.blit(wall_surface, (y, 780))
        i += 1
        y += 52


def drawlevelfloor():
    x = 52
    y = 52
    i = 0
    c = 0
    for i in range(14):
        for c in range(13):
            screen.blit(floor_surface, (x, y))
            x += 52
            c += 1
        i += 1
        x = 52
        y += 52


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # quit the game
            pygame.quit()
            exit()

    screen.fill(background_color)

    drawupperwall()
    drawleftwall()
    drawrightwall()
    drawbottomwall()
    drawlevelfloor()

    pygame.display.update()
    clock.tick(60)
