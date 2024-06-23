import pygame


ASTEROID_VARIANTS = {
    "asteroid1": {"img": pygame.image.load('Resources/Images/asteroid_1.png'),
                  "hitbox_x": 42,
                  "hitbox_y": 36},
    "asteroid2": {"img": pygame.image.load('Resources/Images/asteroid_2.png'),
                  "hitbox_x": 46,
                  "hitbox_y": 35},
    "asteroid3": {"img": pygame.image.load('Resources/Images/asteroid_3.png'),
                  "hitbox_x": 27,
                  "hitbox_y": 35},
    "asteroid4": {"img": pygame.image.load('Resources/Images/asteroid_4.png'),
                  "hitbox_x": 37,
                  "hitbox_y": 43},
    "asteroid5": {"img": pygame.image.load('Resources/Images/asteroid_5.png'),
                  "hitbox_x": 35,
                  "hitbox_y": 43}
}
