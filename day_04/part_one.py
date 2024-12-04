#!/usr/bin/env python3

import core

WORD = 'XMAS'


def main(options):
    acc = 0
    cols, rows, data = core.load_input(options.filename)

    # By rows
    for sequence in core.iterate_by_rows(cols, rows, data):
        text = core.as_string(sequence)
        acc += text.count(WORD)
        acc += text[::-1].count(WORD)
    # By cols
    for sequence in core.iterate_by_cols(cols, rows, data):
        text = core.as_string(sequence)
        acc += text.count(WORD)
        acc += text[::-1].count(WORD)

    # Up -> Down
    for sequence in core.iterate_diagonal_down(cols, rows, data):
        text = core.as_string(sequence)
        acc += text.count(WORD)
        acc += text[::-1].count(WORD)

    # Down -> Up
    for sequence in core.iterate_diagonal_up(cols, rows, data):
        text = core.as_string(sequence)
        acc += text.count(WORD)
        acc += text[::-1].count(WORD)

    return acc


if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 4] Sol. part one is: {sol}')
