import pygame
import random

from asteroid import Asteroid
from constants import *
from asteroid_variants import *


class AsteroidFactory:
    @classmethod
    def create(cls):
        y_coord = random.randint(0, SCREEN_HEIGHT)
        position = pygame.Vector2(SCREEN_WIDTH, y_coord)

        variant_key = ""
        variant_index = random.randint(0,len(ASTEROID_VARIANTS))
        for index, key in enumerate(ASTEROID_VARIANTS):
            if index == variant_index:
                variant_key = key            

        if variant_key == "":
            variant_key = "asteroid5"

        variant = ASTEROID_VARIANTS[variant_key]

        original_width, original_height = variant["img"].get_size()
        aspect_ratio = original_width / original_height
        
        new_height = random.randint(ASTEROID_MIN_HEIGHT, ASTEROID_MAX_HEIGHT)
        new_width = new_height * aspect_ratio

        height_multiplier = new_height / original_height
        width_multiplier = new_width / original_width

        variant["hitbox_x"] = variant["hitbox_x"] * width_multiplier
        variant["hitbox_y"] = variant["hitbox_y"] * height_multiplier
        
        variant["img"] = pygame.transform.scale(variant["img"], (new_width, new_height))

        return Asteroid(variant["img"], position, variant["hitbox_x"], variant["hitbox_y"])
