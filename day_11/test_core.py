#!/usr/bin/env python3

import pytest

import core


def test_load_input():
    assert list(core.load_input('sample')) == [
        125,
        17,
        ]


def test_rule_1():
    assert core.rule(0) == [1]


def test_rule_2():
    assert core.rule(1234) == [12, 34]
    assert core.rule(10) == [1, 0]


def test_rule_3():
    assert core.rule(1) == [2024]
    assert core.rule(2) == [4048]
    assert core.rule(9) == [18216]
    assert core.rule(456) == [922944]


if __name__ == "__main__":
    pytest.main()
