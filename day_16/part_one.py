#!/usr/bin/env python3

import core


def main(options):
    world, start, target = core.load_input(options.filename)
    costs, come_from = core.a_star(world, start, target)
    print(core.get_path(come_from, target, costs))
    for pos, cost in sorted(costs.items()):
        print(f"{pos.x}, {pos.y} : {cost}")
    return costs[target]


if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 16] Sol. part one is: {sol}')
