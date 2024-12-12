#!/usr/bin/env python3

import core
from core import Vector2


def perimeter(world, positions, letter):
    xs = [pos.x for pos in positions]
    ys = [pos.y for pos in positions]
    range_x = range(min(xs) - 1,  max(xs) + 1)
    range_y = range(min(ys) - 1, max(ys) + 1)
    acc = 0
    # vertical count
    for x in range_x:
        prev = 0
        for y in range_y:
            new_value = 0
            if world.at(Vector2(x, y)) != world.at(Vector2(x + 1, y)):
                if world.at(Vector2(x, y)) == letter and Vector2(x, y) in positions:
                    new_value = 1
                elif world.at(Vector2(x + 1, y)) == letter and Vector2(x + 1, y) in positions:
                    new_value = -1
            if prev != new_value and new_value != 0:
                acc += 1
            prev = new_value
    # horizontal count
    for y in range_y:
        prev = 0
        for x in range_x:
            new_value = 0
            if world.at(Vector2(x, y)) != world.at(Vector2(x, y + 1)):
                if world.at(Vector2(x, y)) == letter and Vector2(x, y) in positions:
                    new_value = 1
                elif world.at(Vector2(x, y + 1)) == letter and Vector2(x, y + 1) in positions:
                    new_value = -1
            if prev != new_value and new_value != 0:
                acc += 1
            prev = new_value
    return acc


def main(options):
    acc = 0
    world = core.load_input(options.filename)
    world.show_world()
    for letter, area in world.find_regions():
        p = perimeter(world, area, letter)
        size = len(area)
        if options.trace:
            print(f' - A region of {letter} plants with price {size} * {p} = {p * size}')
        acc = acc + size * p
    return acc


if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 12] Sol. part two is: {sol}')
