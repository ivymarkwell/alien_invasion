import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    ''' A class to manage bullets fired from the ship '''

    def __init__(self, ui_settings, screen, ship):
        ''' Create a bullet object at the ship's current '''
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0,0) and then set current position
        self.rect = pygame.Rect(0, 0, ui_settings.bullet_width, ui_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = ui_settings.bullet_color
        self.speed_factor = ui_settings.bullet_speed_factor