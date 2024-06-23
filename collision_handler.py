import pygame
from events import PLAYER_COLLIDED_EVENT


class CollisionHandler:
    @classmethod
    def checkPlayer(cls, player, asteroids):
        for asteroid in asteroids:
            hitboxXHalf = (asteroid.hitbox_x / 2)
            hitboxYHalf = (asteroid.hitbox_y / 2)

            asteroid_left = asteroid.position.x - hitboxXHalf
            asteroid_right = asteroid.position.x + hitboxXHalf
            asteroid_top = asteroid.position.y - hitboxYHalf
            asteroid_bot = asteroid.position.y + hitboxYHalf

            if player.position.x < asteroid_right and player.position.x > asteroid_left and player.position.y < asteroid_bot and player.position.y > asteroid_top:
                pygame.event.post(pygame.event.Event(PLAYER_COLLIDED_EVENT, {
                                  'message': 'Player collided.'}))

    def checkBlast(cls, bullet, asteroids):
        # Check if a bullet has hit an asteroid
        pass

    def checkPickup(cls, player, pickup):
        # Check if the player has picked up an item
        pass
