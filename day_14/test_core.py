#!/usr/bin/env python3

import pytest

import core
from core import Robot
from core import Vector2


def test_add_vectors():
    a = Vector2(3, 5)
    b = Vector2(7, 9)
    assert a + b == Vector2(10, 14)


def test_sub_vectors():
    a = Vector2(7, 4)
    b = Vector2(3, 5)
    assert a - b == Vector2(4, -1)


def test_create_robot():
    bot = Robot.create('p=2,4 v=2,-3')
    assert bot.position.x == 2
    assert bot.position.y == 4
    assert bot.velocity.x == 2
    assert bot.velocity.y == -3


def test_robot_move_clock():
    bot = Robot(position=Vector2(2, 4), velocity=Vector2(5, -3))
    assert bot.clock == 0
    bot.move(space=Vector2(101, 103))
    assert bot.clock == 1


def test_robot_move():
    bot = Robot(position=Vector2(2, 4), velocity=Vector2(2, -3))
    assert bot.position.x == 2
    assert bot.position.y == 4
    bot.move(space=Vector2(101, 103))
    assert bot.position.x == 4
    assert bot.position.y == 1


def test_robot_move_teleport():
    bot = Robot(position=Vector2(2, 4), velocity=Vector2(1, 1))
    assert bot.position.x == 2
    assert bot.position.y == 4
    bot.move(space=Vector2(3, 103))
    assert bot.position.x == 0
    assert bot.position.y == 5


def test_sample():
    space = Vector2(11, 7)
    bot = core.Robot.create('p=2,4 v=2,-3')
    assert bot.position == Vector2(2, 4)
    bot.move(space)  # First second
    assert bot.position == Vector2(4, 1)
    bot.move(space)  # Second second
    assert bot.position == Vector2(6, 5)
    bot.move(space)  # Third second
    assert bot.position == Vector2(8, 2)
    bot.move(space)  # Fourth second
    assert bot.position == Vector2(10, 6)
    bot.move(space)  # Five second
    assert bot.position == Vector2(1, 3)






if __name__ == "__main__":
    pytest.main()
