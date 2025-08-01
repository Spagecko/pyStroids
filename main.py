import pygame
import constants
from  player import Player

ONE_MILISECOND = 1000

def main():
    print('Starting Asteroids!')
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    gameClock = pygame.time.Clock()
    dt = 0 #delta time

    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT ))
    playerXpoint = constants.SCREEN_WIDTH / 2
    playerYpoint= constants.SCREEN_HEIGHT / 2
    mainPlayer = Player(playerXpoint, playerYpoint)
    mainPlayerTriangle = mainPlayer.triangle()
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        mainPlayer.draw(screen)
        pygame.display.flip()
        
        
        timeValue = gameClock.tick()
        dt = timeValue / ONE_MILISECOND

        


if __name__ == "__main__":
    main()
