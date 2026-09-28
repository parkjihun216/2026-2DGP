from pico2d import *


open_canvas(800, 600)

boy = load_image('character.png')

while True:
    for event in get_events():
        pass

    clear_canvas()
    boy.draw(400, 300)
    update_canvas()

close_canvas()
