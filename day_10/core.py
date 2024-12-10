#!/usr/bin/env python3

import argparse
import copy
import dataclasses


def get_options():
    parser = argparse.ArgumentParser(prog='AOC day 10')
    parser.add_argument('filename')
    parser.add_argument('-t', '--trace', action='store_true')
    return parser.parse_args()


@dataclasses.dataclass(frozen=True)
class Vector2:
    x: int = 0
    y: int = 0

    def up(self):
        return Vector2(self.x, self.y - 1)

    def down(self):
        return Vector2(self.x, self.y + 1)

    def left(self):
        return Vector2(self.x - 1, self.y)

    def right(self):
        return Vector2(self.x + 1, self.y)

    def adyacents(self):
        yield self.left()
        yield self.down()
        yield self.right()
        yield self.up()


class World:

    def __init__(self):
        self.lines = []
        self.width = 0
        self.height = 0

    def copy(self):
        result = World()
        result.lines = copy.deepcopy(self.lines)
        result.width = self.width
        result.height = self.height
        return result

    def add_line(self, line: str):
        self.lines.append(list(line))
        self.height += 1
        self.width = max(self.width, len(line))

    def is_inside(self, pos: Vector2) -> bool:
        return (0 <= pos.x < self.width) and (0 <= pos.y < self.height)

    def is_out(self, pos: Vector2) -> bool:
        return not self.is_inside(pos)

    def at(self, pos: Vector2, value=None):
        if self.is_out(pos):
            return '.'
        if value:
            self.lines[pos.y][pos.x] = value
        return self.lines[pos.y][pos.x]

    def show_world(self, caption=''):
        if caption:
            print(caption)
        print(f'Width: {self.width} x Height {self.height}')
        for (y, row) in enumerate(self.lines):
            for (x, cell) in enumerate(row):
                print(cell, end='')
            print()

    def find_by_value(self, value):
        for (y, row) in enumerate(self.lines):
            for (x, cell) in enumerate(row):
                if value == cell:
                    yield Vector2(x, y)

    def neighbors(self, origin: Vector2):
        yield from (v for v in origin.adyacents() if self.is_inside(v))


def distance(v1: Vector2, v2: Vector2) -> int:
    return abs(v2.x - v1.x) - abs(v2.y - v1.y)


def load_input(filename: str):
    world = World()
    with open(filename) as f_input:
        for y, line in enumerate(f_input):
            line = line.strip()
            world.add_line([int(c) for c in line])
    return world
