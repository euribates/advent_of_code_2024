#!/usr/bin/env python3

import argparse
import itertools


class FileEntry:

    def __init__(self, id_file, blocks: int):
        self.id_file = id_file
        self.blocks = blocks


class Directory():

    def __init__(self):
        self.total_blocks = 0
        self.files = {}
        self.free = []

    def add_file(self, file: FileEntry):
        self.total_blocks += file.blocks
        self.files[file.id_file] = file
        self.total_blocks += file.blocks

    def add_free(self, blocks):
        self.total_blocks += blocks
        self.free.append(blocks)

    def free_space(self) -> int:
        return sum(self.free)

    def list(self):
        print(f'Total num. of files: {len(self.files)}')
        print(f'Total num. of blocks: {self.total_blocks}')
        print(f'Free space (in blocks): {self.free_space()}')

        print('      id. file     num. blocks')
        print('-------------- ---------------')
        for id_file in self.files:
            print(f'{id_file:14} {self.files[id_file].blocks:15}') 
        print('-------------- ---------------')


def batched(iterable, n, *, strict=False):
    # batched('ABCDEFG', 3) → ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    iterator = iter(iterable)
    while batch := tuple(itertools.islice(iterator, n)):
        if strict and len(batch) != n:
            raise ValueError('batched(): incomplete batch')
        yield batch


def get_options():
    parser = argparse.ArgumentParser(prog='AOC day 9')
    parser.add_argument('filename')
    parser.add_argument('-t', '--trace', action='store_true')
    return parser.parse_args()


def load_input(filename: str):
    with open(filename) as f_input:
        line = f_input.readline().strip()
        for id_file, tupla in enumerate(batched(line, 2)):
            blocks = int(tupla[0])
            empty = int(tupla[1]) if len(tupla) == 2 else None
            yield (id_file, blocks, empty)
