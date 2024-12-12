#!/usr/bin/env python3

import core


def perimeter(world, positions, letter):
    result = len(positions) * 4
    for pos in positions:
        for neighbor in world.neighbors(pos):
            if world.at(neighbor) == letter:
                result = result - 1
    return result


def main(options):
    acc = 0
    world = core.load_input(options.filename)
    world.show_world()
    for region, area in world.find_regions():
        acc = acc + len(area) * perimeter(world, area, region)
    return acc


if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 12] Sol. part one is: {sol}')
