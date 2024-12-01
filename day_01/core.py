#!/usr/bin/env python3

import argparse


def get_options():
    parser = argparse.ArgumentParser(prog='AOC day 1')
    parser.add_argument('filename')
    parser.add_argument('-t', '--trace', action='store_true')
    return parser.parse_args()


def load_input(filename: str):
    with open(filename) as f_input:
        for line in f_input:
            a, b = line.strip().split()
            yield int(a), int(b)
