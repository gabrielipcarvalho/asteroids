import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, 'white', self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_direction = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_asteroid_1 = self.velocity.rotate(new_direction)
            new_asteroid_2 = self.velocity.rotate(-new_direction)

            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = new_asteroid_1 * 1.2
            asteroid_2.velocity = new_asteroid_2 * 1.2
