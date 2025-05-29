# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame


# import the connect_database function
# and the database_version variable
# from database.py into the current file
# from database import connect_database, database_version

from constants import *




def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while (pygame.get_init()):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(pygame.Color(color_value))
        pygame.display.flip()




if __name__ == "__main__":
    main()