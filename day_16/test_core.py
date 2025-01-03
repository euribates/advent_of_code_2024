#!/usr/bin/env python3

import pytest

import core


def test_load_input():
    world = core.load_input('sample')
    assert world.width == 15
    assert world.height == 15
    assert world.start == core.Vector2(1, 13)
    assert world.target == core.Vector2(13, 1)
    assert world.direction == core.RIGHT


def test_vector_distance():
    assert core.distance(
        core.Vector2(1, 1),
        core.Vector2(3, 4),
        ) == 5


if __name__ == "__main__":
    pytest.main()
