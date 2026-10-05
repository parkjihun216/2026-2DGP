"""Play the Sonic sprite sheet with pico2d."""

from pathlib import Path

import pico2d as p2d

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
SCALE = 4
FRAME_INTERVAL = 0.1
REPEAT_COUNT = 5
PAUSE_DURATION = 1.0
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
    {
        'name': 'A03',
        'frames': (
            (1, 361, 33, 40), (39, 362, 35, 39),
            (89, 362, 35, 38), (130, 362, 34, 42),
            (181, 362, 34, 41), (228, 363, 33, 40),
        ),
    },
    {
        'name': 'A04',
        'frames': (
            (1, 326, 29, 30), (35, 327, 29, 31),
            (67, 327, 30, 29), (98, 327, 31, 29),
            (131, 327, 29, 30), (162, 326, 29, 31),
            (193, 326, 30, 29), (230, 326, 31, 29),
            (268, 325, 30, 30),
        ),
    },
    {
        'name': 'A05',
        'frames': (
            (1, 292, 30, 27), (36, 292, 29, 27),
            (70, 292, 29, 27), (105, 292, 29, 27),
            (139, 292, 29, 27), (174, 292, 29, 27),
        ),
    },
    {
        'name': 'A06',
        'frames': (
            (1, 251, 29, 35), (36, 251, 30, 35),
            (74, 251, 31, 35), (111, 251, 31, 36),
            (149, 251, 30, 35), (186, 251, 31, 36),
        ),
    },
    {
        'name': 'A07',
        'frames': (
            (1, 207, 29, 35), (36, 207, 30, 35),
            (72, 208, 39, 31), (123, 208, 39, 32),
            (172, 208, 39, 31), (218, 208, 38, 32),
        ),
    },
    {
        'name': 'A08',
        'frames': (
            (1, 154, 24, 45), (31, 154, 29, 44),
            (65, 154, 20, 44), (90, 155, 25, 43),
            (119, 155, 25, 43), (149, 154, 20, 44),
            (184, 156, 40, 28), (232, 157, 39, 27),
        ),
    },
    {
        'name': 'A09',
        'frames': (
            (1, 108, 27, 38), (31, 110, 31, 36),
            (64, 110, 31, 36), (99, 110, 33, 38),
            (136, 110, 32, 36), (176, 110, 33, 36),
            (217, 110, 33, 36), (254, 111, 33, 36),
        ),
    },
    {
        'name': 'A10',
        'frames': (
            (6, 56, 34, 40), (49, 56, 34, 43),
            (96, 59, 23, 39), (125, 59, 23, 39),
        ),
    },
)


class Playback:
    def __init__(self, animations=ANIMATIONS):
        self.animations = animations
        self.animation_index = 0
        self.frame_index = 0
        self.frame_elapsed = 0.0
        self.completed_cycles = 0
        self.is_paused = False
        self.pause_elapsed = 0.0

    def start_animation(self, index):
        self.animation_index = index
        self.frame_index = 0
        self.frame_elapsed = 0.0
        self.completed_cycles = 0
        self.is_paused = False
        self.pause_elapsed = 0.0

    @property
    def animation(self):
        return self.animations[self.animation_index]

    @property
    def frame(self):
        return self.animation['frames'][self.frame_index]

    def update(self, elapsed):
        if self.is_paused:
            self.pause_elapsed += elapsed
            if self.pause_elapsed >= PAUSE_DURATION:
                next_index = self.animation_index + 1
                if next_index < len(self.animations):
                    self.start_animation(next_index)
            return
        self.frame_elapsed += elapsed
        if self.frame_elapsed < FRAME_INTERVAL:
            return
        # Advance once so a delayed render never skips an unseen frame.
        self.frame_elapsed = 0.0
        self.frame_index += 1
        if self.frame_index >= len(self.animation['frames']):
            self.completed_cycles += 1
            if self.completed_cycles == REPEAT_COUNT:
                self.frame_index = len(self.animation['frames']) - 1
                self.is_paused = True
            else:
                self.frame_index = 0


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
        playback = Playback()
        previous_time = p2d.get_time()
        while handle_events():
            current_time = p2d.get_time()
            playback.update(current_time - previous_time)
            previous_time = current_time
            p2d.clear_canvas()
            draw_frame(sprite, playback.frame)
            p2d.update_canvas()
            p2d.delay(0.01)
    finally:
        p2d.close_canvas()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
