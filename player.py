import pygame
from pygame.math import Vector2


class Player(pygame.sprite.Sprite):
    WALK_SPEED = 3
    RUN_SPEED = 6

    def __init__(self, group, cls):
        pygame.sprite.Sprite.__init__(self)
        self.position = Vector2(200, 200)
        self.image = pygame.Surface((20, 20))
        self.image.fill((100, 100, 100))
        self.rect = self.image.get_rect()
        self.bullet_class = cls
        self.add(group)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT]:
            self.movement(keys, self.RUN_SPEED)
        elif not keys[pygame.K_LSHIFT]:
            self.movement(keys, self.WALK_SPEED)
        self.rect.center = self.position

    def movement(self, keys, move_mode):
        if keys[pygame.K_w]:
            self.position = self.position + Vector2(0, -move_mode)
        if keys[pygame.K_s]:
            self.position = self.position + Vector2(0, move_mode)
        if keys[pygame.K_a]:
            self.position = self.position + Vector2(-move_mode, 0)
        if keys[pygame.K_d]:
            self.position = self.position + Vector2(move_mode, 0)
        if self.position[0] > 1670:
            self.position[0] = 1670
        elif self.position[0] < 10:
            self.position[0] = 10
        if self.position[1] > 1040:
            self.position[1] = 1040
        elif self.position[1] < 10:
            self.position[1] = 10
