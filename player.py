# in the player class
import constants
import pygame
from  circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
 
        self.rotation = 0
        self.playerShootCD =  constants.PLAYER_SHOOT_COOLDOWN
        self.shoot_timer = 0
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

    def rotate (self, dt):
        self.rotation = self.rotation + constants.PLAYER_TURN_SPEED * dt
        pass

    def update(self, dt):
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            reverseDt = dt * -1
            self.rotate(reverseDt) 
            # ?
        if keys[pygame.K_d]:
            self.rotate(dt)
            # ?
        if(keys[pygame.K_w]):
            self.move(dt)
        
        if(keys[pygame.K_s]):
            reverseDt = dt * -1
            self.move(reverseDt)
        
        if(keys[pygame.K_SPACE]):
            
            self.shoot()

    def move(self, dt):
        
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt
        
        pass

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = constants.PLAYER_SHOOT_COOLDOWN
    
        bullet = Shot(self.position.x, self.position.y, self.radius)
        
        pyVector = pygame.Vector2(0, 1)
        
        pyVector.rotate_ip(self.rotation)  # This modifies pyVector directly
        bullet.velocity = pyVector * constants.PLAYER_SHOOT_SPEED


        pass

