#!/usr/bin/env python3

import pytest

from core import Vector2D, load_input
from core import all_antinodes, get_antinodes


def test_is_inside():
    world, _ = load_input('simple')
    assert world.is_inside(0, 0)
    assert not world.is_inside(-1, 0)
    assert not world.is_inside(0, -1)
    assert not world.is_inside(-1, -1)

    assert world.is_inside(19, 0)
    assert not world.is_inside(20, 0)
    assert not world.is_inside(19, -1)
    assert not world.is_inside(20, -1)

    assert world.is_inside(0, 3)
    assert not world.is_inside(0, 4)
    assert not world.is_inside(-1, 3)
    assert not world.is_inside(-1, 4)

    assert world.is_inside(19, 3)
    assert not world.is_inside(20, 3)
    assert not world.is_inside(19, 4)
    assert not world.is_inside(20, 4)


def test_add_vectors():
    assert Vector2D(1, 2) + Vector2D(3, 5) == Vector2D(4, 7)


def test_sub_vectors():
    assert Vector2D(4, 7) - Vector2D(3, 5) == Vector2D(1, 2)


def test_load_input():
    world, antennas = load_input('simple')
    assert world.width == 20
    assert world.height == 4
    assert len(antennas) == 2
    assert world.at(0, 0) == '.'
    assert world.at(5, 1) == 'A'
    assert world.at(9, 1) == 'A'
    assert world.at(13, 1) == 'B'
    assert world.at(14, 2) == 'B'


def test_distance():
    v1 = Vector2D(5, 1)
    v2 = Vector2D(8, 1)
    assert v1 - v2 == Vector2D(-3, 0)
    assert v2 - v1 == Vector2D(3, 0)


def test_distance_zero():
    v1 = Vector2D(x=5, y=1)
    assert v1 - v1 == Vector2D(0, 0)


def test_get_antinodes():
    v1 = Vector2D(x=5, y=1)
    v2 = Vector2D(x=9, y=1)
    n1, n2 = get_antinodes(v1, v2)
    assert n1 == Vector2D(1, 1)
    assert n2 == Vector2D(13, 1)


def test_get_antinodes_diagonal():
    v1 = Vector2D(x=7, y=2)
    v2 = Vector2D(x=5, y=4)
    n1, n2 = get_antinodes(v1, v2)
    assert n1 == Vector2D(9, 0)
    assert n2 == Vector2D(3, 6)


def test_all_antinodes():
    world, _ = load_input('simple')
    v1 = Vector2D(5, 1)
    v2 = Vector2D(9, 1)
    antinodes = set(all_antinodes(world, v1, v2))
    assert len(antinodes) == 5
    assert Vector2D(1, 1) in antinodes
    assert Vector2D(5, 1) in antinodes
    assert Vector2D(9, 1) in antinodes
    assert Vector2D(13, 1) in antinodes
    assert Vector2D(17, 1) in antinodes


if __name__ == "__main__":
    pytest.main()
