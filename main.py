import sys
import pygame
from pygame.time import Clock
from pygame.version import PygameVersion
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
time = pygame.time.Clock()
dt = 0


while(True):
    
    log_state()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  
    screen.fill("black")
    player.draw(screen)
    pygame.display.flip()
    player.update(dt)
    dt = time.tick(60)/1000
    



def main():
    print(f"Starting Asteroids with pygame version {PygameVersion}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    


if __name__ == "__main__":
    main()
