import pygame
import constants 
from  player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

import sys

ONE_MILISECOND = 1000

def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers= (updatable,)
    Shot.containers= (shots,updatable,drawable)

    player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        for ast in asteroids:
            if(player.collisionCheck(ast)):
                sys.exit("Game over!")
            for shot in shots:
                if(shot.collisionCheck(ast)):
                    ast.split()

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
    
       

        


if __name__ == "__main__":
    main()
