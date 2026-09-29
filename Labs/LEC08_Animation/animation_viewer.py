from pathlib import Path

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600

FRAME_HEIGHT = 256
DRAW_HEIGHT = 420

CENTER_X = CANVAS_WIDTH / 2
CENTER_Y = CANVAS_HEIGHT / 2
REPEAT_COUNT = 5
PAUSE_DURATION = 1.0

ANIMATIONS = (
    {
        'name': 'walk',
        'frames': ((50, 220), (280, 220), (510, 220),
                   (740, 220), (970, 220), (1200, 220)),
        'frame_y': 768,
        'interval': 0.18,
    },
    {
        'name': 'run',
        'frames': ((15, 205), (225, 210), (435, 188), (623, 193),
                   (815, 192), (1006, 186), (1192, 168), (1360, 176)),
        'frame_y': 512,
        'interval': 0.12,
    },
    {
        'name': 'jump',
        'frames': ((45, 150), (255, 180), (445, 177), (629, 177),
                   (815, 200), (1015, 205), (1235, 170)),
        'frame_y': 256,
        'interval': 0.10,
    },
    {
        'name': 'attack',
        'frames': ((20, 185), (205, 150), (355, 140), (495, 130),
                   (625, 170), (795, 220), (1015, 185),
                   (1200, 180), (1380, 156)),
        'frame_y': 0,
        'interval': 0.10,
    },
)


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            return False
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            return False
    return True


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

image_path = Path(__file__).with_name('night.png')
knight = load_image(str(image_path))

running = True
animation_index = 0
frame = 0
frame_elapsed = 0.0
completed_cycles = 0
is_paused = False
pause_elapsed = 0.0
previous_time = get_time()

while running:
    current_time = get_time()
    elapsed = current_time - previous_time
    previous_time = current_time

    animation = ANIMATIONS[animation_index]

    if is_paused:
        pause_elapsed += elapsed

        if pause_elapsed >= PAUSE_DURATION:
            is_paused = False
            pause_elapsed = 0.0
            animation_index = (animation_index + 1) % len(ANIMATIONS)
            animation = ANIMATIONS[animation_index]
            frame = 0
            frame_elapsed = 0.0
    else:
        frame_elapsed += elapsed

        while frame_elapsed >= animation['interval'] and not is_paused:
            frame_elapsed -= animation['interval']
            frame += 1

            if frame >= len(animation['frames']):
                completed_cycles += 1

                if completed_cycles >= REPEAT_COUNT:
                    completed_cycles = 0
                    frame = len(animation['frames']) - 1
                    is_paused = True
                    pause_elapsed = 0.0
                else:
                    frame = 0

    clear_canvas()
    source_x, source_width = animation['frames'][frame]
    draw_width = DRAW_HEIGHT
    knight.clip_draw(
        source_x,
        animation['frame_y'],
        source_width,
        FRAME_HEIGHT,
        CENTER_X,
        CENTER_Y,
        draw_width,
        DRAW_HEIGHT,
    )
    update_canvas()

    running = handle_events()
    delay(0.01)

close_canvas()
