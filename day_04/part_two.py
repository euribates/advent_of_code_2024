#!/usr/bin/env python3

import core


def verificar_candidato(data, x, y):
    """Solo hay 4 posibles combinaciones que deb un X-MAS.
    """
    left_up = data[x-1, y-1]
    right_up = data[x+1, y-1]
    left_down = data[x-1, y+1]
    right_down = data[x+1, y+1]
    if (left_up, right_up, left_down, right_down) == ('M', 'S', 'M', 'S'):
        return 1
    elif (left_up, right_up, left_down, right_down) == ('M', 'M', 'S', 'S'):
        return 1
    elif (left_up, right_up, left_down, right_down) == ('S', 'S', 'M', 'M'):
        return 1
    elif (left_up, right_up, left_down, right_down) == ('S', 'M', 'S', 'M'):
        return 1
    return 0


def main(options):
    acc = 0
    cols, rows, data = core.load_input(options.filename)
    for x in range(1, cols-1):
        for y in range(1, rows-1):
            if data[x, y] == 'A':
                acc += verificar_candidato(data, x, y)
    return acc


if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 4] Sol. part two is: {sol}')
