from pico2d import *
import math


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FRAME_DELAY = 0.01
CIRCLE_CENTER_X = 400
CIRCLE_CENTER_Y = 300
CIRCLE_RADIUS = 200


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

boy = load_image('character.png')

running = True


def draw_boy(x, y):
    global running

    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

    if not running:
        return

    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(FRAME_DELAY)


def move_top_edge():
    for x in range(50, 751, 5):
        if not running:
            break
        draw_boy(x, 550)


def move_right_edge():
    for y in range(550, 49, -5):
        if not running:
            break
        draw_boy(750, y)


def move_bottom_edge():
    for x in range(750, 49, -5):
        if not running:
            break
        draw_boy(x, 50)


def move_left_edge():
    for y in range(50, 551, 5):
        if not running:
            break
        draw_boy(50, y)


def move_rectangle():
    move_top_edge()
    if running:
        move_right_edge()
    if running:
        move_bottom_edge()
    if running:
        move_left_edge()


def move_circle():
    for degree in range(360):
        if not running:
            break
        theta = math.radians(degree)
        x = CIRCLE_CENTER_X + CIRCLE_RADIUS * math.cos(theta)
        y = CIRCLE_CENTER_Y + CIRCLE_RADIUS * math.sin(theta)
        draw_boy(x, y)


def move_line(x0, y0, x1, y1, steps):
    for step in range(steps + 1):
        if not running:
            break
        t = step / steps
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        draw_boy(x, y)


def move_a_to_b():
    move_line(100, 100, 700, 100, 120)


def move_b_to_c():
    move_line(700, 100, 400, 500, 100)


def move_c_to_a():
    move_line(400, 500, 100, 100, 100)


def move_triangle():
    move_a_to_b()
    if running:
        move_b_to_c()
    if running:
        move_c_to_a()


while running:
    move_circle()
    if running:
        move_rectangle()
    if running:
        move_triangle()

close_canvas()
