#!/usr/bin/env python3

import collections
import argparse


def get_options():
    parser = argparse.ArgumentParser(prog='AOC day 5')
    parser.add_argument('filename')
    parser.add_argument('-t', '--trace', action='store_true')
    return parser.parse_args()


def load_input(filename: str):
    rules = collections.defaultdict(set)
    instructions = []
    with open(filename) as f_input:
        for line in f_input:
            line = line.strip()
            if not line:
                break
            page_before, page_after = [int(_) for _ in line.split('|')]
            rules[page_after].add(page_before)
        for line in f_input:
            nums = [int(_) for _ in line.split(',')]
            instructions.append(nums)
    return rules, instructions


def is_valid(rules, pages):
    for i, page in enumerate(pages):
        next_pages = set(pages[i+1:])
        if len(rules[page].intersection(next_pages)) > 0:
            return False
    return True


def first(iterable, condition=lambda x: True, default=None):
    for item in iterable:
        if condition(item):
            return item
    return default


def find_swap_candidate(rules, pages, index, page):
    next_pages = set(pages[index+1:])
    subset = rules[page].intersection(next_pages)
    if subset:
        new_page = first(subset)
        return pages.index(new_page)
    return -1


def fix_order(rules, pages):
    result = pages.copy()
    while not is_valid(rules, result):
        for index, page in enumerate(result):
            other = find_swap_candidate(rules, result, index, page)
            if other >= 0:
                result[index], result[other] = result[other], result[index]
    return result
