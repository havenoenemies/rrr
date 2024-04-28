from pygame import *
from random import *


window = display.set_mode((700, 500))
display.set_caption('يهعلبت')
background = transform.scale(image.load('wh.jpg'), (700, 500))


clock = time.Clock()
FPS = 30
clock.tick(FPS)

class GameSprite(sprite.Sprite):
        def __init__(self,player_image,player_x,player_y,player_speed,player_asd,player_hh):
             super().__init__()
             self.image = transform.scale(image.load(player_image),(player_asd,player_hh))
             self.speed = player_speed
             self.speedX = player_speed
             self.speedY = player_speed
             self.rect = self.image.get_rect()
             self.rect.x = player_x
             self.rect.x = player_y
        def reset(self):
             window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
     def update(self):
          keys_pressed = key.get_pressed()
          if keys_pressed[K_w]:
               self.rect.y -= self.speed
          if keys_pressed[K_s]:
               self.rect.y += self.speed

class Enemy(GameSprite):
     def update(self):
          keys_pressed = key.get_pressed()
          if keys_pressed[K_UP]:
               self.rect.y -= self.speed
          if keys_pressed[K_DOWN]:
               self.rect.y += self.speed


class Ball(GameSprite):
     def update(self):
        self.rect.x += self.speedX
        self.rect.y += self.speedY
        if self.rect.x <= 0:
           self.rect.x = 500

        if self.rect.x >= 650:
            self.rect.x = 100

        if self.rect.y <= 0:
             self.speedY *= -1
        if self.rect.y >= 450:
             self.speedY *= -1
        if sprite.collide_rect(sprite1, sprite3):
             self.speedX *= -1
            
        if sprite.collide_rect(sprite2, sprite3):
             self.speedX *= -1

        
sprite1 = Player('player.png', 630,200,5)
sprite2 = Enemy('player2.jpg', 5,200,5)
sprite3 = Player('ball.jpg', 30,80,5)


finish = False
game = True

while game:
    if finish != True:
        window.blit(background,(0, 0))
        sprite1.reset()
        sprite1.update()
        sprite2.reset()
        sprite2.update()
        sprite3.reset()
        sprite3.update()
        display.update()

    def reset(self):
         window.blit(self.image,(self.rect.x,self.rect.y))



    for e in event.get():
        if e.type == QUIT:
            game = False


    clock.tick(FPS)  
