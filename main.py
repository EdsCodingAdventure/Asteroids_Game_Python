import pygame
from constants import *
from player import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    #---For capping the game at 60 FPS
    clock = pygame.time.Clock()
    dt = 0 #delta time
    #---

    #---Game Loop: To keep the game open
    i = 1
    while i == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        #---limiting the game to 60 FPS
        dt = clock.tick(60) / 1000
        #---
        
        player.update(dt)
        player.draw(screen)

        pygame.display.flip()


    #---
    
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)


if __name__ == "__main__":
    main()

