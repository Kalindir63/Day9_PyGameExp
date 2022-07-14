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

# ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../Assets/graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# weapons
weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'graphic': '../Assets/graphics/weapons/sword/full.png'},
    'lance': {'cooldown': 400, 'damage': 30, 'graphic': '../Assets/graphics/weapons/lance/full.png'},
    'axe': {'cooldown': 300, 'damage': 20, 'graphic': '../Assets/graphics/weapons/axe/full.png'},
    'rapier': {'cooldown': 50, 'damage': 8, 'graphic': '../Assets/graphics/weapons/rapier/full.png'},
    'sai': {'cooldown': 80, 'damage': 10, 'graphic': '../Assets/graphics/weapons/sai/full.png'}}
