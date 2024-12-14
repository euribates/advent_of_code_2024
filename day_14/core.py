#!/usr/bin/env python3

import dataclasses
import argparse


def get_options():
    parser = argparse.ArgumentParser(prog='AOC day 14')
    parser.add_argument('filename')
    parser.add_argument('size')
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


class Robot:

    def __init__(self, position: Vector2, velocity: Vector2):
        self.position = position
        self.velocity = velocity
        self.clock = 0

    def __str__(self):
        return (
            f'Bot at {self.position.x}, {self.position.y}'
            f'f pointing to {self.velocity.x}, {self.velocity.y}'
            )

    def move(self, space: Vector2):
        new_position = self.position + self.velocity
        self.position = Vector2(
            new_position.x % space.x,
            new_position.y % space.y,
            )
        self.clock += 1

    @classmethod
    def create(cls, line: str):
        part_pos, part_vel = line.split(' ')
        position = Vector2(*(int(_) for _ in part_pos[2:].split(',')))
        velocity = Vector2(*(int(_) for _ in part_vel[2:].split(',')))
        return cls(position, velocity)


def load_input(filename: str):
    with open(filename) as f_input:
        for line in f_input:
            line = line.strip()
            yield Robot.create(line)
