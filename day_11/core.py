#!/usr/bin/env python3

import argparse


def get_options():
    parser = argparse.ArgumentParser(prog='AOC day 11')
    parser.add_argument('filename')
    parser.add_argument('-t', '--trace', action='store_true')
    return parser.parse_args()


def rule(num):
    if num == 0:
        return [1]
    txt = str(num)
    size = len(txt)
    if size % 2 == 0:
        middle = size // 2
        return [int(txt[0:middle]), int(txt[middle:])]
    return [num * 2024]


def load_input(filename: str):
    with open(filename) as f_input:
        for line in f_input:
            line = line.strip()
            for num in line.split():
                yield int(num)
