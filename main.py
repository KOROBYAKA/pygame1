import pygame
from gun import Gun
import controls
from pygame.sprite import Group
from enemie import Enemy

def main():

    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Python noob invaders")
    bg_color = (5,5,5)
    gun = Gun(screen)
    bullets = Group()
    enemyGroup = Group()
    controls.create_army(screen, enemyGroup)


    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        controls.update_enemies(enemyGroup)
        controls.update(bg_color, screen, gun, enemyGroup,bullets)
        controls.update_bullets(bullets)








if __name__ == '__main__':
    main()
