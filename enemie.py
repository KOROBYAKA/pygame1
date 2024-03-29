import pygame

class Enemy(pygame.sprite.Sprite):
    """Ebeny class"""

    def __init__(self, screen):
        self.screen = screen
        super(Enemy, self).__init__()
        self.image = pygame.image.load('images/enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)




    def draw(self):
        """prints enemy on the screen"""
        self.screen.blit(self.image, self.rect)


    def update(self):
        self.y += 0.05
        self.rect.y = self.y





