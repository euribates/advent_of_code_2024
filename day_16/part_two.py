#!/usr/bin/env python3

import core
import itertools
import math
import collections

from icecream import ic

MAX_ITERATIONS = 65536 


def bsf(world, start, target):
    queue = collections.deque([core.Actor(start, core.RIGHT)])
    visited = set([])
    distances = {start: 0}
    while queue:
        actor = queue.pop()
        print(actor)
        visited.add(actor.pos)
        

nitialization: Enqueue the given source vertex into a queue and mark it as visited.

    Exploration: While the queue is not empty:
        Dequeue a node from the queue and visit it (e.g., print its value).
        For each unvisited neighbor of the dequeued node:
            Enqueue the neighbor into the queue.
            Mark the neighbor as visited. 
    Termination: Repeat step 2 until the queue is empty. 

sorted
uu
class BSF:

    def __init__(self, world, start, target, optimal_path_cost):#
        self.in_optimal_path = set()
        self.world = world
        self.start = start
        self.target = target
        self.optimal_path_cost = optimal_path_cost
        self.explored = set()
        self.iteration = itertools.count()

    def bsf(self, path):
        next_iteration = next(self.iteration)
        ic(next_iteration, path)
        if next_iteration > MAX_ITERATIONS:
            raise ValueError("Estoy en bucle...")
        actor, prev_cost = path[-1]
        if actor.position == self.target:
            ic(prev_cost, self.optimal_path_cost)
            if prev_cost == self.optimal_path_cost:
                return True
            return False
        self.explored.add(actor.position)
        result = False
        for neighbor, next_cost in self.world.neighbors(actor):
            if neighbor.position in self.explored:
                continue
            new_path = path + [(neighbor, prev_cost+next_cost)]
            if self.bsf(new_path):
                self.in_optimal_path.add(neighbor.position)
                result = True
        return result


def main(options):
    world, start, target = core.load_input(options.filename)
    optimal_path_cost = core.a_star(world, start, target)
    if options.trace:
        print(f"Optimal path cost: {optimal_path_cost}") 
    search = BSF(world, start, target, optimal_path_cost)
    initial_path = [(core.Actor(start, core.RIGHT), 0)]
    search.bsf(initial_path)
    from icecream import ic; ic(search.in_optimal_path)
    return len(search.in_optimal_path)


if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 16] Sol. part two is: {sol}')
