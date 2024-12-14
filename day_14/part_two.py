#!/usr/bin/env python3

import core
import math
from PIL import Image
from sklearn.cluster import KMeans

from rich.progress import track


def find_candidate(frame, bots):
    dataset = [
        (b.position.x, b.position.y)
        for b in bots
        ]
    kmeans = KMeans(n_clusters=1)
    kmeans.fit(dataset)
    return kmeans.inertia_


def save_frame(frame, space, bots):
    img = Image.new(mode="RGB", size=(space.x*3, space.y*3))
    for bot in bots:
        x = bot.position.x * 3
        y = bot.position.y * 3

        img.putpixel((x-1, y-1), (125, 155, 55))
        img.putpixel((x, y-1), (155, 155, 55))
        img.putpixel((x+1, y-1), (125, 155, 55))

        img.putpixel((x-1, y), (125, 255, 55))
        img.putpixel((x, y), (255, 255, 55))
        img.putpixel((x+1, y), (125, 255, 55))

        img.putpixel((x-1, y+1), (125, 155, 55))
        img.putpixel((x, y+1), (155, 155, 55))
        img.putpixel((x+1, y+1), (125, 155, 55))

    img.save(f'frames/frame_{frame:05d}.png')


def main(options):
    space = core.Vector2(*(int(_) for _ in options.size.split('x')))
    if options.trace:
        print(f'space is {space.x} x {space.y}')
    bots = list(core.load_input(options.filename))
    min_score = math.inf
    frame = None
    for tick in track(range(0, 10404)):
        for bot in bots:
            bot.move(space)
        value = find_candidate(tick, bots)
        if value < min_score:
            min_score = value
            frame = tick
        if 8200 <= tick < 8321:
            save_frame(tick, space, bots)
    print(min_score, 'at', frame)
    return frame + 1  # Frames start by 0

if __name__ == '__main__':
    sol = main(core.get_options())
    print(f'[Day 8] Sol. part two is: {sol}')
