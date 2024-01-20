import time

import pygame
import random
import math


#colors
r = (0,0,255)
y = (255, 251, 0)
b = (0, 0, 255)
p = (255, 0, 228)
f = (0, 255, 42)
c1 = (0, 255, 119)
c2 = (198, 0, 255)
c3 = (255, 0, 48)
c4 = (255, 147, 0)
def randomColor():
#making random colors
    colors = (r,y,b,p,f,c1,c2,c3,c4)
    rand = random.randint(0,len(colors)-1)

    return colors[rand ]


def random_speed():
    rand = random.randint(0,5)/1000
    rand2= random.randint(0,1)
    if rand2:
        return -rand
    else:
        return rand
class Bullet(pygame.sprite.Sprite):

    def __init__(self,screen,gun):
        """making bullet at actual gun position"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 4, 12)
        self.speed = 20/math.sqrt(2) + random_speed()
        self.color = randomColor()
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """bullet movement up"""
        self.y -= self.speed
        self.rect.y = self.y



    def draw_bullet(self):
        """drawing bullet"""
        for i in range(1,10):
            pygame.draw.rect(self.screen, self.color, self.rect)