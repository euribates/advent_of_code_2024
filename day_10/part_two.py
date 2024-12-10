#!/usr/bin/env python3

import collections

from core import load_input, get_options
from core import Vector2, World


def bfs(world: World, origin: Vector2, target: Vector2) -> int:
    acc = 0
    queue = collections.deque()
    queue.append(tuple([origin]))
    visited = set()
    results = []
    while queue:
        path = queue.pop()  # Gets the first path in the queue
        current = path[-1]
        if current == target:
            acc += 1
            results.append(path)
            continue
        # We check if the current path is already in the visited
        # nodes set in order not to recheck it
        elif path not in visited:
            # enumerate all adjacent nodes, construct a new
            # path and push it into the queue
            for neighbor in world.neighbors(current):
                if world.at(current) == world.at(neighbor) - 1:
                    new_path = list(path[:])
                    new_path.append(neighbor)
                    queue.append(tuple(new_path))
            visited.add(path)  # Mark the vertex as visited
    return acc, results


def main(options):
    acc = 0
    world = load_input(options.filename)
    if options.trace:
        world.show_world()
    for origin in world.find_by_value(0):
        for target in world.find_by_value(9):
            if options.trace:
                print(f'Desde {origin} hasta {target}', end=' ')
            partial_acc, _results = bfs(world, origin, target)
            acc += partial_acc
    return acc


if __name__ == '__main__':
    sol = main(get_options())
    print(f'[Day 10] Sol. part two is: {sol}')
