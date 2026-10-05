"""Play the Sonic sprite sheet with pico2d."""

import pico2d as p2d

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600


def handle_events():
    for event in p2d.get_events():
        if event.type == p2d.SDL_QUIT:
            return False
        if event.type == p2d.SDL_KEYDOWN and event.key == p2d.SDLK_ESCAPE:
            return False
    return True


def main():
    p2d.open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        while handle_events():
            p2d.clear_canvas()
            p2d.update_canvas()
            p2d.delay(0.01)
    finally:
        p2d.close_canvas()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
