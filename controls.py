import pygame, sys
from bullet import Bullet
from enemie import Enemy
import math, time


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



def update(bg_color, screen, gun, enemyGroup,bullets, stats, scores):

    screen.fill(bg_color)
    check_high_score(stats,scores)
    scores.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    enemyGroup.draw(screen)

    pygame.display.flip()




def update_bullets(enemyGroup, bullets, screen, stats, scores):
    """updates bullets positions"""
    bullets.update()

    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, enemyGroup, True, True)
    if collisions:
        for enemyGroup in collisions .values():
            stats.score += 10 * len(enemyGroup)
        scores.image_score()
        #scores.image_guns()
    if len(enemyGroup) == 0:
        bullets.empty()
        create_army(screen, enemyGroup)





def create_army(screen, enemyGroup):
    """creates an enemy army"""
    enemy = Enemy(screen)
    enemy_height = enemy.rect.height
    enemy_width = enemy.rect.width
    width, height = screen.get_size()
    amountx = 20
    amounty = 4

    for row_number in range(amounty ):
        for enemy_number in range(amountx):
            print(enemy_number)
            enemy = Enemy(screen)
            enemy.rect.x = 110+ enemy_width * enemy_number + enemy_number * 15
            enemy.y = (enemy_height + 30) * row_number
            enemy.rect.y = enemy.y
            enemyGroup.add(enemy)



def update_enemies(gun, enemyGroup,stats, screen, bullets, scores):
    """Updates positions of enemies group"""


    enemyGroup.update()
    if pygame.sprite.spritecollideany(gun, enemyGroup):
        print('\/  \/')
        gun_kill(stats, screen, gun, enemyGroup, bullets, scores)
    enemies_passed(stats, screen, gun, enemyGroup, bullets, scores)


def gun_kill(stats, screen, gun, enemyGroup, bullets, scores):
    if stats.gun_hp > 0:
        #scores.image_guns()
        stats.gun_hp -= 1
        gun.create_gun()
        bullets.empty()
        enemyGroup.empty()

        create_army(screen, enemyGroup)




    else:
        stats.run_game = False
        sys.exit()

def enemies_passed(stats, screen, gun, enemyGroup, bullets, scores):
    """checks if enemies are passed through defender"""
    screen_rect = screen.get_rect()
    for enemy in enemyGroup.sprites():
        if enemy.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, gun, enemyGroup, bullets, scores)
            break

def check_high_score(stats,scores):
    if stats.score >= stats.high_score:
        stats.high_score = stats.score
        scores.image_high_score()
        with open('high_score','w') as f:
            f.write(str(stats.high_score))









