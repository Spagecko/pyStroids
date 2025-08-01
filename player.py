# in the player class
import constants
import pygame
from  circleshape import CircleShape


class Player(CircleShape):
    def __init__(self, x, y):
 
        self.rotation = 0
        super().__init__(x,y,constants.PLAYER_RADIUS)

        pass
            

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        pass 
