import pygame
from gun import Gun
import controls
from pygame.sprite import Group

def main():

    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Python noob invaders")
    bg_color = (0,30,0)
    gun = Gun(screen)
    bullets = Group()
    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        controls.update_bullets(bullets)
        controls.update(bg_color, screen, gun, bullets)







if __name__ == '__main__':
    main()
