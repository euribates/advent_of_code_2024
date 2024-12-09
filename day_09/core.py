#!/usr/bin/env python3

import argparse
import itertools


def get_mark(num: int) -> str:
    if num is None:
        return '.'
    MARKS = (
        '0123456789'
        '█▓▒░▛▜▙▟▄▀'
        'αβγδεζηθικλμξπρτφψ'
        'aábcdeéfghiíjklmnñoópqrstuvwxyz'
        'AÁBCDEÉFGHIÍJKLMNÑOÓPQRSTUVWXYZ'
        '•⊙⊚⊛◉○◌◍◎●◘。☉⦾⦿◆◇◈★☆❖⋄✤✱✲✦✧'
        )
    return MARKS[num % len(MARKS)]


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


class Node:

    def __init__(self, num_blocks: int, id_file=None):
        self.num_blocks = num_blocks
        self.id_file = id_file

    def is_free(self):
        return self.id_file is None

    def is_file(self):
        return not self.is_free()

    def __str__(self):
        if self.is_free():
            return f'{self.num_blocks} free'
        return f'{self.num_blocks} owned by file {self.id_file}'

    __repr__ = __str__


class Directory():

    def __init__(self):
        self.total_blocks = 0
        self.total_files = 0
        self.nodes = []
        self.files = {}

    def add_file(self, id_file, num_blocks):
        self.total_blocks += num_blocks
        self.total_files += 1
        self.files[id_file] = len(self.nodes)
        self.nodes.append(Node(num_blocks, id_file))

    def add_free(self, num_blocks):
        self.total_blocks += num_blocks
        self.nodes.append(Node(num_blocks))

    def first(self, condition=lambda x: True, default=None):
        for index, item in enumerate(self.nodes):
            if condition(item):
                return index, item
        return -1, default

    def last(self, condition=lambda x: True, default=None):
        index = len(self.nodes) - 1
        while index >= 0:
            item = self.nodes[index]
            if condition(item):
                return index, item
            index = index - 1
        return -1, default

    def free_space(self) -> int:
        return sum(_.num_blocks for _ in self.nodes if _.is_free())

    def signature(self) -> str:
        buff = []
        acc = 0
        for node in self.nodes:
            acc += node.num_blocks
            mark = get_mark(node.id_file)
            buff.append(mark * node.num_blocks)
        buff.insert(0, f'{acc}|')
        return ''.join(buff)

    def dump(self):
        print(f'Total num. of files: {self.total_files}')
        print(f'Total num. of blocks: {self.total_blocks}')
        print(f'Free space (in blocks): {self.free_space()}')
        print(f'Signature: {self.signature()}')
        print('-------- ------------------------- --------------')
        for index, node in enumerate(self.nodes):
            bar = get_mark(node.id_file) * node.num_blocks
            print(f'{index:8} {node.num_blocks:25} {bar} {node.num_blocks}')
        print('-------- ------------------------- -------------- ')

    def no_adjacent_gaps(self):
        for (n1, n2) in itertools.pairwise(self.nodes):
            if n1.id_file is None and n2.id_file is None:
                self.dump()
                return False
        return True

    def checksum(self):
        acc = 0
        index = 0
        for node in self.nodes:
            if node.is_file():
                for _ in range(node.num_blocks):
                    acc += index * node.id_file
                    index += 1
            else:
                index += node.num_blocks
        return acc


def load_input(filename: str):
    with open(filename) as f_input:
        line = f_input.readline().strip()
        for id_file, tupla in enumerate(batched(line, 2)):
            blocks = int(tupla[0])
            empty = int(tupla[1]) if len(tupla) == 2 else 0
            yield (id_file, blocks, empty or None)
