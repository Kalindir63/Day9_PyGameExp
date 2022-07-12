from pathlib import Path

import pygame
from pygame.locals import *
from pygame.surface import Surface

ASSETS_FOLDER = Path(__file__).parent.parent / 'Assets'


class TileCache:
    """Load the tilesets lazily into global cache"""

    def __init__(self, width=32, height=None):
        self.width = width
        self.height = height or width
        self.cache = {}

    def __getitem__(self, filename):
        """Return a table of tiles, load it from disk if needed."""
        file = ASSETS_FOLDER / filename
        key = (file, self.width, self.height)
        try:
            return self.cache[key]
        except KeyError:
            tile_table = self._load_tile_table(file, self.width, self.height)
            self.cache[key] = tile_table
            return tile_table

    @staticmethod
    def _load_tile_table(filename, width: int, height: int):
        """Load an image and split it into tiles."""

        image = pygame.image.load(filename).convert()
        image_width, image_height = image.get_size()
        tile_table = []
        for tile_x in range(0, int(image_width / width)):
            line: list[Surface] = []
            tile_table.append(line)
            for tile_y in range(0, int(image_height / height)):
                rect = (tile_x * width, tile_y * height, width, height)
                line.append(image.subsurface(rect))
        return tile_table
