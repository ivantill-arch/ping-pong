from pygame import *

back = (200, 255, 255)
window = display.set_mode(600, 500)
display.set_caption('Пинг-понг')
window.fill(back)

clock = time.Clock()
FPS = 60
game = True

class Area():
    def __init__(self, x=0, y=0, widht=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, widht, height)
        self.fill_color = back
        if color:
            self.color = color

    def set_color(self, new_color):
        self.fill_color = new_color

    def painting(self):
        pygame.draw.rect(window, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Picture(Area):
    def __init__(self, name_image, x=0, y=0, widht=10, height=10):
        Area.__init__(self, x=x, y=y, widht=widht, height=height, color=None)
        self.image = pygame.image.load(name_image)
    
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)

