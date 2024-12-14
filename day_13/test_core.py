#!/usr/bin/env python3

import pytest

from core import ClawMachine, Vector2


def test_first_sample_machine():
    m = ClawMachine(
        a_button=Vector2(94, 34),
        b_button=Vector2(22, 67),
        prize=Vector2(8400, 5400),
        )
    assert m.is_solvable() is True


def test_first_sample_machine_solution():
    m = ClawMachine(
        a_button=Vector2(94, 34),
        b_button=Vector2(22, 67),
        prize=Vector2(8400, 5400),
        )
    assert m.check(80, 40, trace=False)


def test_second_sample_machine():
    m = ClawMachine(
        a_button=Vector2(26, 66),
        b_button=Vector2(67, 21),
        prize=Vector2(12748, 12176),
        )
    assert m.is_solvable() is False


def test_third_sample_machine():
    m = ClawMachine(
        a_button=Vector2(17, 86),
        b_button=Vector2(84, 37),
        prize=Vector2(7970, 6450),
        )
    assert m.is_solvable() is True


def test_fourth_sample_machine():
    m = ClawMachine(
        a_button=Vector2(69, 23),
        b_button=Vector2(27, 71),
        prize=Vector2(18641, 10270),
        )
    assert m.is_solvable() is False





if __name__ == "__main__":
    pytest.main()
