#!/usr/bin/env python3

import pytest
from operator import add, mul

import core


def test_operators_two_numbers():
    ops = list(core.operators(1))
    assert len(ops) == 2


def test_operators_three_numbers():
    ops = list(core.operators(2))
    assert len(ops) == 4


def test_get_solution_mul():
    assert core.get_solution([1, 2], (mul,)) == 2


def test_get_solution_add():
    assert core.get_solution([1, 2], (add,)) == 3


def test_get_solution_one_mul_mul():
    assert core.get_solution([2, 3, 5], (mul, mul)) == 30


def test_get_solution_one_mul_add():
    assert core.get_solution([2, 3, 5], (mul, add)) == 11


def test_get_solution_one_add_mul():
    assert core.get_solution([2, 3, 5], (add, mul)) == 25


def test_get_solution_one_add_add():
    assert core.get_solution([2, 3, 5], (add, add)) == 10


def test_sample_3267():
    """3267: 81 40 27 has two positions for operators.

    Of the four possible configurations of the operators, two cause
    the right side to match the test value: 81 + 40 * 27 and
    81 * 40 + 27 both equal 3267 (when evaluated left-to-right)!

    """
    assert core.get_solution([81, 40, 27], (add, mul)) == 3267
    assert core.get_solution([81, 40, 27], (mul, add)) == 3267


def test_sample_192():
    """192: 17 8 14 can be made true using 17 || 8 + 14

    """
    assert core.get_solution([17, 8, 14], (core.concat, add)) == 192


def test_concat():
    assert core.concat(1, 32) == 132


if __name__ == "__main__":
    pytest.main()
