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

    @classmethod
    def checkBlast(cls, rocket, asteroids):
        for asteroid in asteroids:
            hitboxXHalf = (asteroid.hitbox_x / 2)
            hitboxYHalf = (asteroid.hitbox_y / 2)

            asteroid_left = asteroid.position.x - hitboxXHalf
            asteroid_right = asteroid.position.x + hitboxXHalf
            asteroid_top = asteroid.position.y - hitboxYHalf
            asteroid_bot = asteroid.position.y + hitboxYHalf

            if rocket.position.x < asteroid_right and rocket.position.x > asteroid_left and rocket.position.y < asteroid_bot and rocket.position.y > asteroid_top:
               asteroids.remove(asteroid)

        return asteroids

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
        
