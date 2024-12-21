#!/usr/bin/env python3

import collections
import time
import typing
import curses

from core import get_options, load_input
from core import Vector2, World
from core import Direction, UP, RIGHT, DOWN, LEFT
from core import as_direction
from core import MoveCommand
from core import expand_world, expand_bot
from core import make_space



def show_world(stdscr, world, bot, orientation, queue, trace=False):
    stdscr.clear()
    stdscr.addstr(1, 0, f'Size is {world.width} x {world.height}')
    stdscr.addstr(2, 0, f'Bot at {bot}')
    stdscr.addstr(3, 0, f'orientation is : {as_direction(orientation)}')
    stdscr.addstr(4, 0, f'Queue size: {len(queue)}')
    for (y, row) in enumerate(world.lines):
        for (x, symbol) in enumerate(row):
            if bot and bot.x == x and bot.y == y:
                if orientation:
                    symbol = as_direction(orientation)
                else:
                    symbol = '@'
            stdscr.addch(y + 4, x, symbol)
    prompt = '◉'
    for index, item in enumerate(reversed(queue)):
        msg = f'{prompt} {index}) Move {item.trace(world)}'
        stdscr.addstr(index, 60, msg)
        prompt = ' '
    stdscr.refresh()
    if trace:
        stdscr.getkey()
    else:
        time.sleep(0.1)


def main(stdscr):
    options = get_options()
    world, moves, bot = load_input(options.filename)
    world = expand_world(world)
    bot = expand_bot(bot)
    show_world(stdscr, world, bot, UP, [], options.trace)
    for move in moves:
        queue = collections.deque()
        can_move = make_space(world, bot, move, queue)
        if can_move:
            while queue:
                movement = queue.pop()
                show_world(stdscr, world, bot, move, queue, options.trace)
                movement.apply_to(world)
                show_world(stdscr, world, bot, move, queue, options.trace)
            # Do initial movement
            world.at(bot, '.')
            bot = bot + move
            world.at(bot, '@')
            show_world(stdscr, world, bot, move, queue, options.trace)
    stdscr.getkey()
    acc = 0
    for (pos, item) in world.all_nodes():
        if item == '[':
            acc += pos.x + 100 * pos.y
    return acc


if __name__ == '__main__':
    sol = curses.wrapper(main)
    print(f'[Day 15] Sol. part two is: {sol}')
