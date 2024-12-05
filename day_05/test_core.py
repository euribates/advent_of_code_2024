#!/usr/bin/env python3

import pytest

import core


@pytest.fixture(scope="module")
def playset():
    rules, instructions = core.load_input('sample')
    return rules, instructions


def test_load_input(playset):
    rules, instructions = playset

    assert rules[61] == {97, 75, 47}
    assert rules[13] == {53, 75, 47, 29, 61, 97}
    assert instructions[0] == [75, 47, 61, 53, 29]
    assert instructions[-1] == [97, 13, 75, 29, 47]


def test_is_valid(playset):
    rules, instructions = playset
    assert core.is_valid(rules, instructions[0]) is True
    assert core.is_valid(rules, instructions[1]) is True
    assert core.is_valid(rules, instructions[2]) is True
    assert core.is_valid(rules, instructions[3]) is False
    assert core.is_valid(rules, instructions[4]) is False
    assert core.is_valid(rules, instructions[5]) is False


def test_fix_order(playset):
    rules, instructions = playset
    assert core.fix_order(rules, [75, 97, 47, 61, 53]) == [97, 75, 47, 61, 53]
    assert core.fix_order(rules, [61, 13, 29]) == [61, 29, 13]
    assert core.fix_order(rules, [97, 13, 75, 29, 47]) == [97, 75, 47, 29, 13]



if __name__ == "__main__":
    pytest.main()
