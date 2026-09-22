from pico2d import *
import math


open_canvas(800, 600)

boy = load_image('character.png')


def draw_boy(x, y):
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(0.01)


def move_circle():
    for degree in range(360):
        theta = math.radians(degree)

        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        draw_boy(x, y)


def move_rectangle():
    print('rectangle')


def move_triangle():
    print('triangle')


while True:
    move_circle()
    move_rectangle()
    move_triangle()
    break

close_canvas()