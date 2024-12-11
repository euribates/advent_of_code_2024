#!/usr/bin/env python3

import core


def evolve(num_list):
    result = []
    for num in num_list:
        result += core.rule(num)
    return result


def main(options):
    acc = 0
    data = list(core.load_input(options.filename))
    for _ in range(25):
        data = evolve(data)
    acc = len(data)
    return acc



if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 11] Sol. part one is: {sol}')
