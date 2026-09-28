from pico2d import *


open_canvas(800, 600)

boy = load_image('character.png')

running = True

while running:
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False

    clear_canvas()
    boy.draw(400, 300)
    update_canvas()

close_canvas()
