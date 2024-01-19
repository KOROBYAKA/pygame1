import pygame, math

#gun logic



#some global variables
move_speed = 1.1/math.sqrt(2)


class Gun():

    def __init__(self,screen):
        """Gun initialization"""
        self.screen = screen
        self.image = pygame.image.load('images/space_ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 2
        self.gun_center = float(self.rect.centerx)
        self.mright = False
        self.mleft = False




    def output(self):
        """print gun"""
        self.screen.blit(self.image,self.rect)



    def update_gun(self):
        """update of gun position"""
        if self.mright and self.rect.right < self.screen_rect.right +28:
            self.gun_center += move_speed
        if self.mleft and self.rect.left >  self.screen_rect.left +28:
            self.gun_center -= move_speed

        self.rect.centerx = self.gun_center


    #def shoot(self):



