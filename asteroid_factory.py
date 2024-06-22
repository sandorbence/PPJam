import pygame
import random

from asteroid import Asteroid
from constants import *

variant1_image = pygame.image.load('Resources/Meteors/Meteor_02.png')
variant1_image = pygame.transform.scale(
    variant1_image, (ASTEROID_V1_WIDTH, ASTEROID_V1_HEIGHT))


class AsteroidFactory:
    @classmethod
    def create(cls, variant):
        y_coord = random.randint(0, SCREEN_HEIGHT)
        position = (SCREEN_WIDTH, y_coord)

        return Asteroid(variant1_image, position)
