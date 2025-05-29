# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys


# import the connect_database function
# and the database_version variable
# from database.py into the current file
# from database import connect_database, database_version

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot




def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.groups = (updatable, drawable)
    Asteroid.groups = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.groups = (shots, updatable, drawable)

    asteroidfield = AsteroidField()
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    
    while (pygame.get_init()):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit(0)

        screen.fill(background_color_value)
        
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

        dt = (clock.tick(60)/1000)




if __name__ == "__main__":
    main()