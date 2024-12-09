#!/usr/bin/env python3

import pytest

import core


def test_load_input():
    disk = list(core.load_input('simple'))
    assert disk[0] == (0, 1, 2)
    assert disk[1] == (1, 3, 4)
    assert disk[2] == (2, 5, None)



if __name__ == "__main__":
    pytest.main()
