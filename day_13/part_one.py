#!/usr/bin/env python3

import core


def find_solution(machine):
    for a in range(1, 100):
        for b in range(1, 100):
            if machine.check(a, b):
                return (a, b)


def main(options):
    acc = 0
    for i, machine in enumerate(core.load_input(options.filename), start=1):
        if machine.is_solvable():
            sol = find_solution(machine)
            if sol is None:
                continue
            a, b = sol
            if options.trace:
                print(f'Sol. for machine {i} is a = {a}, b = {b}', flush=True)
            acc += (3 * a + b)
    return acc


if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 13] Sol. part one is: {sol}')
