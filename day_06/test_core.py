#!/usr/bin/env python3

import pytest

import core


def test_direcion():
    flag = core.Direction.NORTH | core.Direction.EAST
    assert flag & core.Direction.NORTH
    assert flag & core.Direction.EAST
    assert not flag & core.Direction.SOUTH
    assert not flag & core.Direction.WEST


def test_direcion_all():
    flag = (
        core.Direction.NORTH
        | core.Direction.EAST
        | core.Direction.SOUTH
        | core.Direction.WEST
        )
    assert flag & core.Direction.NORTH
    assert flag & core.Direction.EAST
    assert flag & core.Direction.SOUTH
    assert flag & core.Direction.WEST




if __name__ == "__main__":
    pytest.main()
