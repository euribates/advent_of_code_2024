#!/usr/bin/env python3

import core


def find_regions(world):
    non_visited = list(world.all_nodes())
    visited = set()
    while frontier:
        x, y, letter = frontier.pop(0)
        initial = core.Vector(x, y)
        frontier = [initial]
        while frontier:
            current = frontier.pop(0)
            visited.add(current)

            current = []
            region = set([current])



    
def main(options):
    acc = 0
    world = core.load_input(options.filename)
    world.show_world()
    return acc


if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 12] Sol. part one is: {sol}')
