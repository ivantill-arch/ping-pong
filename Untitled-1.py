from pygame import *

back = (200, 255, 255)
window = display.set_mode(600, 500)
window.fill(back)

clock = time.Clock()
FPS = 60
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)
