import sys

import pygame

def check_events(ship):
    ''' Respond to kepresses and mouse events '''
    # Watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right
                ship.moving_right = True

            elif event.key == pygame.K_LEFT:
                # Move the ship to the left
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False

            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(ui_settings, screen, ship):
    ''' Update images on the screen and flip to the new screen '''
    # Redraw the screen during each pass through the loop
    screen.fill(ui_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visibile
    pygame.display.flip()