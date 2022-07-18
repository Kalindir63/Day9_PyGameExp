from PIL import Image
from pathlib import Path

# TODO File Helper
ASSETS_FOLDER = Path(__file__).parent.parent / 'Assets'

def display_image(filename, assets_folder=ASSETS_FOLDER):
    print(assets_folder / filename)
    file = assets_folder / filename
    with Image.open(file) as im:
        im.rotate(45).show()


if __name__ == '__main__':
    display_image('graphics/grass/grass_1.png')
