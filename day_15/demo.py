import collections

import pygame

import core

WHITE = (255, 255, 255)
SILVER = (64, 64, 64)
RED = (200, 32, 32)
GREEN = (32, 220, 32)
YELLOW = (255, 255, 32)


def draw(screen, x, y, symbol, bot):
    x = x * 10
    y = y * 10
    if symbol == '#':
        pygame.draw.rect(screen, WHITE, [x+1, y+1, 8, 8], 0)
    if symbol == '@':
        pygame.draw.ellipse(screen, YELLOW, [x+1, y+1, 9, 9], 0)
    elif symbol == '.':
        screen.set_at((x+5, y+5), SILVER)
    elif symbol == '[':
        pygame.draw.rect(screen, GREEN, [x+2, y+2, 8, 8], 0)
    elif symbol == ']':
        pygame.draw.rect(screen, GREEN, [x, y+2, 8, 8], 0)


def main():
    options = core.get_options()
    world, moves, bot = core.load_input(options.filename)
    world = core.expand_world(world)
    bot = core.expand_bot(bot)

    pygame.init()
    screen = pygame.display.set_mode((world.width*10, world.height*10))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        for (y, row) in enumerate(world.lines):
            for (x, symbol) in enumerate(row):
                draw(screen, x, y, symbol, bot)
        # flip() the display to put your work on screen
        pygame.display.flip()
        if moves:
            print(len(moves))
            move = moves.pop(0)
            queue = collections.deque()
            can_move = core.make_space(world, bot, move, queue)
            if can_move:
                bot = core.move_all(world, bot, move, queue)
        clock.tick(25)  # limits FP
    pygame.quit()

if __name__ == '__main__':
    main()
