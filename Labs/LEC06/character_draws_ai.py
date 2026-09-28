from math import cos, hypot, pi, sin
from pathlib import Path

from pico2d import *


CANVAS_SIZE = (800, 600)
FRAME_DELAY = 0.01
PIXELS_PER_STEP = 5

CIRCLE_CENTER = (400, 300)
CIRCLE_RADIUS = 200

RECTANGLE_VERTICES = (
    (50, 550),
    (750, 550),
    (750, 50),
    (50, 50),
)

TRIANGLE_VERTICES = (
    (100, 100),
    (700, 100),
    (400, 500),
)


def process_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            return False
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            return False
    return True


def make_line_points(start, end):
    x0, y0 = start
    x1, y1 = end
    distance = hypot(x1 - x0, y1 - y0)
    steps = max(1, round(distance / PIXELS_PER_STEP))

    return [
        (
            x0 + (x1 - x0) * step / steps,
            y0 + (y1 - y0) * step / steps,
        )
        for step in range(steps + 1)
    ]


def make_polygon_points(vertices):
    points = []

    for index, start in enumerate(vertices):
        end = vertices[(index + 1) % len(vertices)]
        edge_points = make_line_points(start, end)

        if points:
            edge_points = edge_points[1:]

        points.extend(edge_points)

    return points


def make_circle_points():
    center_x, center_y = CIRCLE_CENTER

    return [
        (
            center_x + CIRCLE_RADIUS * cos(2 * pi * degree / 360),
            center_y + CIRCLE_RADIUS * sin(2 * pi * degree / 360),
        )
        for degree in range(360)
    ]


def draw_frame(character, position):
    clear_canvas()
    character.draw(*position)
    update_canvas()
    delay(FRAME_DELAY)


def play_route(character, route):
    for position in route:
        if not process_events():
            return False
        draw_frame(character, position)

    return True


def main():
    open_canvas(*CANVAS_SIZE)

    image_path = Path(__file__).with_name('character.png')
    character = load_image(str(image_path))

    routes = (
        make_circle_points(),
        make_polygon_points(RECTANGLE_VERTICES),
        make_polygon_points(TRIANGLE_VERTICES),
    )

    running = True

    try:
        while running:
            for route in routes:
                running = play_route(character, route)
                if not running:
                    break
    finally:
        close_canvas()


if __name__ == '__main__':
    main()
