import pygame
from gun import Gun
import controls
from pygame.sprite import Group
from enemie import Enemy
from stats import  Stats
from scores import Scores


def main():

    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Python noob invaders")
    bg_color = (5,5,5)
    gun = Gun(screen)
    bullets = Group()
    enemyGroup = Group()
    controls.create_army(screen, enemyGroup)
    stats = Stats()
    scores = Scores(screen, stats)

    while True:

        controls.events(screen, gun, bullets)
        gun.update_gun()
        controls.update(bg_color, screen, gun, enemyGroup,bullets, stats, scores)
        controls.update_enemies(gun, enemyGroup,stats, screen, bullets, scores)
        controls.update_bullets(enemyGroup, bullets, screen, stats, scores)









if __name__ == '__main__':
    main()
