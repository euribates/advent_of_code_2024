#!/usr/bin/env python3

from itertools import tee

from icecream import ic

from core import get_options, load_input


def is_valid(num_list, trace=False):
    is_ascendent = num_list[0] < num_list[-1]
    first_iter, second_iter = tee(num_list, 2)
    next(second_iter)
    if is_ascendent:
        for a, b in zip(first_iter, second_iter):
            if a >= b or (b - a) > 3:
                if trace:
                    ic(a, b, a >= b or (b - a) > 3)
                return False
    else:
        for a, b in zip(first_iter, second_iter):
            if a <= b or (a - b) > 3:
                if trace:
                    ic(a, b, a <= b or (a - b) > 3)
                return False
    return True


def main(options):
    acc = 0
    for data in load_input(options.filename):
        if is_valid(data, options.trace):
            acc += 1
    print(f'[Day 2] Sol. part one is: {acc}')


if __name__ == '__main__':
    main(get_options())
