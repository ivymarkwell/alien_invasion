import sys

import pygame

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

    # Make a ship
    ship = Ship(screen)

    # Start the main loop for the game
    while True:
        gf.check_events()
        gf.update_screen(ui_settings, screen, ship)

run_game()