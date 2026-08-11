import tile


class Floor:
    def __init__(self, widht, height):
        newtile = tile.Tile(widht, height, "darkolivegreen2", True, False)
        self.tile = newtile
