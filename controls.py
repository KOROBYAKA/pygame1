import pygame, sys
from bullet import Bullet
from enemie import Enemy
import math


def events(screen,gun,bullets):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #to the righ
                    gun.mright = True
            if event.key == pygame.K_LEFT:
                #to the left
                    gun.mleft = True
            if event.key == pygame.K_SPACE:
                    new_bullet = Bullet(screen, gun)
                    bullets.add(new_bullet)




        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                #to the right
                    gun.mright = False
            if event.key == pygame.K_LEFT:
                #to the left
                    gun.mleft = False



def update(bg_color, screen, gun, enemyGroup, bullets ):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    enemyGroup.draw(screen)
    pygame.display.flip()




def update_bullets(bullets):
    """updates bullets positions"""
    bullets.update()
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def create_army(screen, enemyGroup):
    """creates an enemy army"""
    enemy = Enemy(screen)
    enemy_height = enemy.rect.height
    enemy_width = enemy.rect.width
    width, height = screen.get_size()
    amountx = int((width - 2 * (enemy_width + 7)) / (enemy_width + 7))
    amounty = 7

    for row_number in range(amounty ):
        for enemy_number in range(amountx):
            enemy = Enemy(screen)
            enemy.rect.x = enemy_width * enemy_number + enemy_number * 10 + 18
            enemy.y  = (enemy_height + 15) * row_number
            enemy.rect.y = enemy.y
            print(len(enemyGroup))
            enemyGroup.add(enemy)



def update_enemies(enemyGroup):
    """Updates positions of enemies group"""
    enemyGroup.update()