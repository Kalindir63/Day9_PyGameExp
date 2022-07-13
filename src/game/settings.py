import configparser
from pathlib import Path

filename = 'level.map'

parser = configparser.ConfigParser()
parser.read(filename)

tileset = parser.get('level', 'tileset')

# game setup
WIDTH = int(parser.get('settings', 'width'))
HEIGHT = int(parser.get('settings', 'height'))
FPS = int(parser.get('settings', 'fps'))
TILE_SIZE = int(parser.get('settings', 'tile_size'))

WORLD_MAP = [list(i) for i in parser.get('level', 'map').split('\n')]

SOURCE_ROOT = Path(__file__).parent.parent
