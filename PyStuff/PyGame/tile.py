import pygame


class Tile:
    def __init__(self, widht, height, bgcolor, walkable, breakable):
        self.widht = widht
        self.height = height
        self.bgcolor = bgcolor
        self.walkable = walkable
        self.breakable = breakable

    def setAdjacentUpTile(self, tile):
        self.tileup = tile

    def setAdjacentDownTile(self, tile):
        self.tiledown = tile

    def setAdjacentLeftTile(self, tile):
        self.tileleft = tile

    def setAdjacentRightTile(self, tile):
        self.tileright = tile
