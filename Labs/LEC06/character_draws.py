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


while running:
    draw_boy(400, 300)

close_canvas()
