from pygame import *
from random import *

score1 = 0
score2 = 0

window = display.set_mode((700, 500))
display.set_caption('يهعلبت')
background = transform.scale(image.load('bckgrd.png'), (700, 500))


font.init()
font1 = font.Font(None, 36)


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
        global score1, score2
        self.rect.x += self.speedX
        self.rect.y += self.speedY
        if self.rect.x <= 0:
          self.rect.x = 500
          score2 = score2 + 1

        if self.rect.x >= 650:  
          self.rect.x = 100
          score1 = score1 + 1

        if self.rect.y <= 0:
             self.speedY *= -1
        if self.rect.y >= 450:
             self.speedY *= -1
        if sprite.collide_rect(sprite1, sprite3):
             self.speedX *= -1
            
        if sprite.collide_rect(sprite2, sprite3):
             self.speedX *= -1

        
sprite1 = Player('player.png', 200, 0, 7, 15, 80)
sprite2 = Enemy('player2.jpg', 200, 685, 7, 15, 80)
sprite3 = Ball('ball.png', 30, 80, 7, 70, 50)


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
          text1 = font1.render(str(score1) + ':' + str(score2), 1, (255, 255 , 255))
          window.blit(text1, (330, 50))
        



     for e in event.get():
          if e.type == QUIT:
               game = False

     display.update()
     clock.tick(FPS)  
