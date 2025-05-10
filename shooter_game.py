from pygame import *

win = display.set_mode((700,500))
display.set_caption('Ping-pong')
game = True
background = (0,0,0)
FPS = 90
class Gamesprite(sprite.Sprite):
    def __init__(self, p_image, p_y, p_x, s_y1, s_x1, p_speed):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (s_x1, s_y1))
        self.speed = p_speed

        self.rect = self.image.get_rect()

        self.rect.x = p_x
        self.rect.y = p_y

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
        
class Player1(Gamesprite):
    def walking1(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 15:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 395:
            self.rect.y += self.speed
            
class Player2(Gamesprite):
    def walking2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 15:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 395:
            self.rect.y += self.speed


player1 = Player1('ракетка2.png', 250, 50, 100, 20, 5)
player2 = Player2('ракетка2.png', 250, 650, 100, 20, 5)
ball = Gamesprite('мяч.png', 250, 350, 50, 90, 5)
clock = time.Clock()
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
            
    win.fill(background)
    player1.reset()
    player1.walking1()
    player2.reset()
    player2.walking2()
    ball.reset()
    display.update()
    clock.tick(FPS)
