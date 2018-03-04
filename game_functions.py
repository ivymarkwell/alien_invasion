import sys

import pygame

from bullet import Bullet

def check_events(ui_settings, screen, ship, bullets):
    ''' Respond to kepresses and mouse events '''
    # Watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ui_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ui_settings, screen, ship, alien, bullets):
    ''' Update images on the screen and flip to the new screen '''
    # Redraw the screen during each pass through the loop
    screen.fill(ui_settings.bg_color)

    # Redraw all bullets behind ship and alien
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    alien.blitme()

    # Make the most recently drawn screen visibile
    pygame.display.flip()

def check_keydown_events(event, ui_settings, screen, ship, bullets):
    ''' Respond to keypresses '''
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        # Move the ship to the left
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group
        fire_bullet(ui_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    ''' Respond to key releases '''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_bullets(bullets):
    # Get rid of bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def fire_bullet(ui_settings, screen, ship, bullets):
    ''' Fire a bullet if limit not reached yet '''
    if len(bullets) < ui_settings.bullets_allowed:
        new_bullet = Bullet(ui_settings, screen, ship)
        bullets.add(new_bullet)