#!/usr/bin/env python3

import core


def main(options):
    acc = 0
    for data in core.load_input(options.filename):
        ...
        pass

    return acc


if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 9] Sol. part two is: {sol}')
