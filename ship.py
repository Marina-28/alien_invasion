import pygame

class Ship():
	"""Class for controlling ship."""
	def __init__(self, ai_game):
		"""Initializes the ship and sets its initial position."""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		
		# Loads an image of the ship and gets a rectangle.
		self.image = pygame.image.load('images/ship_.bmp')
		self.rect = self.image.get_rect()

		# Each new ship appears at the bottom of the screen
		self.rect.midbottom = self.screen_rect.midbottom

		self.moving_right = False
		self.moving_left = False

		
	def blitme(self):
		"""Draw the ship in its current position."""
		self.screen.blit(self.image, self.rect)
	def update(self):
		"""Updates ship's position."""
		if self.moving_right:
			self.rect.x += 1
		if self.moving_left:
			self.rect.x -= 1

