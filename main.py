import sys
import pygame
from pygame.version import PygameVersion
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

while(True):
    log_state()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  
    screen.fill("black")
    pygame.display.flip()



def main():
    print(f"Starting Asteroids with pygame version {PygameVersion}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
