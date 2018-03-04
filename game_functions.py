import sys

import pygame

def check_events():
    ''' Respond to kepresses and mouse events '''
    # Watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ui_settings, screen, ship):
    ''' Update images on the screen and flip to the new screen '''
    # Redraw the screen during each pass through the loop
    screen.fill(ui_settings.bg_color)
    ship.blitme()
    
    # Make the most recently drawn screen visibile
    pygame.display.flip()