from pico2d import *

open_canvas()

school = load_image('TUK_GROUND.png')
character = load_image('charter4direction.png')

def handle_events():
    global running, dir, dir2,dir_char
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
        
            if event.key == SDLK_RIGHT:
                dir += 1
                dir_char = 0
            elif event.key == SDLK_LEFT:
                dir -= 1
                dir_char = 2
            elif event.key == SDLK_UP:
                dir2 += 1
                dir_char = 3
            elif event.key == SDLK_DOWN:
                dir2 -= 1
                dir_char = 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                dir2 -= 1

            elif event.key == SDLK_DOWN:
                dir2 += 1

running = True
x = 800 // 2
y = 90
frame = 0
dir_char = 0
dir = 0
dir2 = 0
while running:
    clear_canvas()
    school.draw(400, 300)
    if frame == 8 and dir_char == 3:
        character.clip_draw(frame * 100 + 5, dir_char * 100 - 5 , 125, 180, x, y,70,90)
    else :
        character.clip_draw(frame * 100, dir_char * 100, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 9
    x += dir * 5
    y += dir2 * 5
    delay(0.05)