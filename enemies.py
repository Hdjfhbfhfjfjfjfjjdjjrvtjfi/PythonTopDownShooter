import pygame


class Enemy(pygame.sprite.Sprite):
    SPEED = 3

    def __init__(self, group, start_coord):
        pygame.sprite.Sprite.__init__(self)
        self.magazine = (10, 30, 5)
        self.health = 30
        self.image = pygame.Surface((20, 20))
        self.direction = pygame.math.Vector2((0, 0))
        self.position = pygame.math.Vector2(start_coord)
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.add(group)

    def update(self, player_coord, group):
        self.movement(player_coord, group)

    def movement(self, player_coord, group):
        self.direction = pygame.math.Vector2(player_coord[0]-self.position[0], player_coord[1]-self.position[1]).normalize()
        for _ in range(self.SPEED):
            self.position += self.direction
            self.rect.center = self.position
            self.collide(group)

    def collide(self, group):
        collides = pygame.sprite.spritecollideany(sprite=self, group=group, collided=pygame.sprite.collide_rect)
        if collides is not None:
            collides.kill()

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.kill()
