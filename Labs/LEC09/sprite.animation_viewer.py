"""Play the Sonic sprite sheet with pico2d."""

from pathlib import Path

import pico2d as p2d

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
SPRITE_PATH = Path(__file__).with_name('sonic-sprite.png')


def load_sprite():
    if not SPRITE_PATH.is_file():
        raise FileNotFoundError(f'Sprite sheet not found: {SPRITE_PATH}')
    try:
        return p2d.load_image(str(SPRITE_PATH))
    except Exception as error:
        raise RuntimeError(f'Cannot load sprite sheet {SPRITE_PATH}: {error}') from error


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
        sprite = load_sprite()
        while handle_events():
            p2d.clear_canvas()
            sprite.draw(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2)
            p2d.update_canvas()
            p2d.delay(0.01)
    finally:
        p2d.close_canvas()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
