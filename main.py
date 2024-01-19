import pygame
import sys
from gun import Gun


def main():

    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Space Invaders")
    bg_color = (0,30,0)
    gun = Gun(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        screen.fill(bg_color)
        gun.output()
        pygame.display.flip()






if __name__ == '__main__':
    main()