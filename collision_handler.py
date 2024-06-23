import pygame
from events import PLAYER_COLLIDED_EVENT


class CollisionHandler:
    @classmethod
    def check_player_collision(cls, player, asteroid):
        collided = check_collision(player, asteroid)

        if collided:
            pygame.event.post(pygame.event.Event(PLAYER_COLLIDED_EVENT, {
                'message': 'Player collided.'}))

    @classmethod
    def check_blast(cls, rocket, asteroid):
        return check_collision(rocket, asteroid)

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


def check_collision(object1, object2):
    hitboxXHalf = (object2.hitbox_x / 2)
    hitboxYHalf = (object2.hitbox_y / 2)

    object2_left = object2.position.x - hitboxXHalf
    object2_right = object2.position.x + hitboxXHalf
    object2_top = object2.position.y - hitboxYHalf
    object2_bot = object2.position.y + hitboxYHalf

    if object1.position.x < object2_right and object1.position.x > object2_left and object1.position.y < object2_bot and object1.position.y > object2_top:
        return True

    return False
