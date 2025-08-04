# in the player class
import constants
import pygame
from  circleshape import CircleShape


class Shot(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, constants.SHOT_RADIUS, 2)
        pass

    def update(self, dt):
        self.position += self.velocity * dt
        pass  

