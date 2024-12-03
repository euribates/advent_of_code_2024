#!/usr/bin/env python3

from core import get_options, load_input


def main(options):
    acc = 0
    for data in load_input(options.filename):
        ...
        pass

    return acc


if __name__ == '__main__':
    sol = main(get_options())
    print(f'[Day {{ cookiecutter.num }}] Sol. part two is: {sol}')
