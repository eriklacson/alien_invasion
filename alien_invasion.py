import pygame


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

	# Start the main loop for the game.

	while True:

		# Watch for keyboard and mouse events.
		gf.check_events(ship)
		# Redraw the screen during each pass through the loop.
		gf.update_screen(ai_settings, screen, ship)

run_game()