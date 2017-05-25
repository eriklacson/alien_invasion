import pygame

from pygame.sprite import Group


#import settings class
from settings import Settings

#import ship class
from ship import Ship

#import game_functions class
import game_functions as gf



def run_game():
	# Initialize game and create a screen object.
	pygame.init()

	ai_settings = Settings()

	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# Make a ship.
	ship = Ship(ai_settings, screen)

	# Make an alien.
	aliens = Group()

	# Make a group to store bullets in.
	bullets = Group()

	# Create the fleet of aliens.
	gf.create_fleet(ai_settings, screen, ship, aliens)

	# Start the main loop for the game.
	while True:

		# Watch for keyboard and mouse events.
		gf.check_events(ai_settings, screen, ship, bullets)

		# Redraw the screen during each pass through the loop.
		ship.update()

		#update bullets status
		gf.update_bullets(ai_settings, screen, ship, aliens, bullets)

		#update aliens position
		gf.update_aliens(ai_settings, aliens)

		#redraw screen
		gf.update_screen(ai_settings, screen, aliens, ship, bullets)

run_game()