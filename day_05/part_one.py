#!/usr/bin/env python3

import core


def main(options):
    acc = 0
    rules, instructions = core.load_input(options.filename)
    for pages in instructions:
        is_ok = core.is_valid(rules, pages)
        if options.trace:
            print(f'Pages {pages}: {is_ok}')
        if is_ok:
            acc += pages[len(pages) // 2]
    return acc


if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 5] Sol. part one is: {sol}')
