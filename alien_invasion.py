import sys

import pygame
from pygame.sprite import Group

from alien import Alien
import game_functions as gf
from settings import Settings
from ship import Ship

def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ui_settings = Settings()
    screen = pygame.display.set_mode(
        (ui_settings.screen_width, ui_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Make a ship, a group of bullets and a group of aliens
    ship = Ship(ui_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create a fleet of aliens
    gf.create_fleet(ui_settings, screen, aliens)

    # Start the main loop for the game
    while True:
        gf.check_events(ui_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        gf.update_bullets(bullets)
        gf.update_screen(ui_settings, screen, ship, aliens, bullets)

run_game()