#!/usr/bin/env python3

import core


def main(options):
    acc = 0
    dd = core.Directory()
    for (id_file, blocks, empty) in core.load_input(options.filename):
        dd.add_file(core.FileEntry(id_file, blocks))
        if empty is not None:
            dd.add_free(empty)
    dd.list()
    return acc


if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 9] Sol. part one is: {sol}')
