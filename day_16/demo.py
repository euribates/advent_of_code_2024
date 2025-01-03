import collections

import pygame

import core

FPS = 30

SCALE = 60
if SCALE < 10:
    WIDTH = 1
else:
    WIDTH = SCALE // 10

WHITE = (255, 255, 255)
SILVER = (64, 64, 64)
RED = (200, 32, 32)
GREEN = (32, 220, 32)
YELLOW = (255, 255, 32)
CYAN = (0, 255, 255)


def draw(screen, x, y, symbol):
    x = x * SCALE
    y = y * SCALE
    if symbol == '#':
        pygame.draw.rect(screen, WHITE, [x+1, y+1, SCALE-2, SCALE-2], 0)
    elif symbol == 'S':
        pygame.draw.ellipse(screen, YELLOW, [x+1, y+1, SCALE-2, SCALE-2], 0)
    elif symbol == 'E':
        pygame.draw.ellipse(screen, GREEN, [x+1, y+1, SCALE-2, SCALE-2], 0)
    elif symbol == '.':
        screen.set_at((x+5, y+5), SILVER)
    else:
        raise ValueError(f'What the fuck is {symbol}?')


def draw_explored(screen, explored):
    for position in explored:
        x = position.x * SCALE
        y = position.y * SCALE
        pygame.draw.line(
            screen, RED, [x+1, y+1], [x+SCALE-2, y+SCALE-2], WIDTH
            )
        pygame.draw.line(
            screen, RED, [x+SCALE-2, y+1], [x+1, y+SCALE-2], WIDTH)


def draw_frontier(screen, frontier):
    for item in frontier.heap:
        _, _, actor = item
        if actor:
            x = actor.position.x * SCALE
            y = actor.position.y * SCALE
            pygame.draw.rect(screen, CYAN, [x, y, SCALE, SCALE], WIDTH)

def draw_path(screen, path):
    SIZE = SCALE // 4
    for pos in path:
        x = pos.x * SCALE + SCALE // 2
        y = pos.y * SCALE + SCALE // 2
        pygame.draw.circle(screen, GREEN, [x, y], SIZE, 0)


def main():
    options = core.get_options()
    world, start, target = core.load_input(options.filename)
    pygame.init()
    screen = pygame.display.set_mode((world.width*SCALE, world.height*SCALE))
    clock = pygame.time.Clock()
    running = True
    path = []
    explored = set()
    actor = core.Actor(start, core.RIGHT)
    frontier = core.PriorityMap()
    frontier.push(0, actor)
    come_from = {}
    costs = {
        start: 0,
        }
    sol = 0
    found = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_Q:
                    running = False

        screen.fill("black")
        for (y, row) in enumerate(world.lines):
            for (x, symbol) in enumerate(row):
                draw(screen, x, y, symbol)
        draw_explored(screen, explored)
        draw_frontier(screen, frontier)
        if path:
            draw_path(screen, path)
        # flip() the display to put your work on screen
        pygame.display.flip()
        
        # Explore and find#
        if not found:
            cost, actor = frontier.pop()
            explored.add(actor.position)
            for neighbor, next_cost in world.neighbors(actor):
                if neighbor.position in explored:
                    continue
                come_from[neighbor.position] = actor.position
                if neighbor.position == target:
                    print('Encontrado!')
                    found = True
                    sol, path = core.reverse_path(come_from, target, costs)
                new_cost = cost + next_cost
                if frontier.it_exists(neighbor):
                    if frontier.get_priority(neighbor) <= new_cost:
                        continue
                frontier.push(new_cost, neighbor)
                costs[neighbor.position] = new_cost
        clock.tick(FPS)  # limits FP
    pygame.quit()
    sol = costs[target]
    return sol

if __name__ == '__main__':
    sol = main()
    print(f'[Day 16] Sol. part one is: {sol}')
