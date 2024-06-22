import pygame
import random

from asteroid import Asteroid
from constants import *
from asteroid_variants import *


class AsteroidFactory:
    @classmethod
    def create(cls):
        y_coord = random.randint(0, SCREEN_HEIGHT)
        position = (SCREEN_WIDTH, y_coord)

        variant = ASTEROID_VARIANTS[random.randint(
            0, len(ASTEROID_VARIANTS)-1)]

        original_width, original_height = variant.get_size()
        aspect_ratio = original_width / original_height
        
        new_height = random.randint(ASTEROID_MIN_HEIGHT, ASTEROID_MAX_HEIGHT)
        new_width = new_height * aspect_ratio
        
        variant = pygame.transform.scale(variant, (new_width, new_height))

        return Asteroid(variant, position)
