import pygame
import random
import constants
from  circleshape import CircleShape

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  
    

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        pass

    def update(self, dt):
        self.position += self.velocity * dt
        pass

    def split(self):
        self.kill()
        if(self.radius <= constants.ASTEROID_MIN_RADIUS):
            pass
        else:
            randomAngle = random.uniform(20,50)
            randomAngle2 = random.uniform(20,50) * -1
            velcVect1 = self.velocity.rotate(randomAngle)
            velcVect2 = self.velocity.rotate(randomAngle2)
            newRadius = self.radius - constants.ASTEROID_MIN_RADIUS

            #create astroid objects 
            rock1 = Asteroid(self.position.x, self.position.y, newRadius)
            rock2 = Asteroid(self.position.x, self.position.y, newRadius)
            rock1.velocity = velcVect1 * 1.2
            rock2.velocity = velcVect2 * 1.2
            #draw astroids

