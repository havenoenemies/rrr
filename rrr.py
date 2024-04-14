from pygame import *

sprite1 = transform.scale(image.load('rrr.jpg'), (10, 100))

window = display.set_mode((700, 500))
display.set_caption('يهعلبت')
background = transform.scale(image.load('ttt.jpg'), (700, 500))


clock = time.Clock()
FPS = 30
clock.tick(FPS)


finish = False
game = True
while game:
    if finish != True:
        window.blit(background,(0, 0))
        window.blit(sprite1, (100, 100))


    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()  
    clock.tick(FPS)  
