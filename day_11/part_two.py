#!/usr/bin/env python3

import functools
import core


@functools.cache
def evolve(num_list, steps) -> int:
    if steps == 0:
        return len(num_list)
    acc = 0
    for num in num_list:
        acc += evolve(tuple(core.rule(num)), steps-1)
    return acc


def main(options):
    acc = 0
    data = list(core.load_input(options.filename))
    acc = evolve(tuple(data), 75)
    return acc


if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 11] Sol. part two is: {sol}')
