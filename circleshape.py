import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
	def __init__(self, x, y, radius):
		if hasattr(self, "containers"):
			super().__init__(self.containers)
		else:
			super().__init__()

		self.position = pygame.Vector2(x, y)
		self.velocity = pygame.Vector2(0, 0)
		self.radius = radius

	def draw(self, screen):
		pass

	def update(self, dt):
		pass

	def collides_with(self, player):
		# Checks for collisions by passing player object here, it still detects hits despite grazing the physical object, not sure how to correct it
		if self.position.distance_to(player.position) <= self.radius + player.radius:
			return True

	def hit_with(self, shot):
		if self.position.distance_to(shot.position) <= self.radius + shot.radius:
			return True
