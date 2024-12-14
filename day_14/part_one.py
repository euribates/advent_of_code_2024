#!/usr/bin/env python3

import core


def show_space(space, bots):
    print(f'space is {space.x} x {space.y}')
    places = set([b.position for b in bots])
    for y in range(space.y):
        for x in range(space.x):
            if core.Vector2(x, y) in places:
                print('X', end='', flush=True)
            else:
                print('.', end='', flush=True)
        print()


def count_bots(space, bots, min_x, max_x, min_y, max_y):
    acc = 0
    for bot in bots:
        x, y = bot.position.x, bot.position.y
        if min_x <= x < max_x and min_y <= y < max_y:
            acc += 1
    return acc


def main(options):
    space = core.Vector2(*(int(_) for _ in options.size.split('x')))
    if options.trace:
        print(f'space is {space.x} x {space.y}')
    bots = list(core.load_input(options.filename))
    for tick in range(100):
        for bot in bots:
            bot.move(space)
    show_space(space, bots)
    middle_x = space.x // 2
    middle_y = space.y // 2
    left_top = count_bots(space, bots, 0, middle_x, 0, middle_y)
    # from icecream import ic; ic( 0, middle_x, 0, middle_y)
    # from icecream import ic; ic('left_top', left_top)
    right_top = count_bots(space, bots, middle_x+1, space.x + 1, 0, middle_y)
    # from icecream import ic; ic(middle_x+1, space.x + 1, 0, middle_y)
    # from icecream import ic; ic('right_top', right_top)
    left_bottom = count_bots(space, bots, 0, middle_x, middle_y + 1, space.y + 1)
    right_bottom = count_bots(space, bots, middle_x + 1, space.x + 1, middle_y + 1, space.y + 1)
    return left_top * right_top * left_bottom * right_bottom


if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 14] Sol. part one is: {sol}')
