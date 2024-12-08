#!/usr/bin/env python3

import argparse
import copy
import dataclasses
import collections


@dataclasses.dataclass(frozen=True)
class Vector2D:
    x: int
    y: int

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y) 

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y) 


class World:

    def __init__(self):
        self.lines = []
        self.width = 0
        self.height = 0

    def add_line(self, line: str):
        self.lines.append(list(line))
        self.height += 1
        self.width = max(self.width, len(line))

    def is_inside(self, x: int, y: int) -> bool:
        return (0 <= x < self.width) and (0 <= y < self.height)

    def copy(self):
        result = World()
        result.lines = copy.deepcopy(self.lines)
        result.width = self.width
        result.height = self.height
        return result

    def at(self, x, y, value=None):
        if self.is_inside(x, y):
            if value:
                self.lines[y][x] = value
            return self.lines[y][x]
        return '.'

    def show_world(self, caption=''):
        if caption:
            print(caption)
        print(f'Width: {self.width} x Height {self.height}')
        for (y, row) in enumerate(self.lines):
            for (x, cell) in enumerate(row):
                print(cell, end='')
            print()


def get_options():
    parser = argparse.ArgumentParser(prog='AOC day 8')
    parser.add_argument('filename')
    parser.add_argument('-t', '--trace', action='store_true')
    return parser.parse_args()


def load_input(filename: str):
    world = World()
    antennas = collections.defaultdict(list)
    with open(filename) as f_input:
        for y, line in enumerate(f_input):
            line = line.strip()
            world.add_line(line)
            for x, char in enumerate(line):
                if char != '.':
                    antennas[char].append(Vector2D(x=x, y=y))
    return world, antennas


def get_antinodes(v1: Vector2D, v2: Vector2D):
    delta = v2 - v1
    yield v1 - delta
    yield v2 + delta


def all_antinodes(world, v1: Vector2D, v2: Vector2D):
    delta = v1 - v2
    while world.is_inside(v1.x, v1.y):
        yield v1
        v1 = v1 - delta
    while world.is_inside(v2.x, v2.y):
        yield v2
        v2 = v2 + delta
