from pico2d import *


open_canvas(800, 600)

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
    delay(0.01)


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


move_top()
if running:
    move_right()

close_canvas()
