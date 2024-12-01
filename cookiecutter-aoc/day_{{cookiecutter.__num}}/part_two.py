#!/usr/bin/env python3

from core import get_options, load_input


def main(options):
    data = load_input(options.filename)
    ...  # Calcula sol aqui
    sol = len(data)
    
    print(f'[Day {{ cookiecutter.num }}] Sol. part two is: {sol}')


if __name__ == '__main__':
    main(get_options())
