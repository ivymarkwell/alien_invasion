import sys

import pygame

from alien import Alien
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

def update_screen(ui_settings, screen, ship, aliens, bullets):
    ''' Update images on the screen and flip to the new screen '''
    # Redraw the screen during each pass through the loop
    screen.fill(ui_settings.bg_color)

    # Redraw all bullets behind ship and alien
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

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

def create_fleet(ui_settings, screen, aliens):
    ''' Create a fleet of aliens '''
    # Create an alien and find the number of aliens in a row
    # Spacing between each alien is equal to one alien width

    alien = Alien(ui_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ui_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))

    # Create the first row of aliens
    for alien_number in range(number_aliens_x):
        alien = Alien(ui_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)