#!/usr/bin/env python3

import core


def main(options):
    acc = 0
    world, moves, bot = core.load_input(options.filename)
    world.show_world()
    for direction in moves:
        print(direction)
        bot, moved = world.move(bot, direction)
        if options.trace:
            if moved:
                print('bot is now at {bot.x}, {bot.y}')
            else:
                print('bot can\'t move')
    world.show_world()
    for (pos, item) in world.all_nodes():
        if item == 'O':
            acc += pos.x + 100 * pos.y
    return acc


if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 15] Sol. part two is: {sol}')
