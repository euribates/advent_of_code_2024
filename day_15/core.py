#!/usr/bin/env python3

import argparse
import typing
import copy
import dataclasses
from enum import Flag


def get_options():
    parser = argparse.ArgumentParser(prog='AOC day 15')
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
        self.lines = []
        self.width = 0
        self.height = 0
        if lines:
            for line in lines:
                self.add_line(line)

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
            return '#'
        if value:
            self.lines[pos.y][pos.x] = value
        return self.lines[pos.y][pos.x]

    def show_world(self, caption='', bot=None, direction=None):
        if caption:
            print(caption)
        print(f'- Size in {self.width} x Height {self.height}')
        if bot:
            print(f'- Bot at {bot}')
        if direction:
            print(f'- Direction {direction} : {as_direction(direction)}')

        for (y, row) in enumerate(self.lines):
            for (x, cell) in enumerate(row):
                if bot and bot.x == x and bot.y == y:
                    if direction:
                        print(as_direction(direction), end='')
                    else:
                        print('@', end='')
                else:
                    print(cell, end='')
            print()

    def find_by_value(self, value):
        for (y, row) in enumerate(self.lines):
            for (x, cell) in enumerate(row):
                if value == cell:
                    yield Vector2(x, y)

    def neighbors(self, origin: Vector2):
        yield from (v for v in origin.adyacents() if self.is_inside(v))

    def all_nodes(self):
        for (y, row) in enumerate(self.lines):
            for (x, cell) in enumerate(row):
                yield (Vector2(x, y), cell)

    def can_move(self, bot, direction) -> int:
        assert self.at(bot) == '@'
        next_place = bot + direction
        distance = 1
        while self.is_inside(next_place):
            item = self.at(next_place)
            if item == '.':
                return distance
            elif item == '#':
                return 0
            next_place = next_place + direction
            distance  += 1
        return distance

    def move(self, bot, direction):
        start = bot.copy()
        assert self.at(bot) == '@'
        distance = self.can_move(bot, direction)
        if distance == 0:
            return bot, False

        target = bot + direction * distance
        assert self.at(target) == '.'
        for _ in range(distance):
            item = self.at(target - direction)
            self.at(target, item)
            target = target - direction
        self.at(start, '.')
        return bot + direction, True


@dataclasses.dataclass
class MoveCommand:
    position: Vector2
    direction: Direction

    def __str__(self):
        return f'Move {self.position} {as_direction(self.direction)}'

    def trace(self, world):
        symbol = world.at(self.position)
        pos = f'{self.position.x}, {self.position.y}'
        target = self.position + self.direction
        return (
            f'Move {symbol} at {pos}'
            f' {as_direction(self.direction)}'
            f' to {target.x}, {target.y}'
            f' over {world.at(self.position + self.direction)}'
            )

    def apply_to(self, world):
        source_item = world.at(self.position)
        next_pos = self.position + self.direction
        target_item = world.at(next_pos)
        assert target_item == '.'
        world.at(next_pos, source_item)
        world.at(self.position, target_item)


def expand_line(line: str) -> list:
    """
    To get the wider warehouse's map, start with your original
    map and, for each tile, make the following changes:

    If the tile is #, the new map contains ## instead.
    If the tile is O, the new map contains [] instead.
    If the tile is ., the new map contains .. instead.
    If the tile is @, the new map contains @. instead.

    """
    for char in line:
        match char:
            case '.':
                yield '.'
                yield '.'
            case 'O':
                yield '['
                yield ']'
            case '@':
                yield '@'
                yield '.'
            case '#':
                yield '#'
                yield '#'
            case _:
                raise ValueError(f'Invalid character {char}')


def expand_world(world: World) -> World:
    """
    This will produce a new warehouse map which is twice as wide
    and with wide boxes that are represented by []. (The robot
    does not change size.)

    """
    new_world = world.copy()
    for index, line in enumerate(world.lines):
        new_world.lines[index] = list(expand_line(line))
    new_world.width *= 2
    return new_world


def expand_bot(pos: Vector2) -> Vector2:
    return Vector2(pos.x * 2, pos.y)


def make_space(
        world: World,
        position: Vector2,
        direction: Direction,
        queue: typing.Deque,
        ) -> bool:
    next_pos = position + direction
    item = world.at(next_pos)
    if item == '.':
        return True
    elif item == '#':
        return False
    elif item in '[]':
        if direction in {LEFT, RIGHT}:
            queue.append(MoveCommand(next_pos, direction))
            return make_space(world, next_pos, direction, queue)
        elif direction in {UP, DOWN}:
            if item == ']':
                side_pos = next_pos + LEFT
            else:
                side_pos = next_pos + RIGHT
            queue.append(MoveCommand(side_pos, direction))
            queue.append(MoveCommand(next_pos, direction))
            return (
                make_space(world, side_pos, direction, queue)
                and make_space(world, next_pos, direction, queue)
                )
        else:
            raise ValueError(
                f'Impossible movement {direction}'
                f' at position: {position}.'
                )


def load_input(filename: str):
    world = World()
    steps = []
    bot = Vector2()
    with open(filename) as f_input:
        for y, line in enumerate(f_input):
            line = line.strip()
            if '@' in line:
                x = line.index('@')
                bot = Vector2(x, y)
            if line == '':
                break
            world.add_line(line)
        for line in f_input:
            line = line.strip()
            steps.extend([direction(c) for c in line])
    return world, steps, bot
