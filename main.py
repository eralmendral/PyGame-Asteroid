import pygame
import sys
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
	pygame.init()
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	Clock = pygame.time.Clock()
	dt = 0
	


	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()	

	Player.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)

	asteroid = Asteroid(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 50)
	asteroidField = AsteroidField()

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
					return
		dt = Clock.tick(60) / 1000
		screen.fill("black")

		updatable.update(dt)

		updatable.update(dt)

		for asteroid in asteroids:
				if asteroid.collides_with(player):
					print("Game over!")
					sys.exit()	

		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()
	

	
if __name__ == "__main__":
	main()
