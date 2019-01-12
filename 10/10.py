#! /usr/bin/env python3

import re
import os
from time import sleep

TICKS = 1000000

def read_input():
    file = open('./input.txt').read().splitlines()
    return [((int(pos_x), int(pos_y), int(vel_x), int(vel_y))) for pos_x, pos_y, vel_x, vel_y
        in [re.findall(r'-?\d+', line) for line in file]]

def visualize(points):
    xs, ys, vxs, vys = zip(*points)

    for tick in range(TICKS):
        current_x = [xs + tick * vxs for xs, vxs in zip(xs, vxs)]
        current_y = [ys + tick * vys for ys, vys in zip(ys, vys)]
        max_X, min_X, max_Y, min_Y = max(current_x), min(current_x), max(current_y), min(current_y)

        if (max_X - min_X) * (max_Y - min_Y) < 175**2:
            print_matrix(points, max_X, max_Y, min_X, min_Y, tick)


def print_matrix(points, max_X, max_Y, min_X, min_Y, tick):
    os.system('clear')
    dx = max_X - min_X
    dy = max_Y - min_Y
    matrix = [[' '] * (dx + 1) for _ in range(dy + 1)]

    for xs, ys, vxs, vys in points:
        matrix[ys + tick * vys - min_Y][xs + tick * vxs - min_X] = '*'

    for row in matrix:
        print(''.join(row))
    print('t = {}'.format(tick))
    sleep(0.5)

if __name__ == "__main__":
    points = read_input()
    visualize(points)

