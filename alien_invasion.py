import sys

import pygame
from pygame.sprite import Group

from alien import Alien
from button import Button
import game_functions as gf
from game_stats import GameStats
from settings import Settings
from ship import Ship
from scoreboard import Scoreboard

def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ui_settings = Settings()
    screen = pygame.display.set_mode(
        (ui_settings.screen_width, ui_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Make the play button
    play_button = Button(ui_settings, screen, "Play")

    # Create an instance to store game stats and create a scoreboard
    stats = GameStats(ui_settings)
    sb = Scoreboard(ui_settings, screen, stats)

    # Make a ship, a group of bullets and a group of aliens
    ship = Ship(ui_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create a fleet of aliens
    gf.create_fleet(ui_settings, screen, ship, aliens)

    # Start the main loop for the game
    while True:
        gf.check_events(ui_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            bullets.update()

            gf.update_bullets(ui_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ui_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ui_settings, screen, ship, stats, sb, aliens, bullets, play_button)

run_game()