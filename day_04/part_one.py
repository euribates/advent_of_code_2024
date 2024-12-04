#!/usr/bin/env python3

import core


def main(options):
    acc = 0
    cols, rows, data = core.load_input(options.filename)
    from icecream import ic; ic(cols)
    from icecream import ic; ic(rows)
    from icecream import ic; ic(len(data))

    assert data[0, 0] == 'A'
    assert data[1, 0] == 'B'

    # print('Right -> Left:')
    # for sequence in core.iterate_by_cols(cols, rows, data):
        # for (x, y, char) in sequence:
            # print(data[x, y], sep=' ', end='')
        # print()

    # print('Left -> Right:')
    # for sequence in core.iterate_by_cols(cols, rows, data):
        # for (x, y, char) in reversed(sequence):
            # print(data[x, y], sep=' ', end='')
        # print()

    # print('Up -> Down')
    # for sequence in core.iterate_by_rows(cols, rows, data):
        # for (x, y, char) in sequence:
            # print(data[x, y], sep=' ', end='')
        # print()

    # print('Down -> Up')
    # for sequence in core.iterate_by_rows(cols, rows, data):
        # for (x, y, char) in reversed(sequence):
            # print(data[x, y], sep=' ', end='')
        # print()

    print('Up/Left -> Down/Right')
    for sequence in core.iterate_diagonal_down(cols, rows, data):
        from icecream import ic; ic(len(sequence))
        for (x, y, char) in sequence:
            print(char, end='')
        print()

    return acc


if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 4] Sol. part one is: {sol}')
