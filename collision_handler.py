import pygame
from events import PLAYER_COLLIDED_EVENT


class CollisionHandler:
    @classmethod
    def checkPickup(cls, player, pickup):
        if pickup != '':
            hitboxXHalf = pickup.hitbox_x / 2
            hitboxYHalf = pickup.hitbox_y / 2

            pickup_left = pickup.position.x - hitboxXHalf
            pickup_right = pickup.position.x + hitboxXHalf
            pickup_top = pickup.position.y - hitboxYHalf
            pickup_bot = pickup.position.y + hitboxYHalf

            if player.position.x < pickup_right and player.position.x > pickup_left and player.position.y < pickup_bot and player.position.y > pickup_top:
                return True

        return False

    @classmethod
    def check_collision(cls, object1, object2):
        hitbox_half_x_1 = (object1.hitbox_x / 2)
        hitbox_half_y_1 = (object1.hitbox_y / 2)
        hitbox_half_x_2 = (object2.hitbox_x / 2)
        hitbox_half_y_2 = (object2.hitbox_y / 2)

        object1_left = object1.position.x - hitbox_half_x_1
        object1_right = object1.position.x + hitbox_half_x_1
        object1_top = object1.position.y - hitbox_half_y_1
        object1_bot = object1.position.y + hitbox_half_y_1

        object2_left = object2.position.x - hitbox_half_x_2
        object2_right = object2.position.x + hitbox_half_x_2
        object2_top = object2.position.y - hitbox_half_y_2
        object2_bot = object2.position.y + hitbox_half_y_2

        if object1_left < object2_right and object1_right > object2_left and object1_top < object2_bot and object1_bot > object2_top:
            return True

        return False
