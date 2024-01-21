import pygame.font
from gun import Gun
from pygame.sprite import Group

class Scores():
    """Game scores & info"""
    def __init__(self, screen, stats):
        """Initializing game stats counter"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (10, 255, 10)
        self.font = pygame.font.SysFont(None, 32)
        self.image_score()
        self.image_high_score()
        # self.image_guns()

    """
    def image_guns(self):
        # Number of lives
        for gun_number in range(self.stats.gun_hp):
            gun = Gun(self.screen)
            gun.rect.x = 15 + gun_number * gun.rect.width
            gun.rect.y = 20
            self.guns.add(gun)
    """

    def image_high_score(self):
        self.high_score_image = self.font.render("Highest is:"+str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 40
        self.high_score_rect.top = 40

    def image_score(self):
        """Make text into image"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def show_score(self):
        """Print scores on screen"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        # self.guns.draw(self.screen)
