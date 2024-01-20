from pygame import *
from random import *

window = display.set_mode((700, 500))
display.set_caption('Шутер')
font.init()
font1 = font.SysFont('Arial', 30)

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

background = transform.scale(image.load('galaxy.jpg'), (700, 500))
window.blit(background, (0, 0))

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

bullets = sprite.Group()

class Player(GameSprite):
    def update(self):

        keys_pressed = key.get_pressed()
    
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 590:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', 8, self.rect.centerx - 7, self.rect.top, 15, 20)
        bullets.add(bullet)


lost = 0

class Enemy(GameSprite):
    direction = 'down'
    def update(self):
        direction = 'down'
        if self.rect.y <= 0:
            self.direction = 'down'
              
        if self.direction == 'down':
            self.rect.y += self.speed
        global lost
        if self.rect.y >= 500:
            self.rect.x = randint(20, 600)
            self.rect.y = 0
            lost = lost + 1



class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill()
              
DNSs = sprite.Group()
asteroids = sprite.Group()

player = Player('rocket.png', 10, 5, 370, 80, 112)
for i in range(5):
    DNS = Enemy('ufo.png', randint(1, 3), randint(20, 600), randint(0, 0), 76, 45)
    DNSs.add(DNS)
for i in range(3):
    asteroid = Enemy('asteroid.png', randint(1, 3), randint(20, 600), randint(0, 0), 50, 50)
    asteroids.add(asteroid)


font.init()
font = font.SysFont('Arial', 80)
win = font.render('YOU WIN!', True, (255, 215, 5))
lose = font.render('YOU LOSE!', True, (255, 5, 5))

clock = time.Clock()
FPS = 60

lives = 3
account = 0

finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
                fire = mixer.Sound('fire.ogg')
                fire.play()  

    if finish != True: 
        window.blit(background,(0, 0))
        player.reset()
        player.update()
        
        bullets.update()
        bullets.draw(window)

        DNS.reset()
        DNSs.update()
        DNSs.draw(window)

        asteroid.reset()
        asteroids.update()
        asteroids.draw(window)


        sprite_list = sprite.groupcollide(DNSs, bullets, True, True)
        for i in sprite_list:
            account = account + 1
            DNS = Enemy('ufo.png', randint(1, 3), randint(20, 600), randint(0, 0), 76, 45)
            DNSs.add(DNS)

        sprite_list1 = sprite.spritecollide(player, asteroids, True)
        for i in sprite_list1:
            lives = lives - 1
            asteroid = Enemy('asteroid.png', randint(1, 3), randint(20, 600), randint(0, 0), 50, 50)
            asteroids.add(asteroid)



        text_lose = font1.render('Пропущено: ' + str(lost), True, (255,255,255))
        window.blit(text_lose, (5, 30))

        text_point = font1.render('Счет: ' + str(account), True, (255,255,255))
        window.blit(text_point, (5, 5))
        
        text_live = font1.render('Жизни: ' + str(lives), True, (255, 255, 255))
        window.blit(text_live, (5, 55))

        if lost >= 10 or sprite.spritecollide(player, DNSs, False) or lives == 0:
            finish = True
            window.blit(lose, (200, 200))

        if account >= 100:
            finish = True
            window.blit(win, (200, 200))
    else:
        time.delay(3000)
        finish = False
        for i in DNSs:
            i.kill()
            lost = 0
            account = 0

        for i in asteroids:
            i.kill()
            lives = 3
            
        for i in bullets:
            i.kill()

        for i in range(5): 
            DNS = Enemy('ufo.png', randint(1, 3), randint(20, 600), randint(0, 0), 76, 45)
            DNSs.add(DNS)   

        for i in range(3):
            asteroid = Enemy('asteroid.png', randint(1, 3), randint(20, 600), randint(0, 0), 50, 50)
            asteroids.add(asteroid)

             

    display.update()
    clock.tick(FPS) 


