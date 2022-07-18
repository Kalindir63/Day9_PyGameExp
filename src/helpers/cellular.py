import random

import matplotlib.pyplot as plt
import numpy as np
import random

from PIL import Image
from noise import pnoise1, pnoise2

# walls will be 0
# floors will be 1
WALL = 0
FLOOR = 1


def display_cave(matrix):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            char = '#' if matrix[i][j] == WALL else '.'
            print(char, end='')
        print()


def generate_initial_map(shape, fill_prob):
    level = np.ones(shape)
    for i in range(shape[0]):
        # for each col
        for j in range(shape[1]):
            # choose a number between 0-1
            choice = random.uniform(0, 1)
            # choose a wall or a floor
            level[i][j] = WALL if choice < fill_prob else FLOOR

    return level


def iterate_level(new_map, shape, generation):
    for i in range(shape[0]):
        for j in range(shape[1]):
            # get the number of walls 1 away from each index
            # get the number of walls 2 away from each index
            submap = new_map[
                     max(i - 1, 0):min(i + 2, new_map.shape[0]),
                     max(j - 1, 0):min(j + 2, new_map.shape[1])
                     ]
            wallcount_1away = len(np.where(submap.flatten() == WALL)[0])
            submap = new_map[
                     max(i - 2, 0):min(i + 3, new_map.shape[0]),
                     max(j - 2, 0):min(j + 3, new_map.shape[1])
                     ]
            wallcount_2away = len(np.where(submap.flatten() == WALL)[0])

            # this consolidates walls for the first 5 generations build a
            # scaffolding of walls
            if generation < 5:
                # if looking 1 away in all directions you see 5 or more walls
                # consolidate this point into a wall, if that doesn't happen
                # and if looking 2 away in all directions you see less than
                # 7 walls, add a wall, this consolidates and adds walls
                if wallcount_1away >= 5 or wallcount_2away <= 7:
                    new_map[i][j] = WALL
                else:
                    new_map[i][j] = FLOOR

                if i == 0 or j == 0 or i == shape[0] - 1 or j == shape[1] - 1:
                    new_map[i][j] = WALL

            # this consolidates open space, fills in standalone walls,
            # after generation 5 consolidate walls and increase walking space
            # if there are more than 5 walls nearby make that point a wall,
            # otherwise add a floor
            else:
                # if looking away in all directions you see 5 walls
                # consolidate this point into a wall
                if wallcount_1away >= 5:
                    new_map[i][j] = WALL
                else:
                    new_map[i][j] = FLOOR

    return new_map


if __name__ == '__main__':
    # the cave should be 42x42
    shape = (42, 42)

    # create a random map choosing walls 40% of the time
    # floors 60% of the time
    fill_prob = 0.4

    new_map = generate_initial_map(shape, fill_prob)
    generations = 6
    for generation in range(generations):
        new_map = iterate_level(new_map, shape, generation)

    display_cave(new_map)
