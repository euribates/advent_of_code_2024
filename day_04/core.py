#!/usr/bin/env python3

import argparse


def get_options():
    parser = argparse.ArgumentParser(prog='AOC day 4')
    parser.add_argument('filename')
    parser.add_argument('-t', '--trace', action='store_true')
    return parser.parse_args()


def load_input(filename: str):
    letters = {}
    with open(filename) as f_input:
        for y, line in enumerate(f_input):
            for x, char in enumerate(line.strip()):
                letters[x, y] = char
    return x+1, y+1, letters


def iterate_by_cols(cols, rows, data):
    for y in range(rows):
        yield [(x, y, data[x, y]) for x in range(cols)]


def iterate_by_rows(cols, rows, data):
    for x in range(cols):
        yield [(x, y, data[x, y]) for y in range(rows)]


def go_down(cols, rows, data, x, y):
    return [
        (x + delta, y + delta, data[x + delta, y + delta])
        for delta in range(min(cols, rows))
        if x + delta < cols and y + delta < rows
        ]


def iterate_diagonal_down(cols, rows, data):
    for y in range(rows - 1, 0, -1):
        yield go_down(cols, rows, data, 0, y)
    for x in range(0, cols):
        yield go_down(cols, rows, data, x, 0)
