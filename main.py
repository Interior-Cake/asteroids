import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill((0,0,0))

        for object in drawable:
            object.draw(screen)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()

        pygame.display.flip()

        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
