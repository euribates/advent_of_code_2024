#!/usr/bin/env python3

import re

from core import get_options, load_input


pat_op = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)")


def main(options) -> int:
    acc = 0
    is_enabled = True
    for line in load_input(options.filename):
        for m in pat_op.finditer(line):
            if options.trace:
                print(m, m.group(0))
            g = m.group(0)
            if g.startswith('mul('):
                if is_enabled:
                    acc += int(m.group(1)) * int(m.group(2))
            elif g == "don't()":
                is_enabled = False
            elif g == "do()":
                is_enabled = True
    return acc


if __name__ == '__main__':
    sol = main(get_options())
    print(f'[Day 3] Sol. part two is: {sol}')
