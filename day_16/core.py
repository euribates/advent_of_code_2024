#!/usr/bin/env python3

import argparse
import dataclasses
import functools
import heapq
import itertools
import typing


def get_options():
    parser = argparse.ArgumentParser(prog='AOC day 16')
    parser.add_argument('filename')
    parser.add_argument('-t', '--trace', action='store_true')
    return parser.parse_args()


@dataclasses.dataclass(frozen=True)
class Vector2:

    x: int = 0
    y: int = 0

    def __rerp__(self):
        return f'Vector2({self.x!r}, {self.y!r})'

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: int):
        return Vector2(self.x * scalar, self.y * scalar)

    def copy(self):
        return Vector2(x=self.x, y=self.y)

    def up(self):
        return Vector2(self.x, self.y - 1)

    def down(self):
        return Vector2(self.x, self.y + 1)

    def left(self):
        return Vector2(self.x - 1, self.y)

    def right(self):
        return Vector2(self.x + 1, self.y)

    def adyacents(self):
        yield self.left()
        yield self.down()
        yield self.right()
        yield self.up()


UP = Vector2(0, -1)
RIGHT = Vector2(1, 0)
DOWN = Vector2(0, 1)
LEFT = Vector2(-1, 0)


Direction = typing.Literal[UP, RIGHT, DOWN, LEFT]


def as_direction(direction: Direction) -> str:
    match (direction.x, direction.y):
        case 0, -1:
            return '^'
        case 1, 0:
            return '>'
        case 0, 1:
            return 'v'
        case -1, 0:
            return '<'
        case _:
            raise ValueError(f'Direction {direction} must be a unit vector')


@dataclasses.dataclass
class Actor:

    position: Vector2 = Vector2(0, 0)
    direction: Direction = RIGHT

    def __repr__(self):
        return f'Actor({self.position!r}, {self.direction!r}'

    def __hash__(self):
        x = self.position.x
        y = self.position.y
        dx = self.direction.x
        dy = self.direction.y
        return hash((x, y, dx, dy))

    def copy(self):
        return Actor(self.position, self.direction)
    
    def can_move(self, world) -> bool:
        return world.at(self.position + self.direction) in 'S.E'

    def move(self):
        self.position = self.position + self.direction

    def turn_right(self):
        left_turns = {
            UP: RIGHT,
            RIGHT: DOWN,
            DOWN: LEFT,
            LEFT: UP,
            }
        self.direction = left_turns[self.direction]

    def turn_left(self):
        right_turns = {
            UP: LEFT,
            LEFT: DOWN,
            DOWN: RIGHT,
            RIGHT: UP,
            }
        self.direction = right_turns[self.direction]


class World:

    def __init__(self, lines=None):
        self.lines = []
        self.width = 0
        self.height = 0
        if lines:
            for line in lines:
                self.add_line(line)

    def add_line(self, line: str):
        self.lines.append(list(line))
        self.height += 1
        self.width = max(self.width, len(line))
    
    @classmethod
    def from_file(cls, filename):
        world = cls()
        start = None
        target = None
        with open(filename) as f_input:
            for y, line in enumerate(f_input):
                line = line.strip()
                world.add_line(line)
                for x, char in enumerate(line):
                    if char == 'S':
                        start = Vector2(x, y)
                    elif char == 'E':
                        target = Vector2(x, y)
        return world, start, target

    def __str__(self):
        buff = []
        for (y, row) in enumerate(self.lines):
            for (x, cell) in enumerate(row):
                buff.append(cell)
            buff.append("\n")
        return ''.join(buff)

    def is_inside(self, pos: Vector2) -> bool:
        return (0 <= pos.x < self.width) and (0 <= pos.y < self.height)

    def is_out(self, pos: Vector2) -> bool:
        return not self.is_inside(pos)

    def at(self, pos: Vector2, value=None):
        if self.is_out(pos):
            return '#'
        if value:
            self.lines[pos.y][pos.x] = value
        return self.lines[pos.y][pos.x]

    def show_world(self, caption='', actor=None):
        if caption:
            print(caption)
        print(f'- Size in {self.width} x {self.height}')
        if actor:
            print(f'- Actor at {actor.position} fecing {as_direction(actor.direction)}')
        print(self)

    def neighbors(self, actor: Actor):
        # Straigth ahead
        straight_actor = actor.copy()
        straight_actor.move()
        if self.at(straight_actor.position) in {'.', 'E'}:
            yield straight_actor, 1  # One movement
        left_actor = actor.copy()
        left_actor.turn_left()
        left_actor.move()
        if self.at(left_actor.position) in {'.', 'E'}:
            yield left_actor, 1001  # One turn, one movement
        right_actor = actor.copy()
        right_actor.turn_right()
        right_actor.move()
        if self.at(right_actor.position) in {'.', 'E'}:
            yield right_actor, 1001  # One turn, one movement

    def all_nodes(self):
        for (y, row) in enumerate(self.lines):
            for (x, cell) in enumerate(row):
                yield (Vector2(x, y), cell)

    def can_move(self) -> bool:
        return self.at(self.current + self.direction) in 'S.E'

    def move(self, bot, direction):
        self.current += self.direction


def distance(source: Vector2, target: Vector2):
    """
    Manhattan geometry is geometry where the familiar
    Euclidean distance is ignored, and the distance between
    two points is instead defined to be the sum of the
    absolute differences of their respective Cartesian coordinates,
    """
    return abs(source.x - target.x) + abs(source.y - target.y)



class PriorityMap:

    def __init__(self):
        self.directory = {}
        self.counter = itertools.count()
        self.total = 0
        self.heap = []
        heapq.heapify(self.heap)
        assert len(self.heap) == 0
        assert self.heap is not None

    def __str__(self) -> str:
        buff = []
        for item in self.heap:
            buff.append(str(item))
        return '\n'.join(buff)

    def __len__(self):
        return self.total

    def push(self, priority, actor):
        if actor.position in self.directory:
            self.remove(actor)
        count = next(self.counter)
        entry = [priority, count, actor]
        self.directory[actor.position] = entry
        heapq.heappush(self.heap, entry)
        self.total += 1

    def it_exists(self, actor) -> bool:
        return actor.position in self.directory

    def get_priority(self, actor):
        entry = self.directory.get(actor.position, None)
        if entry:
            return entry[0]
        raise KeyError(f"Position {position} not in PriorityMap")

    def remove(self, actor: Actor):
        """
        Mark an existing position as removed. 
        """
        entry = self.directory.pop(actor.position)
        entry[-1] = None
        self.total -= 1

    def pop(self):
        while self.heap:
            priority, count, actor = heapq.heappop(self.heap)
            if actor is not None:
                del self.directory[actor.position]
                self.total -= 1
                return priority, actor
        raise KeyError('pop from an empty priority queue')


def reverse_path(come_from, target, costs):
    acc = 0
    result = [target]
    prev = come_from[target]
    while prev:
        result.insert(0, prev)
        acc += costs[prev]
        prev = come_from.get(prev, None)
    return acc, result


def a_star(world: World, start, target, max_iterations=65536):
    explored = set()
    actor = Actor(start, RIGHT)
    frontier = PriorityMap()
    frontier.push(0, actor)
    come_from = {}
    iteration = itertools.count()
    costs = {start: 0}
    while frontier and next(iteration) < max_iterations:
        cost, actor = frontier.pop()
        explored.add(actor.position)
        for neighbor, next_cost in world.neighbors(actor):
            if neighbor.position in explored:
                continue
            come_from[neighbor.position] = actor.position
            if neighbor.position == target:
                return costs[actor.position] + next_cost
            new_cost = cost + next_cost
            if frontier.it_exists(neighbor):
                if frontier.get_priority(neighbor) <= new_cost:
                    continue
            frontier.push(new_cost, neighbor)
            costs[neighbor.position] = new_cost
    raise ValueError("Can't find a solution")


def load_input(filename: str):
    world, start, target = World.from_file(filename)
    return world, start, target
