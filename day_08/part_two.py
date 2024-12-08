#!/usr/bin/env python3

import core
import itertools


def main(options):
    acc = 0
    world, antennas = core.load_input(options.filename)
    if options.trace:
        world.show_world()
        print('Antenas:', ''.join(list(antennas)))
    antinodes = world.copy()
    for antenna, positions in antennas.items():
        for v1, v2 in itertools.combinations(positions, 2):
            for n in core.all_antinodes(antinodes, v1, v2):
                if antinodes.at(n.x, n.y) != '#':
                    acc += 1
                    antinodes.at(n.x, n.y, '#')
    if options.trace:
        antinodes.show_world()
    return acc


if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 8] Sol. part two is: {sol}')
