#!/usr/bin/env python3

import argparse
from operator import add, mul
import itertools

OPS_PART_ONE = [mul, add]


def concat(op1: int, op2: int):
    return int(f'{op1}{op2}')


OPS_PART_TWO = [mul, add, concat]


def get_options():
    parser = argparse.ArgumentParser(prog='AOC day 7')
    parser.add_argument('filename')
    parser.add_argument('-t', '--trace', action='store_true')
    return parser.parse_args()


def load_input(filename: str):
    with open(filename) as f_input:
        for line in f_input:
            line = line.strip()
            result, rest = line.split(': ')
            result = int(result)
            numbers = [int(_) for _ in rest.split()]
            yield (result, numbers)


def operators(num: int, ops=OPS_PART_ONE):
    for tuple_ops in itertools.product(ops, repeat=num):
        yield tuple_ops


def get_solution(numbers, ops) -> int:
    acc, *rest = numbers[:]
    for op in ops:
        next_val = rest.pop(0)
        acc = op(acc, next_val)
    return acc


def show_solution(numbers, ops) -> str:
    acc, *rest = numbers[:]
    buff = [str(acc)]
    for op in ops:
        if op == mul:
            buff.append(' * ')
        elif op == add:
            buff.append(' + ')
        else:
            buff.append(' || ')
        next_val = rest.pop(0)
        buff.append(str(next_val))
        acc = op(acc, next_val)
    buff.append(' = ')
    buff.append(str(acc))
    return ''.join(buff)
