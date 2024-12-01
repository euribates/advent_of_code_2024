#!/usr/bin/env python3

from core import get_options, load_input
from core import expand


def main(options):
    data = load_input(options.filename)
    sol = len(list(data))

    
    print(f'[Day {{ cookiecutter.num }}] Sol. part one is: {sol}')




if __name__ == '__main__':
    main(get_options())
