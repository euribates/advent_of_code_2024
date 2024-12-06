#!/usr/bin/env python3

import dataclasses
from copy import deepcopy
import argparse
from enum import Flag


class Direction(Flag):

    NORTH = 1
    EAST = 2
    SOUTH = 4
    WEST = 8

    @classmethod
    def create(cls, char: str):
        match char:
            case '^':
                return cls.NORTH
            case '>':
                return cls.EAST
            case 'v':
                return cls.SOUTH
            case '<':
                return cls.WEST

    def __str__(self):
        match self.value:
            case 1:
                return '^'
            case 2:
                return '>'
            case 4:
                return 'v'
            case 8:
                return '<'


@dataclasses.dataclass
class Player:
    x: int = 0
    y: int = 0
    facing: Direction = Direction.NORTH

    def __str__(self):
        return str(self.facing)

    def copy(self):
        return Player(self.x, self.y, self.facing)

    def forward(self, world) -> bool:
        x = self.x
        y = self.y
        match self.facing:
            case Direction.NORTH:
                y -= 1
            case Direction.EAST:
                x += 1
            case Direction.SOUTH:
                y += 1
            case Direction.WEST:
                x -= 1
        if world.at(x, y) == '.':
            world.at(self.x, self.y, '.')
            self.x = x
            self.y = y
            world.at(self.x, self.y, self.facing.value)
            return True
        return False

    def rotate_right(self):
        match self.facing:
            case Direction.NORTH:
                self.facing = Direction.EAST
            case Direction.EAST:
                self.facing = Direction.SOUTH
            case Direction.SOUTH:
                self.facing = Direction.WEST
            case Direction.WEST:
                self.facing = Direction.NORTH


class World:

    def __init__(self):
        self.lines = []
        self.width = 0
        self.height = 0

    def copy(self):
        result = World()
        result.lines = deepcopy(self.lines)
        result.width = self.width
        result.height = self.height
        return result

    def add_line(self, line: str):
        self.lines.append(list(line))
        self.height += 1
        self.width = max(self.width, len(line))

    def is_out(self, x: int, y: int) -> bool:
        return x < 0 or x >= self.width or y < 0 or y >= self.height

    def at(self, x, y, value=None):
        if self.is_out(x, y):
            return '.'
        if value:
            self.lines[y][x] = value
        return self.lines[y][x]

    def show_world(self, caption='', player=None, visited=None):
        if caption:
            print(caption)
        print(f'Width: {self.width} x Height {self.height}')

        if player:
            print(
                f'Player at x: {player.x}'
                f'| y: {player.y}'
                f'| Facing: {player.facing}'
                )
        for (y, row) in enumerate(self.lines):
            for (x, cell) in enumerate(row):
                if player and x == player.x and y == player.y:
                    print(player, end='')
                else:
                    if visited and (x, y) in visited:
                        print('X', end='')
                    else:
                        print(cell, end='')
            print()


def get_options():
    parser = argparse.ArgumentParser(prog='AOC day 6')
    parser.add_argument('filename')
    parser.add_argument('-t', '--trace', action='store_true')
    return parser.parse_args()


def load_input(filename: str):
    world = World()
    player = Player()
    with open(filename) as f_input:
        for y, line in enumerate(f_input):
            line = line.strip()
            world.add_line(line)
            for x, char in enumerate(line):
                if char in '^>v<':
                    player.x = x
                    player.y = y
                    player.facing = Direction.create(char)
                    from icecream import ic; ic(player.facing)
    return world, player
