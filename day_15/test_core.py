#!/usr/bin/env python3

import collections
import pytest

import core

def test_vector_scalar_multiplicity():
    v = core.Vector2(7, 11)
    assert v * 3 == core.Vector2(21, 33)


def test_load_input_integrity():
    world, _, _ = core.load_input('simple_move')
    assert world.lines[0] == ['.', '.', '.']
    assert world.lines[1] == ['.', '@', '.']
    assert world.lines[2] == ['.', '.', '.']
    assert world.at(core.Vector2(1, 1)) == '@'
    world.at(core.Vector2(1, 1), 'X')
    assert world.at(core.Vector2(1, 1)) == 'X'
    assert world.lines[0] == ['.', '.', '.']
    assert world.lines[1] == ['.', 'X', '.']
    assert world.lines[2] == ['.', '.', '.']


def test_make_space_up():
    world = core.World(lines=[
        '##########',
        '#........#',
        '#..[][]..#',
        '#...[]...#',
        '#...@....#',
        '#........#',
        '##########',
        ])
    bot = core.Vector2(4, 4)
    assert world.at(bot) == '@'
    move = core.UP
    queue = collections.deque()
    can_move = core.make_space(world, bot, move, queue)
    assert can_move is True
    assert len(queue) == 6
    while queue:
        move = queue.pop()
        move.apply_to(world)
    assert world.at(bot) == '@'
    assert world.at(bot + core.UP) == '.'


def test_make_column_up():
    world = core.World(lines=[
        '##########',
        '#........#',
        '#...[][].#',
        '#...[]...#',
        '#...@....#',
        '#........#',
        '##########',
        ])
    bot = core.Vector2(4, 4)
    assert world.at(bot) == '@'
    move = core.UP
    queue = collections.deque()
    can_move = core.make_space(world, bot, move, queue)
    assert can_move is True
    assert len(queue) == 4
    while queue:
        move = queue.pop()
        move.apply_to(world)
    assert world.at(bot) == '@'
    assert world.at(bot + core.UP) == '.'


def test_make_space_down():
    world = core.World(lines=[
        '##########',
        '#........#',
        '#....@...#',
        '#...[]...#',
        '#..[][]..#',
        '#........#',
        '##########',
        ])
    bot = core.Vector2(5, 2)
    assert world.at(bot) == '@'
    move = core.DOWN
    queue = collections.deque()
    can_move = core.make_space(world, bot, move, queue)
    assert len(queue) == 6
    assert can_move is True
    while queue:
        move = queue.pop()
        move.apply_to(world)
    assert world.at(bot) == '@'
    assert world.at(bot + core.DOWN) == '.'


def test_load_input_world():
    world, _, _ = core.load_input('sample')
    assert world.width == 10
    assert world.height == 10
    assert world.at(core.Vector2(0, 0)) == '#'
    assert world.at(core.Vector2(1, 1)) == '.'
    assert world.at(core.Vector2(4, 4)) == '@'
    assert world.at(core.Vector2(3, 1)) == 'O'


def test_load_input_steps():
    _, steps, _ = core.load_input('sample')
    assert len(steps) == 700
    assert steps[0:4] == [core.LEFT, core.DOWN, core.DOWN, core.RIGHT]
    assert steps[-4:] == [core.UP, core.LEFT, core.LEFT, core.UP]


def test_load_input_bot():
    _, _, bot = core.load_input('sample')
    assert bot == core.Vector2(4, 4)


def test_can_move():
    world, moves, bot = core.load_input('supersimple')
    assert world.can_move(bot, core.direction('>')) == 1
    assert world.can_move(bot, core.direction('<')) == 1
    assert world.can_move(bot, core.direction('^')) == 0
    assert world.can_move(bot, core.direction('v')) == 1


def test_can_move_with_one_push():
    world, moves, bot = core.load_input('pushsimple')
    assert world.can_move(bot, core.direction('>')) == 2
    for _ in range(4):
        bot, moved = world.move(bot, core.direction('>'))
        assert moved is True
    bot, moved = world.move(bot, core.direction('>'))
    assert moved is False


def test_move_simple():
    world, moves, bot = core.load_input('supersimple')
    assert world.can_move(bot, core.direction('>')) == 1
    bot, moved = world.move(bot, core.direction('>'))
    assert moved is True
    assert world.can_move(bot, core.direction('>')) == 0
    new_bot, moved = world.move(bot, core.direction('>'))
    assert moved is False
    assert bot == new_bot


def test_directions_sanity():
    assert core.as_direction(core.direction('<')) == '<'
    assert core.as_direction(core.direction('>')) == '>'
    assert core.as_direction(core.direction('v')) == 'v'
    assert core.as_direction(core.direction('<')) == '<'


def test_move_command_up():
    world, _, bot = core.load_input('simple_move')
    assert all([cell == '.' for pos, cell in world.all_nodes() if pos != bot])
    assert world.at(bot) == '@'
    move_up = core.MoveCommand(position=bot, direction=core.UP)
    move_up.apply_to(world)
    bot = core.Vector2(1, 0)
    assert all([cell == '.' for pos, cell in world.all_nodes() if pos != bot])
    assert world.at(bot) == '@'


def test_move_command_right():
    world, _, bot = core.load_input('simple_move')
    assert all([cell == '.' for pos, cell in world.all_nodes() if pos != bot])
    assert world.at(bot) == '@'
    move_up = core.MoveCommand(position=bot, direction=core.RIGHT)
    move_up.apply_to(world)
    bot = core.Vector2(2, 1)
    assert all([cell == '.' for pos, cell in world.all_nodes() if pos != bot])
    assert world.at(bot) == '@'


def test_move_command_down():
    world, _, bot = core.load_input('simple_move')
    assert all([cell == '.' for pos, cell in world.all_nodes() if pos != bot])
    assert world.at(bot) == '@'
    move_up = core.MoveCommand(position=bot, direction=core.DOWN)
    move_up.apply_to(world)
    bot = core.Vector2(1, 2)
    assert all([cell == '.' for pos, cell in world.all_nodes() if pos != bot])
    assert world.at(bot) == '@'


def test_move_command_left():
    world, _, bot = core.load_input('simple_move')
    assert all([cell == '.' for pos, cell in world.all_nodes() if pos != bot])
    assert world.at(bot) == '@'
    move_up = core.MoveCommand(position=bot, direction=core.LEFT)
    move_up.apply_to(world)
    bot = core.Vector2(0, 1)
    assert all([cell == '.' for pos, cell in world.all_nodes() if pos != bot])
    assert world.at(bot) == '@'


def test_sample_2():
    world, moves, bot = core.load_input('sample2')
    world = core.expand_world(world)
    bot = core.expand_bot(bot)
    assert world.at(bot) == '@'
    assert moves[0] == core.LEFT
    assert all([cell in '.#[]' for pos, cell in world.all_nodes() if pos != bot])
    queue = collections.deque()
    move = moves.pop(0)
    can_move = core.make_space(world, bot, move, queue)
    assert can_move is True
    assert len(queue) == 4


def test_tricky():
    world = core.World(lines=[
        "#######################",
        "##...................##",
        "##...................##",
        "##.....[]####........##",
        "##.....##....[]......##",
        "##.....##...[][].....##",
        "##...##....[][]......##",
        "##.......##..@.......##",
        "##...##......[]......##",
        "##...................##",
        "##...................##",
        "#######################",
        ])
    bot = core.Vector2(13, 7)
    assert world.at(bot) == '@'
    move = core.UP
    queue = collections.deque()
    can_move = core.make_space(world, bot, move, queue)
    assert can_move
    bot = core.move_all(world, bot, move, queue)
    assert world.at(bot) == '@'




if __name__ == "__main__":
    pytest.main()
