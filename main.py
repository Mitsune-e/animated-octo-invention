from sys import exit
import pygame
import wall
import floor
pygame.init()


size = width, height = 850, 650
tileX = 50
tileY = 50
speed = [2, 2]
background_color = "WHITE"

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Explosions')
clock = pygame.time.Clock()


testwall = wall.Wall(tileX, tileY)
wall_surface = pygame.Surface((testwall.tile.widht, testwall.tile.height))
wall_surface.fill(testwall.tile.bgcolor)

middlewalls = wall.Wall(tileX, tileY)
middleWall_surface = pygame.Surface(
    (middlewalls.tile.widht, middlewalls.tile.height))
middleWall_surface.fill(middlewalls.tile.bgcolor)

testfloor = floor.Floor(tileX, tileY)
floor_surface = pygame.Surface((testfloor.tile.widht, testfloor.tile.height))
floor_surface.fill(testfloor.tile.bgcolor)


def drawmiddlewalls():
    i = 0
    c = 0
    x = 50
    y = 100
    for c in range(5):
        for i in range(8):
            screen.blit(wall_surface, (x, y))
            i += 1
            x += 100
        x = 50
        c += 1
        y += 100


def drawrightwall():
    i = 0
    x = 0
    for i in range(13):
        screen.blit(wall_surface, (800, x))
        i += 1
        x += 50


def drawleftwall():
    i = 0
    x = 0
    for i in range(13):
        screen.blit(wall_surface, (0, x))
        i += 1
        x += 50


def drawupperwall():
    i = 0
    y = 0
    # draw left wall collumn
    for i in range(17):
        screen.blit(wall_surface, (y, 0))
        i += 1
        y += 50


def drawbottomwall():
    i = 0
    y = 0
    # draw left wall collumn
    for i in range(17):
        screen.blit(wall_surface, (y, 600))
        i += 1
        y += 50


def drawlevelfloor():
    x = 50
    y = 50
    i = 0
    c = 0
    for i in range(11):
        for c in range(15):
            screen.blit(floor_surface, (x, y))
            x += 50
            c += 1
        i += 1
        x = 50
        y += 50


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
    drawmiddlewalls()

    pygame.display.update()
    clock.tick(60)
