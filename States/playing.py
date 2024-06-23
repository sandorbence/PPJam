import copy
import pygame
import random

from States.game_state import GameState
from pickup import Pickup
from player import Player
from asteroid_factory import AsteroidFactory
from constants import *
from collision_handler import CollisionHandler
from rocket import Rocket
from score import Score
from events import PLAYER_COLLIDED_EVENT


class Playing(GameState):
    def __init__(self, screen):
        self.screen = screen
        self.bg_image = pygame.image.load('Resources/Images/background.png')
        self.bg_image = pygame.transform.scale(
            self.bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        player_pos = pygame.Vector2(
            screen.get_width() / 2, screen.get_height() / 2)

        self.player = Player(player_pos)

        self.player_sprite_group = pygame.sprite.Group()
        self.player_sprite_group.add(self.player)

        self.asteroid_sprite_group = pygame.sprite.Group()
        self.asteroid_group = []
        self.asteroid_counter = 0
        self.next_asteroid = random.randrange(
            ASTEROID_MIN_SPAWN_TIME, ASTEROID_MAX_SPAWN_TIME) / 100

        self.i = 0

        self.pickup_counter = 0
        self.pickup = None
        self.rocket = None
        self.next_pickup = random.randrange(
            PICKUP_MIN_SPAWN_TIME, PICKUP_MAX_SPAWN_TIME) / 100

        self.rocket_sprite_group = pygame.sprite.Group()
        self.pickup_sprite_group = pygame.sprite.Group()

        self.score = Score(self.screen)

        self.pickup_sound = pygame.mixer.Sound('Resources/Sounds/pickup.wav')
        self.pickup_sound.set_volume(0.5)
        self.game_over_sound = pygame.mixer.Sound(
            'Resources/Sounds/game_over.wav')
        self.game_over_sound.set_volume(0.2)
        self.hit_sound = pygame.mixer.Sound('Resources/Sounds/hit.wav')
        self.hit_sound.set_volume(0.5)
        self.shoot_sound = pygame.mixer.Sound('Resources/Sounds/shoot.wav')
        self.shoot_sound.set_volume(0.5)

        self.pace_counter = 0
        self.pace = 1.0

    def handle_events(self, events):
        return super().handle_events()

    def update(self, dt):
        self.pace_counter += dt

        if self.pace_counter >= GETTING_HARDER:
            self.pace += 0.1
            self.pace_counter = 0

        if self.i <= -SCREEN_WIDTH:
            self.i = 0
        self.i -= BACKGROUND_MOVE_SPEED

        self.player_sprite_group.update(dt)

        self.asteroid_counter += dt

        if self.asteroid_counter >= self.next_asteroid:
            asteroid = AsteroidFactory.create(self.pace)
            self.asteroid_sprite_group.add(asteroid)
            self.asteroid_group.append(asteroid)
            self.next_asteroid = random.randrange(
                ASTEROID_MIN_SPAWN_TIME, ASTEROID_MAX_SPAWN_TIME) / (100*self.pace)
            self.asteroid_counter = 0

        self.pickup_counter += dt

        if self.pickup_counter >= self.next_pickup and not self.player.hasRocket:
            y_coord = random.randint(0, SCREEN_HEIGHT)
            position = pygame.Vector2(SCREEN_WIDTH, y_coord)
            self.pickup = Pickup(position, self.pace)
            self.pickup_sprite_group.add(self.pickup)
            self.pickup_counter = 0

        for asteroid in self.asteroid_group:
            # Remove asteroid if it left the screen
            if asteroid.rect.right < 0:
                self.asteroid_group.remove(asteroid)
                self.asteroid_sprite_group.remove(asteroid)

            collided = CollisionHandler.check_collision(self.player, asteroid)
            if collided:
                self.game_over_sound.play()
                pygame.event.post(pygame.event.Event(PLAYER_COLLIDED_EVENT, {
                    'message': f'{self.score.value}'}))
                break

        if self.pickup != None:
            pickupCollision = CollisionHandler.check_collision(
                self.player, self.pickup)

            if pickupCollision:
                self.pickup_sound.play()
                self.player.hasRocket = True
                self.pickup_sprite_group.empty()
                self.pickup = None

        if self.player.hasRocket:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.shoot_sound.play()
                self.rocket = Rocket(
                    copy.copy(self.player.position), self.pace)
                self.rocket_sprite_group.add(self.rocket)
                self.player.hasRocket = False

        if self.rocket != None:
            for asteroid in self.asteroid_group:
                blasted = CollisionHandler.check_collision(
                    self.rocket, asteroid)
                if blasted:
                    self.hit_sound.play()
                    self.asteroid_group.remove(asteroid)
                    self.asteroid_sprite_group.remove(asteroid)
                    self.score.add_asteroid_score()
                    self.rocket_sprite_group.empty()
                    self.rocket = None
                    break

        # Remove rocket if it collided with no asteroid and left the screen
        for rocket in self.rocket_sprite_group:
            if rocket.rect.left > SCREEN_WIDTH:
                self.rocket_sprite_group.remove(rocket)

        # Remove pickup if it left the screen
        for pickup in self.pickup_sprite_group:
            if pickup.rect.right < 0:
                self.pickup_sprite_group.remove(pickup)

        self.asteroid_sprite_group.update(dt)
        self.pickup_sprite_group.update(dt)
        self.rocket_sprite_group.update(dt)
        self.score.update(dt)

    def render(self):
        self.screen.blit(self.bg_image, (self.i, 0))
        self.screen.blit(self.bg_image, (SCREEN_WIDTH+self.i, 0))
        self.player_sprite_group.draw(self.screen)
        self.asteroid_sprite_group.draw(self.screen)
        self.pickup_sprite_group.draw(self.screen)
        self.rocket_sprite_group.draw(self.screen)
        self.score.render()
