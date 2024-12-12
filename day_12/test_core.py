#!/usr/bin/env python3

import collections

import pytest

import core


def test_find_regions_simple_2x2():
    world = core.load_input('simple2x2')
    regions = list(world.find_regions())
    assert len(regions) == 1
    region = regions[0]
    assert region[0] == 'A'
    assert region[1] == {
        core.Vector2(0, 0),
        core.Vector2(0, 1),
        core.Vector2(1, 0),
        core.Vector2(1, 1),
        }


def test_find_simple():
    world = core.load_input('simple')
    counters = {}
    for region_name, items in world.find_regions():
        counters[region_name] = len(items)
    assert len(counters) == 5
    assert counters['A'] == 4
    assert counters['B'] == 4
    assert counters['C'] == 4
    assert counters['D'] == 1
    assert counters['E'] == 3


def test_find_simple_2():
    world = core.load_input('simple_2')
    counter = 0
    counters = collections.defaultdict(int)
    for region_name, items in world.find_regions():
        counters[region_name] += len(items)
        counter += 1
    assert counter == 5
    assert len(counters) == 2
    assert counters['X'] == 4
    assert counters['O'] == 21


def test_find_sample():
    world = core.load_input('sample')
    counter = 0
    counters = collections.defaultdict(int)
    for region_name, items in world.find_regions():
        counters[region_name] += len(items)
        counter += 1
    assert counter == 11
    assert len(counters) == 9
    assert counters['R'] == 12
    assert counters['I'] == 4 + 14
    assert counters['C'] == 14 + 1
    assert counters['F'] == 10
    assert counters['V'] == 13
    assert counters['E'] == 13
    assert counters['M'] == 5
    assert counters['S'] == 3


if __name__ == "__main__":
    pytest.main()
