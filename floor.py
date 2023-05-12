import tile


class Floor:
    def __init__(self, widht, height):
        newtile = tile.Tile(widht, height, "GREEN", True, False)
        self.tile = newtile
