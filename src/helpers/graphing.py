import matplotlib.pyplot as plt
import numpy as np

from PIL import Image
from noise import pnoise1, pnoise2

WIDTH, HEIGHT = SIZE = (1024, 1024)

SEED = np.random.randint(0, 100)
SCALE = .5
OCTAVES = 6
PERSISTENCE = 0.5
LACUNARITY = 2.0

BLUE = [65, 105, 225]
GREEN = [34, 139, 34]
BEACH = [238, 214, 175]
SNOW = [255, 250, 250]
MOUNTAIN = [139, 137, 137]


def get_y(x_off, height, seed):
    y = pnoise1(x_off, base=seed)

    y *= height
    return y


def rgb_norm(world):
    world_min = np.min(world)
    world_max = np.max(world)
    norm = lambda x: (x - world_min / (world_max - world_min)) * 255
    return np.vectorize(norm)


def prep_world(world):
    norm = rgb_norm(world)
    world = norm(world)
    return world


def draw():
    # plt.style.use('_mpl-gallery')

    # make data
    # x = np.linspace(0, WIDTH, WIDTH)
    # y = 4 + 2 * np.sin(2 * x)
    # y = np.zeros(WIDTH)
    x_axis = []
    y_axis = []
    x_off = 0
    for x in range(WIDTH):
        x_axis.append(x)

        y = get_y(x_off, HEIGHT, SEED)
        # print(y)
        y_axis.append(y)
        x_off += 0.02

    # y = 0

    # plot
    fig, ax = plt.subplots()
    ax.plot(x_axis, y_axis, linewidth=2.0)

    # ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
    #        ylim=(0, 8), yticks=np.arange(1, 8))

    plt.show()


def draw_world():
    world = np.zeros(SIZE)
    # make coordinate grid on [1,0]^2
    x_idx = np.linspace(0, 1, SIZE[0])
    y_idx = np.linspace(0, 1, SIZE[1])
    world_x, world_y = np.meshgrid(x_idx, y_idx)

    # apply perlin noise, instead of np.vectorize, consider using itertools.starmap
    world = np.vectorize(pnoise2)(world_x / SCALE,
                                  world_y / SCALE,
                                  octaves=OCTAVES,
                                  persistence=PERSISTENCE,
                                  lacunarity=LACUNARITY,
                                  repeatx=WIDTH,
                                  repeaty=HEIGHT,
                                  base=SEED)
    return world


def to_image(world):
    # here was the error: one needs to normalize the image first. Could be done without copying the array, though
    # img = np.floor((world + .5) * 255).astype(np.uint8)  # <- normalize world first
    # img = np.floor((world + 1) * 127).astype(np.uint8)  # <- normalize world first
    # return Image.fromarray(img, mode='L')
    return Image.fromarray(prep_world(world).astype(np.uint8))


def add_color(world):
    color_world = np.zeros(world.shape + (3,))
    for i in range(SIZE[0]):
        for j in range(SIZE[1]):
            if world[i][j] < -0.05:
                color_world[i][j] = BLUE
            elif world[i][j] < 0:
                color_world[i][j] = BEACH
            elif world[i][j] < 0.20:
                color_world[i][j] = GREEN
            elif world[i][j] < 0.35:
                color_world[i][j] = MOUNTAIN
            elif world[i][j] < 1.0:
                color_world[i][j] = SNOW

    return color_world


if __name__ == '__main__':
    world = draw_world()
    color_world = add_color(world).astype(np.uint8)
    Image.fromarray(color_world, 'RGB').show()
    # to_image(color_world).show()
