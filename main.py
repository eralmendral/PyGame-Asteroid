import pygame
from constants import * 
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField

def main():
	pygame.init()
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

	Clock = pygame.time.Clock()
	dt = 0

	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	asteroid = Asteroid(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 50)
	asteroidField = AsteroidField()

	updatable = [player]
	drawable = [player]
	asteroids = [asteroid]

	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
					return
		dt = Clock.tick(60) / 1000
		screen.fill((0, 0, 0))
		
		for player in drawable:
			player.draw(screen)

		for player in updatable:
			player.update(dt)

		pygame.display.flip()
	

	
if __name__ == "__main__":
	main()
