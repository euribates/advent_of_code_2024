#!/usr/bin/env python3

import core


def main(options):
    acc = 0
    world = core.load_input(options.filename)
    world.show_world()
    return acc


if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 16] Sol. part one is: {sol}')
