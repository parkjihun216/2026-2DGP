"""Play the Sonic sprite sheet with pico2d."""

from pathlib import Path

import pico2d as p2d

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
SCALE = 4
SPRITE_PATH = Path(__file__).with_name('sonic-sprite.png')
ANIMATIONS = (
    {
        'name': 'A01',
        'frames': (
            (1, 447, 29, 39), (31, 447, 26, 38),
            (58, 447, 28, 39), (86, 447, 30, 38),
            (118, 447, 30, 38), (150, 447, 30, 38),
            (182, 447, 29, 38), (211, 448, 29, 38),
            (240, 448, 29, 38), (270, 448, 24, 32),
            (302, 448, 29, 26),
        ),
    },
    {
        'name': 'A02',
        'frames': (
            (8, 408, 26, 37), (37, 408, 27, 37),
            (65, 407, 31, 38), (97, 408, 37, 37),
            (135, 410, 32, 35), (170, 408, 32, 38),
            (206, 408, 26, 38), (238, 408, 24, 37),
            (263, 408, 30, 37), (295, 408, 36, 37),
            (334, 409, 32, 36), (370, 408, 29, 38),
        ),
    },
)


def draw_frame(sprite, frame):
    left, bottom, width, height = frame
    sprite.clip_draw(left, bottom, width, height,
                     CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2,
                     width * SCALE, height * SCALE)


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
        p2d.hide_lattice()
        sprite = load_sprite()
        while handle_events():
            p2d.clear_canvas()
            draw_frame(sprite, ANIMATIONS[0]['frames'][0])
            p2d.update_canvas()
            p2d.delay(0.01)
    finally:
        p2d.close_canvas()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
