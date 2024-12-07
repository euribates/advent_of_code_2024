#!/usr/bin/env python3

import core


def main(options):
    acc = 0
    for result, numbers in core.load_input(options.filename):
        for ops in core.operators(len(numbers) - 1):
            if core.get_solution(numbers, ops) == result:
                acc += result
                if options.trace:
                    print(core.show_solution(numbers, ops))
                break
    return acc


if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 7] Sol. part one is: {sol}')
