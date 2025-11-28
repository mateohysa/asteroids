import constants
from circleshape import CircleShape
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rand = random.uniform(20, 50)
            rot1 = self.velocity.rotate(rand)
            rot2 = self.velocity.rotate(-rand)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            ast1 = Asteroid(self.position.x, self.position.y, new_radius)
            ast2 = Asteroid(self.position.x, self.position.y, new_radius)
            
            ast1.velocity = rot1 * 1.2
            ast2.velocity = rot2 * 1.2
            
            
            