#!/usr/bin/env python3

import argparse
import typing
import dataclasses


def get_options():
    parser = argparse.ArgumentParser(prog='AOC day 16')
    parser.add_argument('filename')
    parser.add_argument('-t', '--trace', action='store_true')
    return parser.parse_args()


@dataclasses.dataclass(frozen=True)
class Vector2:

    x: int = 0
    y: int = 0

    def __rerp__(self):
        return f'Vector2({self.x!r}, {self.y!r})'

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: int):
        return Vector2(self.x * scalar, self.y * scalar)

    def copy(self):
        return Vector2(x=self.x, y=self.y)

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


UP = Vector2(0, -1)
RIGHT = Vector2(1, 0)
DOWN = Vector2(0, 1)
LEFT = Vector2(-1, 0)


Direction = typing.Literal[UP, RIGHT, DOWN, LEFT]


def as_direction(direction: Direction) -> str:
    match (direction.x, direction.y):
        case 0, -1:
            return '^'
        case 1, 0:
            return '>'
        case 0, 1:
            return 'v'
        case -1, 0:
            return '<'
        case _:
            raise ValueError(f'Direction {direction} must be a unit vector')


def direction(char: str) -> Direction:
    match char:
        case '^':
            return UP
        case '>':
            return RIGHT
        case 'v':
            return DOWN
        case '<':
            return LEFT
        case _:
            raise ValueError('Direction must be ^, >, v or <')


class World:

    def __init__(self, lines=None):
        self.start = Vector2()
        self.target = Vector2()
        self.lines = []
        self.width = 0
        self.height = 0
        self.direction = RIGHT
        if lines:
            for line in lines:
                self.add_line(line)

    def add_line(self, line: str):
        self.lines.append(list(line))
        self.height += 1
        self.width = max(self.width, len(line))
    
    @classmethod
    def from_file(cls, filename):
        result = cls()
        with open(filename) as f_input:
            for y, line in enumerate(f_input):
                line = line.strip()
                result.add_line(line)
                for x, char in enumerate(line):
                    if char == 'S':
                        result.start = Vector2(x, y)
                    elif char == 'E':
                        result.target = Vector2(x, y)
        return result

    def __str__(self):
        buff = []
        for (y, row) in enumerate(self.lines):
            for (x, cell) in enumerate(row):
                pos = Vector2(x, y)
                if self.start == pos:
                    buff.append('S')
                elif self.target == pos:
                    buff.append('E')
                else:
                    buff.append(cell)
            buff.append("\n")
        return ''.join(buff)

    def copy(self):
        result = World()
        result.lines = copy.deepcopy(self.lines)
        result.start = self.start
        result.target = self.target
        result.direction = self.direction
        result.width = self.width
        result.height = self.height
        return result

    def is_inside(self, pos: Vector2) -> bool:
        return (0 <= pos.x < self.width) and (0 <= pos.y < self.height)

    def is_out(self, pos: Vector2) -> bool:
        return not self.is_inside(pos)

    def at(self, pos: Vector2, value=None):
        if self.is_out(pos):
            return '#'
        if value:
            self.lines[pos.y][pos.x] = value
        return self.lines[pos.y][pos.x]

    def show_world(self, caption='', bot=None, direction=None):
        if caption:
            print(caption)
        print(f'- Size in {self.width} x {self.height}')
        print(f'- Start at {self.start}')
        print(f'- Target at {self.target}')
        print(f'- Direction {self.direction} : {as_direction(self.direction)}')
        print(self)

    def neighbors(self, origin: Vector2):
        yield from (v for v in origin.adyacents() if self.is_inside(v))

    def all_nodes(self):
        for (y, row) in enumerate(self.lines):
            for (x, cell) in enumerate(row):
                yield (Vector2(x, y), cell)

    def can_move(self) -> bool:
        return self.at(self.current + self.direction) in 'S.E'

    def move(self, bot, direction):
        self.current += self.direction


def load_input(filename: str):
    return World.from_file(filename)
