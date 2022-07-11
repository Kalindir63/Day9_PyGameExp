import configparser
from pathlib import Path

import pygame
import pygame.locals

from map.tileCache import TileCache

ASSETS_FOLDER = Path(__file__).parent.parent / "Assets"


class Level(object):
    def __init__(self):
        self.map_tile_height: int = 0
        self.map_tile_width: int = 0
        self.map_height: int = 0
        self.map_width: int = 0
        self.map = []
        self.key = {}
        self.tileset = None
        self.items = {}
        self.MAP_CACHE = None
        self.SPRITE_CACHE = None

    def load_file(self, filename="level.map"):
        parser = configparser.ConfigParser()
        parser.read(filename)
        self.tileset = parser.get('level', 'tileset')
        self.map = parser.get('level', 'map').split('\n')
        for section in parser.sections():
            if len(section) == 1:
                desc = dict(parser.items(section))
                self.key[section] = desc
        self.map_width = len(self.map[0])
        self.map_height = len(self.map)
        self.map_tile_width = int(parser.get('level', 'tile_width'))
        self.map_tile_height = int(parser.get('level', 'tile_height'))
        self.MAP_CACHE = TileCache(self.map_tile_width, self.map_tile_height)

    def get_tile(self, x, y):
        try:
            char = self.map[y][x]
        except IndexError:
            return {}

        try:
            return self.key[char]
        except KeyError:
            return {}

    def get_bool(self, x, y, name):
        """Tell if the specified flag is set for position on the map."""

        value = self.get_tile(x, y).get(name)
        return value in (True, 1, 'true', 'yes', 'True', 'Yes', '1', 'on', 'On')

    def is_wall(self, x, y):
        """Is there a wall?"""

        return self.get_bool(x, y, 'wall')

    def is_blocking(self, x, y):
        """Is this place blocking movement?"""

        if not 0 <= x < self.map_width or not 0 <= y < self.map_height:
            return True
        return self.get_bool(x, y, 'block')

    def render_walls(self, map_x, map_y, overlays):
        wall = self.is_wall
        tiles = self.MAP_CACHE[self.tileset]
        # Draw different tiles depending on neighbourhood
        if not wall(map_x, map_y + 1):
            if wall(map_x + 1, map_y) and wall(map_x - 1, map_y):
                tile = 1, 2
            elif wall(map_x + 1, map_y):
                tile = 0, 2
            elif wall(map_x - 1, map_y):
                tile = 2, 2
            else:
                tile = 3, 2
        else:
            if wall(map_x + 1, map_y + 1) and wall(map_x - 1, map_y + 1):
                tile = 1, 1
            elif wall(map_x + 1, map_y + 1):
                tile = 0, 1
            elif wall(map_x - 1, map_y + 1):
                tile = 2, 1
            else:
                tile = 3, 1
        # Add overlays if the wall may be obscuring something
        if not wall(map_x, map_y - 1):
            if wall(map_x + 1, map_y) and wall(map_x - 1, map_y):
                over = 1, 0
            elif wall(map_x + 1, map_y):
                over = 0, 0
            elif wall(map_x - 1, map_y):
                over = 2, 0
            else:
                over = 3, 0
            overlays[(map_x, map_y)] = tiles[over[0]][over[1]]
        return tile

    def render(self):
        wall = self.is_wall
        tiles = self.MAP_CACHE[self.tileset]
        image = pygame.Surface((self.map_width * self.map_tile_width, self.map_height * self.map_tile_height))
        overlays = {}
        for map_y, line in enumerate(self.map):
            for map_x, c in enumerate(line):
                if not wall(map_x, map_y) and c in self.key and 'sprite' in self.key[c]:
                    try:
                        self.items[(map_x, map_y)] = self.key[c]
                    except (ValueError, KeyError):
                        "nothing to see here"

                if wall(map_x, map_y):
                    tile = self.render_walls(map_x, map_y, overlays)
                else:
                    try:
                        tile = self.key[c]['tile'].split(',')
                        tile = int(tile[0]), int(tile[1])
                    except (ValueError, KeyError):
                        # Default to ground tile
                        tile = 0, 3
                tile_image = tiles[tile[0]][tile[1]]
                image.blit(tile_image, (map_x * self.map_tile_width, map_y * self.map_tile_height))
        return image, overlays


