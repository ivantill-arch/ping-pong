from pygame import *

back = (200, 255, 255)
window = display.set_mode(600, 500)
display.set_caption('Пинг-понг')
window.fill(back)

clock = time.Clock()
FPS = 60
game = True
finish = False


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Ball(GameSprite):
    def update(self):
        ball.player_x += self.speed
        ball.player_y += self.speed

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit((0,0))

    if keys_pressed[K_LEFT] and player.rect.y >30:
        player.rect.y -= speed
    if keys_pressed[K_RIGHT] and player.rect.y < 595:
        player.rect.y += speed    

    display.update()
    clock.tick(FPS)

