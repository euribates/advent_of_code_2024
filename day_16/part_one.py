#!/usr/bin/env python3

import core


def main(options):
    acc = 0
    world, start, target = core.load_input(options.filename)
    return core.a_star(world, start, target)


if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 16] Sol. part one is: {sol}')
