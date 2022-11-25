import pygame


class Enemy(pygame.sprite.Sprite):
    SPEED = 3

    def __init__(self, group, start_coord):
        pygame.sprite.Sprite.__init__(self, group)
        self.image = pygame.Surface((20, 20))
        self.direction = pygame.math.Vector2((0, 0))
        self.position = pygame.math.Vector2(start_coord)
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()

    def update(self, player_coord):
        self.movement(player_coord)

    def movement(self, player_coord):
        self.direction = pygame.math.Vector2((player_coord[0] - self.position[0], player_coord[1] - self.position[1]))
        self.direction.scale_to_length(self.SPEED)
        self.position += self.direction
        self.rect.center = self.position
