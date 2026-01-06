import tile


class Wall:
    def __init__(self, widht, height):
        newtile = tile.Tile(widht, height, "GRAY", False, False)
        self.tile = newtile
