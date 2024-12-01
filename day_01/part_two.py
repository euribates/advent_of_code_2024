#!/usr/bin/env python3

from collections import Counter

from core import get_options, load_input


def main(options):
    '''Day 1, part 2.
    '''
    first_list = []
    counter = Counter()
    for _a, _b in load_input(options.filename):
        first_list.append(_a)
        counter[_b] += 1
    acc = 0
    for num in first_list:
        acc += (num * counter[num])
    print(f'[Day 2] Sol. part two is: {acc}')


if __name__ == '__main__':
    main(get_options())
