from hashlib import new
import imp
import sys

import pygame

from settings import Settings

from ship import Ship

from bullet import Bullet

from alien import Alien

class AlienInvasion:
	"""Class to control game resources and behavior."""
	
	def __init__(self):
		"""Initialize of game and creating game resources."""
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		
		pygame.display.set_caption("Alien Invasion")
		
		self.bg_color = (self.settings.bg_color)
		self.ship = Ship(self)

		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()

	def run_game(self):
		"""Start the main game cycle."""
		while True:
			# Keyboard and mouse event tracking.
			self._check_events()
			self.ship.update()
			self._update_bullets()
			self._update_screen()
	
	def _check_events(self):
		"""Handles keystrokes and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		"""Responds to key presses."""
		if event.key == pygame.K_RIGHT:
			# Move the ship to the right/left
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_ESCAPE:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		"""Respond to key release."""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _update_screen(self):
		"""Updates the images on the screen and displays a new screen."""
		# Fill the screen with a specific color
		self.screen.fill(self.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)
		# Displays the last screen drawn.
		pygame.display.flip()
	
	def _fire_bullet(self):
		"""Creating a new bullet and adding its in group."""
		if (len(self.bullets) < self.settings.bullets_allowed):
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)
	
	def _remove_bullets(self):
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
	
	def _update_bullets(self):
		self.bullets.update()
		self._remove_bullets()

	def _create_fleet(self):
		"""Creates fleet of aliens."""
		alien = Alien(self)
		alien_width = alien.rect.width
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)

		# Creating the first row of aliens.
		for alien_number in range(number_aliens_x):
			self._create_alien(alien_number)
	
	def _create_alien(self, alien_number):
		"""Creates the alien and append it in row."""
		alien = Alien(self)
		alien_width = alien.rect.width
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		self.aliens.add(alien)


if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()



