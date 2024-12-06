#!/usr/bin/env python3

import core


def main(options):
    world, player = core.load_input(options.filename)
    if options.trace:
        print(player)
        world.show_world(player)
    visited = set([(player.x, player.y)])
    while not world.is_out(player.x, player.y):
        it_moved = player.forward(world)
        if it_moved:
            visited.add((player.x, player.y))
            # print('F', end='')
        else:
            player.rotate_right()
            # print('R', end='')
    if options.trace:
        world.show_world(player, visited=visited)
    return len(visited) - 1 # No contamos el ultimo movimiento


if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 6] Sol. part one is: {sol}')
