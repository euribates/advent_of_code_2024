#!/usr/bin/env python3

import heapq

from core import get_options, load_input


def main(options):
    '''Day 1, part 1.
    '''
    heap_zero = []
    heap_one = []
    counter = 0
    for _a, _b in load_input(options.filename):
        heap_zero.append(_a)
        heap_one.append(_b)
        counter += 1
    heapq.heapify(heap_zero)
    heapq.heapify(heap_one)
    acc = 0
    while counter > 0:
        _a = heapq.heappop(heap_zero)
        _b = heapq.heappop(heap_one)
        acc += abs(_b - _a)
        counter -= 1
    print(f'[Day 1] Sol. part one is: {acc}')


if __name__ == '__main__':
    main(get_options())
