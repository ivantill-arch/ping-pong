from pygame import *

back = (200, 255, 255)
window = display.set_mode((600, 500))
display.set_caption('Пинг-понг')
window.fill(back)

clock = time.Clock()
FPS = 60
game = True
finish = False
speed_x = 3
speed_y = 3
speed = 10


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
        global speed_x
        global speed_y
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.x > 550 or ball.rect.x < 0:
            speed_x *= -1
        if ball.rect.y > 450 or ball.rect.y <0:
            speed_y *= -1




racket1 = GameSprite('racket.png', 500, 200, 5)
racket2 = GameSprite('racket.png', 0, 200, 5)
ball = Ball('pong.png', 100, 200, 3)
font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSE!!!', True, (180, 0, 0))
font2 = font.Font(None, 35)
lose2 = font2.render('PLAYER 2 LOSE!!!', True, (180, 0, 0))

while game:
    window.fill(back)
    for e in event.get():
        if e.type == QUIT:
            game = False
 


    if finish != True:
        ball.update()
        racket1.update()
        racket2.update()

    

        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and racket1.rect.y > 1:
            racket1.rect.y -= speed
        if keys_pressed[K_DOWN] and racket1.rect.y < 430:
            racket1.rect.y += speed

        if keys_pressed[K_w] and racket2.rect.y > 1:
            racket2.rect.y -= speed
        if keys_pressed[K_s] and racket2.rect.y < 430:
            racket2.rect.y += speed

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1

        
            
        
        ball.reset()
        racket1.reset()
        racket2.reset()
    
    if ball.rect.x < 0:
        window.blit(lose1, (200, 200))
        finish = True
    if ball.rect.x > 500:
        window.blit(lose2, (200, 200))
        finish = True

    display.update()
    clock.tick(FPS)
