import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField
from shot import Shot

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()

	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	# This creates a list of objects that are later used to iterate through
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	asteroidField = AsteroidField()

	Player.containers = (updatable, drawable)

	Shot.containers = (shots, updatable, drawable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	dt = 0

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		for obj in updatable:
			obj.update(dt)

		for asteroid in asteroids:
			if asteroid.collides_with(player):
				print("Game Over!")
				sys.exit()

			for shot in shots:
				if asteroid.hit_with(shot):
					pygame.sprite.Sprite.kill(asteroid)
					pygame.sprite.Sprite.kill(shot)

		screen.fill("black")
		
		for obj in drawable:
			obj.draw(screen)
		
		pygame.display.flip()

		# limit frames to 60fps
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()
