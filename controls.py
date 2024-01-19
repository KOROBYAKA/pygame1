import pygame, sys



def events(gun):

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
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                #to the right
                    gun.mright = False
            if event.key == pygame.K_LEFT:
                #to the left
                    gun.mleft = False



