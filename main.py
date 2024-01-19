import pygame
from gun import Gun
import controls


def main():

    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Python noob invaders")
    bg_color = (0,30,0)
    gun = Gun(screen)

    while True:
        controls.events(gun)
        gun.update_gun()
        screen.fill(bg_color)
        gun.output()
        pygame.display.flip()






if __name__ == '__main__':
    main()
