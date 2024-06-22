import pygame
from player import Player
from asteroid import Asteroid

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

            print("LINE: ",asteroid.hitbox_x, asteroid.hitbox_y, asteroid_left, asteroid_right, asteroid_top, asteroid_bot)
            print("player position: ", player.position.x, player.position.y)
            if player.position.x < asteroid_right and player.position.x > asteroid_left and player.position.y < asteroid_bot and player.position.y > asteroid_top:
                # Ide kell a state change, hogy kikapott a játékos
                pygame.quit()

    def checkBlast(cls, bullet, asteroids):
        # Check if a bullet has hit an asteroid
        pass

    def checkPickup(cls, player, pickup):
        # Check if the player has picked up an item
        pass 
        