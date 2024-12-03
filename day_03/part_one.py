#!/usr/bin/env python3

import re

from core import get_options, load_input


pat_mul = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')


def main(options) -> int:
    acc = 0
    for line in load_input(options.filename):
        for n1, n2 in pat_mul.findall(line):
            acc += int(n1) * int(n2)
    return acc


if __name__ == '__main__':
    sol = main(get_options())
    print(f'[Day 3] Sol. part one is: {sol}')
