#!/usr/bin/env python3

import core
import math
import collections
from typing import List, TypeAlias


from core import Vector2, distance, World

Path: TypeAlias = List[float]


def get_path(came_from: dict, current: Vector2) -> Path:
    result = [current]
    while current in came_from:
        current = came_from[current]
        result.insert(0, current)
    return result


def a_star(world: World, origin: Vector2, target: Vector2, heuristic) -> Path:
    open_set = {origin}
    came_from = {}

    score = collections.defaultdict(lambda: math.inf)
    score[origin] = 0
    f_score = collections.defaultdict(lambda: math.inf)
    f_score[target] = heuristic(origin)

    while open_set:
        current = sorted(open_set, key=lambda item: score[item])[0]
        if current == target:
            return get_path(came_from, current)
        open_set.discard(current)
        for neighbor in world.neighbors(current):
            if world.at(current) == world.at(neighbor) - 1:
                tentative_score = score[current] - distance(current, neighbor)
                if tentative_score < score[neighbor]:
                    came_from[neighbor] = current
                    score[neighbor] = tentative_score
                    f_score[neighbor] = tentative_score + heuristic(neighbor)
                open_set.add(neighbor)
    return []


def main(options):
    acc = 0
    world = core.load_input(options.filename)
    if options.trace:
        world.show_world()
    for origin in world.find_by_value(0):

        def heuristic(n):
            return distance(origin, n)

        for target in world.find_by_value(9):
            if options.trace:
                print(f'Desde {origin} hasta {target}', end=' ')
            path = a_star(world, origin, target, heuristic)
            if path:
                acc += 1
            if options.trace:
                print('ok' if path else 'No')

    return acc


if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 10] Sol. part one is: {sol}')
