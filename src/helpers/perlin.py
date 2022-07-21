import math

import numpy as np
from noise import pnoise2

WIDTH, HEIGHT = SIZE = (160, 90)
SEED = np.random.randint(0, 100)
# SEED = 80
print(SEED)


def clamp(value, lower=0, upper=1):
    return lower if value < lower else upper if value > upper else value


def scale(value, target_scale: tuple[int, int], current_scale: tuple[int, int] = (0, 1)):
    y = target_scale[0] + (target_scale[1] - target_scale[0]) * \
        ((value - current_scale[0]) / (current_scale[1] - current_scale[0]))
    return y

class PerlinNoiseMap:
    """
    Perlin Noise map based off of https://pastebin.com/xnbsYSSw
    """

    def __init__(self, map_size: tuple[int, int], perlin_seed: int):
        self.p_seed = perlin_seed
        self.tileset = {}
        self.tile_groups = {}

        self.prefab_plains = None
        self.prefab_forest = None
        self.prefab_hills = None
        self.prefab_mountains = None

        self.map_width, self.map_height = map_size
        self.noise_grid = np.zeros(map_size, dtype=int)
        self.tile_grid = np.zeros(map_size, dtype=str)

        # recommend 4 to 20
        self.magnification = 7.0

        self.x_offset = 0
        self.y_offset = 0

    def Start(self):
        self.CreateTileset()
        self.CreateTileGroups()
        self.GenerateMap()

    def CreateTileset(self):
        """Collect and assign ID codes to the tile prefabs, for ease of access.
            Best ordered to match land elevation."""
        # self.tileset[0] = self.prefab_plains
        # self.tileset[1] = self.prefab_forest
        # self.tileset[2] = self.prefab_hills
        # self.tileset[3] = self.prefab_mountains

        tiles = 'Ñ@#W$9876543210?!abc;:+=-,._ '

        # Test tileset
        for idx, char in enumerate(tiles[::-1]):
            self.tileset[idx] = char

    def CreateTileGroups(self):
        """Create empty gameobjects for grouping tiles of the same type, ie
            forest tiles"""
        for prefab_pair in self.tileset.items():
            pass

    def GenerateMap(self) -> None:
        """Generate a 2D grid using the Perlin noise function, storing it as
            both raw ID values and tile gameobjects"""
        for x in range(self.map_width):
            for y in range(self.map_height):
                tile_id = self.GetIdUsingPerlin(x, y)
                self.noise_grid[x][y] = tile_id
                self.CreateTile(tile_id, x, y)

        # print(self.noise_grid)

    def GetIdUsingPerlin(self, x, y) -> int:
        """Using a grid coordinate input, generate a Perlin noise value to be
            converted into a tile ID code. Rescale the normalised Perlin value
            to the number of tiles available."""
        tileset_count = len(self.tileset.keys())
        raw_perlin = pnoise2(
            (x - self.x_offset) / self.magnification,
            (y - self.y_offset) / self.magnification,
            base=self.p_seed)
        # print(raw_perlin)

        clamp_perlin = clamp(raw_perlin)
        # print(clamp_perlin, tileset_count)

        # scaled_perlin = clamp_perlin * tileset_count
        scaled_perlin = scale(clamp_perlin, (1, tileset_count))
        # print(scaled_perlin)

        if int(scaled_perlin) == tileset_count:
            scaled_perlin = tileset_count - 1

        # print(scaled_perlin)
        return math.floor(scaled_perlin)

    def CreateTile(self, tile_id: int, x: int, y: int) -> None:
        """Creates a new tile using the type id code, group it with common
            tiles, set it's position and store the gameobject"""
        tile = self.tileset[tile_id]
        self.tile_grid[x][y] = tile

    def DisplayRawValues(self):
        self._PrintGrid(self.noise_grid)

    def DisplayTileGrid(self):
        self._PrintGrid(self.tile_grid)

    @staticmethod
    def _PrintGrid(grid):
        for x in range(grid.shape[0]):
            for y in range(grid.shape[1]):
                print(grid[x][y], end='')
            print()


if __name__ == '__main__':
    pn = PerlinNoiseMap(SIZE, SEED)
    pn.Start()
    # pn.DisplayRawValues()
    pn.DisplayTileGrid()
