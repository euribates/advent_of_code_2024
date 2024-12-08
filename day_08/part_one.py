#!/usr/bin/env python3

import core
import itertools

def main(options):
    acc = 0
    world, antennas = core.load_input(options.filename)
    world.show_world()
    if options.trace:
        print('Antenas:', ''.join(list(antennas)))
    antinodes = world.copy()
    for antenna, positions in antennas.items():
        for v1, v2 in itertools.combinations(positions, 2):
            for n in core.get_antinodes(v1, v2):
                if antinodes.is_inside(n.x, n.y):
                    if antinodes.at(n.x, n.y) != '#':
                        acc += 1
                        antinodes.at(n.x, n.y, '#')
    antinodes.show_world()
    return acc


if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 8] Sol. part one is: {sol}')
