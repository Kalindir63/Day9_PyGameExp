from pygame import Vector2
from PIL import Image
from PIL import Image
from pathlib import Path
import random

import matplotlib.pyplot as plt
import numpy as np
import random
from noise import pnoise1

WIDTH, HEIGHT = SIZE = (160, 90)
SEED = random.randint(0, 100)


class PerlinNoiseMap:
    """
    Perlin Noise map based off of https://pastebin.com/xnbsYSSw
    """

    def __init__(self, map_size):
        self.tileset = {}
        self.tile_groups = {}

        self.prefab_plains = None
        self.prefab_forest = None
        self.prefab_hills = None
        self.prefab_mountains = None

        self.map_width, self.map_height = map_size
        self.noise_grid = np.zeros(map_size)
        self.tile_grid = np.zeros(map_size)

        # recommend 4 to 20
        self.maginification = 7.0

        self.x_offset = 0
        self.y_offset = 0

    def Start(self):
        self.CreateTileset()
        self.CreateTileGroups()
        self.GenerateMap()

    def CreateTileset(self):
        """Collect and assign ID codes to the tile prefabs, for ease of access.
            Best ordered to match land elevation."""
        self.tileset[0] = self.prefab_plains
        self.tileset[1] = self.prefab_forest
        self.tileset[2] = self.prefab_hills
        self.tileset[3] = self.prefab_mountains

    def CreateTileGroups(self):
        """Create empty gameobjects for grouping tiles of the same type, ie
            forest tiles"""
        for prefab_pair in self.tileset.items():
            pass

    def GenerateMap(self):
        pass


if __name__ == '__main__':
    PerlinNoiseMap(SIZE)
