import random

import pygame
import abc


class IEnemy(pygame.sprite.Sprite):
    __metaclass__ = abc.ABCMeta

    @property
    def SPEED(self):
        pass

    @abc.abstractmethod
    def __init__(self, group, start_coord, consumable_cls):
        super().__init__()
        self.consumables = consumable_cls
        self.health = 30
        self.image = pygame.Surface((20, 20))
        self.direction = pygame.math.Vector2((0, 0))
        self.position = pygame.math.Vector2(start_coord)
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.add(group)

    @abc.abstractmethod
    def update(self, player_coord, group):
        self.movement(player_coord, group)

    @abc.abstractmethod
    def movement(self, player_coord, group):
        self.direction = pygame.math.Vector2(player_coord[0] - self.position[0],
                                             player_coord[1] - self.position[1]).normalize()
        for _ in range(self.SPEED):
            self.position += self.direction
            self.rect.center = self.position
            self.collide(group)

    @abc.abstractmethod
    def collide(self, group):
        collides = pygame.sprite.spritecollideany(sprite=self, group=group[0], collided=pygame.sprite.collide_rect)
        if collides is not None:
            collides.kill()

    @abc.abstractmethod
    def take_damage(self, damage, group):
        self.health -= damage
        if self.health <= 0:
            self.kill()
            # self.spawn_consumable(group)

    @abc.abstractmethod
    def spawn_consumable(self, group):
        self.consumables[random.randint(0, len(self.consumables))](self.rect.centerx, self.rect.centery, group)



class WalkingEnemy(IEnemy, abc.ABC):
    SPEED = 3


class ShootingEnemy(IEnemy, abc.ABC):
    SPEED = 1

    def __init__(self, group, start_coord, bullet_cls, consumable_cls):
        super().__init__(group, start_coord, consumable_cls)
        self.bullet = bullet_cls
        self.shoot_cooldown = 120

    def update(self, player_coord, group):
        self.strike(group, player_coord)
        super().update(player_coord, group[0])

    def strike(self, group, player_coord):
        if self.shoot_cooldown == 0:
            self.bullet(self.rect.centerx, self.rect.centery, player_coord[0], player_coord[1], group[1], 50)
            self.shoot_cooldown = 120
        else:
            self.shoot_cooldown -= 1
