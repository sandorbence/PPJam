import pygame

# ASTEROID_VARIANTS = [
#     pygame.image.load('Resources/Meteors/Meteor_01.png'),
#     pygame.image.load('Resources/Meteors/Meteor_02.png'),
#     pygame.image.load('Resources/Meteors/Meteor_03.png'),
#     pygame.image.load('Resources/Meteors/Meteor_04.png'),
#     pygame.image.load('Resources/Meteors/Meteor_05.png'),
#     pygame.image.load('Resources/Meteors/Meteor_06.png'),
#     pygame.image.load('Resources/Meteors/Meteor_07.png'),
#     pygame.image.load('Resources/Meteors/Meteor_08.png'),
#     pygame.image.load('Resources/Meteors/Meteor_09.png'),
#     pygame.image.load('Resources/Meteors/Meteor_10.png')
#     pygame.image.load('Resources/Meteors/asteroid_1.png'), #42 36
#     pygame.image.load('Resources/Meteors/asteroid_2.png'), #46 35
#     pygame.image.load('Resources/Meteors/asteroid_3.png'), #27 35
#     pygame.image.load('Resources/Meteors/asteroid_4.png'), #37 43
#     pygame.image.load('Resources/Meteors/asteroid_5.png')  #35 43
#     ]

ASTEROID_VARIANTS = {
    "asteroid1" : {"img" : pygame.image.load('Resources/Meteors/asteroid_1.png'),
                   "hitbox_x" : 42,
                   "hitbox_y" : 36},
    "asteroid2" : {"img" : pygame.image.load('Resources/Meteors/asteroid_2.png'),
                   "hitbox_x" : 46,
                   "hitbox_y" : 35},
    "asteroid3" : {"img" : pygame.image.load('Resources/Meteors/asteroid_3.png'),
                   "hitbox_x" : 27,
                   "hitbox_y" : 35},
    "asteroid4" : {"img" : pygame.image.load('Resources/Meteors/asteroid_4.png'),
                   "hitbox_x" : 37,
                   "hitbox_y" : 43},
    "asteroid5" : {"img" : pygame.image.load('Resources/Meteors/asteroid_5.png'),
                   "hitbox_x" : 35,
                   "hitbox_y" : 43}
}
