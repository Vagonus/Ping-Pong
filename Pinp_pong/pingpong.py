from pygame import *
from random import *

window = display.set_mode((500, 500))
display.set_caption('Ping Pong')
font.init()
font1 = font.SysFont('None', 30)
window.fill((0, 0, 0))




class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, player_z, player_c):
        super(). __init__()
        self.z = player_z
        self.c = player_c
        self.image = transform.scale(image.load(player_image), (self.z, self.c))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):#отобразить спрайт 
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 390:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 390:
            self.rect.y += self.speed        

ball = GameSprite('ball.png', 4, 250, 250, 40, 40)
wall1 = Player1('wall.png', 6, 3, 250, 20, 100)
wall2 = Player2('wall.png', 6, 480, 250, 20, 100)

x = 3
y = 3
left_point = 0
right_point = 0

font.init()
font = font.SysFont(None, 50)
lose1 = font.render('Игрок 1 Проиграл!', True, (255, 255, 255))
lose2 = font.render('Игрок 2 Проиграл', True, (255, 255, 255))

clock = time.Clock()
FPS = 60

finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        ball.rect.x += x
        ball.rect.y += y

        if ball.rect.y > 450 or ball.rect.y < 10:
            y *= -1

        if sprite.collide_rect(wall1, ball):
            x *= -1
            left_point += 1

        if sprite.collide_rect(wall2, ball):
            x *= -1
            right_point += 1

        window.fill((0, 0, 0))

        ball.update()
        ball.reset()

        wall1.update()
        wall1.reset()

        wall2.update()
        wall2.reset()

        if ball.rect.x < 5:
            finish = True
            window.blit(lose1, (110, 210))

        if ball.rect.x > 450:
            finish = True
            window.blit(lose2, (110, 210))

        text_left_point = font1.render('отбит мяч: ' + str(left_point), True, (255,255,255))
        window.blit(text_left_point, (5, 5))

        text_right_point = font1.render('отбит мяч: ' + str(right_point), True, (255,255,255))
        window.blit(text_right_point, (375, 5))

    else:
        time.delay(3000)
        finish = False
        ball = GameSprite('ball.png', 4, 250, 250, 40, 40)
        wall1 = Player1('wall.png', 6, 3, 250, 20, 100)
        wall2 = Player2('wall.png', 6, 480, 250, 20, 100)
        x = 3
        y = 3
        left_point = 0
        right_point = 0
        

    display.update()
    clock.tick(FPS)             