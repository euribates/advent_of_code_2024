#!/usr/bin/env python3

import math
import argparse
import dataclasses
import re


def get_options():
    parser = argparse.ArgumentParser(prog='AOC day 13')
    parser.add_argument('filename')
    parser.add_argument('-t', '--trace', action='store_true')
    return parser.parse_args()


@dataclasses.dataclass(frozen=True)
class Vector2:
    x: int = 0
    y: int = 0

    def __rerp__(self):
        return f'Vector2({self.x!r}, {self.y!r})'

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


class ClawMachine:
    PAT_BUTTON = re.compile(r'Button [AB]: X\+(\d+), Y\+(\d+)')
    PAT_PRIZE = re.compile(r'Prize: X=(\d+), Y=(\d+)')

    def __init__(self, a_button: Vector2, b_button: Vector2, prize: Vector2):
        self.a_button = a_button
        self.b_button = b_button
        self.prize = prize

    def __repr__(self):
        return (
            f'ClawMachine(a_button={self.a_button!r},'
            f' b_button={self.b_button!r},'
            f' prize={self.prize!r})'
            )

    def is_solvable(self):
        mcd_x = math.gcd(self.a_button.x, self.b_button.x)
        mcd_y = math.gcd(self.a_button.y, self.b_button.y)
        return all([
            self.prize.x / mcd_x == self.prize.x // mcd_x,
            self.prize.y / mcd_y == self.prize.y // mcd_y,
            ])

    @classmethod
    def create(cls, lines):
        assert len(lines) == 3
        m_button_a = cls.PAT_BUTTON.match(lines[0])
        button_a = Vector2(int(m_button_a.group(1)), int(m_button_a.group(2)))

        m_button_b = cls.PAT_BUTTON.match(lines[1])
        button_b = Vector2(int(m_button_b.group(1)), int(m_button_b.group(2)))

        m_prize = cls.PAT_PRIZE.match(lines[2])
        prize = Vector2(int(m_prize.group(1)), int(m_prize.group(2)))
        return cls(button_a, button_b, prize)

    def check(self, a, b, trace=False):
        s1 = (a * self.a_button.x + b * self.b_button.x)
        s2 = (a * self.a_button.y + b * self.b_button.y)
        if trace:
            print()
            print(
                f'{a} * {self.a_button.x} = {a * self.a_button.x}',
                '+',
                f'{b} * {self.b_button.x} = {b * self.b_button.x}',
                '=',
                f'{s1}',
                )
            print(
                f'{a} * {self.a_button.y} = {a * self.a_button.y}',
                '+',
                f'{b} * {self.b_button.y} = {b * self.b_button.y}',
                '=',
                f'{s2}',
                )
            print(f'{s1} {"!" if s1 != self.prize.x else "="}= {self.prize.x}')
            print(f'{s2} {"!" if s2 != self.prize.y else "="}= {self.prize.y}')
        return s1 == self.prize.x and s2 == self.prize.y




def load_input(filename: str):
    with open(filename) as f_input:
        buff = []
        for line in f_input:
            line = line.strip()
            if line == '':
                if buff:
                    yield ClawMachine.create(buff)
                buff = []
            else:
                buff.append(line)
        if buff:
            yield ClawMachine.create(buff)
