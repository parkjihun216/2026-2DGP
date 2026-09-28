from pico2d import *
import math


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FRAME_DELAY = 0.01


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


def move_top():
    for x in range(50, 751, 5):
        if not running:
            break
        draw_boy(x, 550)


def move_right():
    for y in range(550, 49, -5):
        if not running:
            break
        draw_boy(750, y)


def move_bottom():
    for x in range(750, 49, -5):
        if not running:
            break
        draw_boy(x, 50)


def move_left():
    for y in range(50, 551, 5):
        if not running:
            break
        draw_boy(50, y)


def move_rectangle():
    move_top()
    if running:
        move_right()
    if running:
        move_bottom()
    if running:
        move_left()


def move_circle():
    for degree in range(360):
        if not running:
            break
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)
        draw_boy(x, y)


def move_a_to_b():
    n = 120
    for step in range(n + 1):
        if not running:
            break
        t = step / n
        x = 100 + (700 - 100) * t
        y = 100 + (100 - 100) * t
        draw_boy(x, y)


def move_b_to_c():
    n = 100
    for step in range(n + 1):
        if not running:
            break
        t = step / n
        x = 700 + (400 - 700) * t
        y = 100 + (500 - 100) * t
        draw_boy(x, y)


def move_c_to_a():
    n = 100
    for step in range(n + 1):
        if not running:
            break
        t = step / n
        x = 400 + (100 - 400) * t
        y = 500 + (100 - 500) * t
        draw_boy(x, y)


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
