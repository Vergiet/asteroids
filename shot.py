from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.velocity = pygame.Vector2(0, 1)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, player_color_value, self.position, self.radius, 2)


    def update(self, dt):
        self.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.position += self.velocity * dt

    def rotate(self, rotation):
        self.rotation += rotation