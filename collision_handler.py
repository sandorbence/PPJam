import pygame
from player import Player
from asteroid import Asteroid
from pickup import Pickup

class CollisionHandler:
    @classmethod
    def checkPlayer(cls,player, asteroids):
        for asteroid in asteroids:
            hitboxXHalf = (asteroid.hitbox_x / 2)
            hitboxYHalf = (asteroid.hitbox_y / 2)

            asteroid_left = asteroid.position.x - hitboxXHalf
            asteroid_right = asteroid.position.x + hitboxXHalf
            asteroid_top = asteroid.position.y - hitboxYHalf
            asteroid_bot = asteroid.position.y + hitboxYHalf

            if player.position.x < asteroid_right and player.position.x > asteroid_left and player.position.y < asteroid_bot and player.position.y > asteroid_top:
                # Ide kell a state change, hogy kikapott a játékos
                pygame.quit()

    def checkBlast(cls, bullet, asteroids):
        # Check if a bullet has hit an asteroid
        pass

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
        