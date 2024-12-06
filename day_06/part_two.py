#!/usr/bin/env python3

import core

import rich
from rich.progress import Progress


def has_solution(world, player, x, y):
    if player.x == x and player.y == y: # We can't place here
        return 0
    if world.at(x, y) != '.': # Obstacle in place
        return 0
    player = player.copy()
    # world.show_world('Original')
    new_world = world.copy()
    new_world.at(x, y, '#')
    # new_world.show_world('Copia')
    # world.show_world('Original')
    # print(id(world))
    # print(id(new_world))
    # print()
    # print(id(world.lines))
    # print(id(new_world.lines))
    # print(world.lines == new_world.lines)
    # print()
    visited = {}
    visited[player.x, player.y] = player.facing
    while not new_world.is_out(player.x, player.y):
        it_moved = player.forward(new_world)
        if it_moved:
            if (player.x, player.y) in visited:
                if player.facing & visited[player.x, player.y]:
                    # Cycle found, can return
                    return 1
                visited[player.x, player.y] |= player.facing
            else:
                visited[player.x, player.y] = player.facing
        else:
            player.rotate_right()
        # new_world.show_world('Copia', player=player)
        # if input('sigo?') in {'n', 'N'}:
            # return 0
    return 0


def main(options):
    acc = 0
    world, player = core.load_input(options.filename)
    world.show_world(player)
    total = world.width * world.height
    with Progress() as progress:
        task = progress.add_task("Working", total=total)
        for x in range(world.width):
            for y in range(world.height):
                acc += has_solution(world, player, x, y)
                progress.update(task, advance=1)

    return acc


if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 6] Sol. part two is: {sol}')
