import pygame
import time


class Bullet(pygame.sprite.Sprite):
    SPEED = 20

    def __init__(self, x, y, mouse_x, mouse_y, group):
        pygame.sprite.Sprite.__init__(self)
        self.position = pygame.math.Vector2(x, y)
        self.speed = pygame.math.Vector2(mouse_x - x, mouse_y - y).normalize()
        self.speed.scale_to_length(self.SPEED)
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.add(group)

    def update(self, group):
        self.movement(group)

    def movement(self, group):
        for _ in range(self.SPEED):
            self.position += self.speed
            self.rect.center = self.position
            try:
                self.collide(group)
            except StopIteration:
                break

    def collide(self, group):
        collides = (pygame.sprite.spritecollideany(sprite=self, group=group[0], collided=pygame.sprite.collide_rect),
                    pygame.sprite.spritecollideany(sprite=self, group=group[1], collided=pygame.sprite.collide_rect))
        if collides[0] is not None:
            self.kill()
        if collides[1] is not None:
            self.kill()
            collides[1].kill()
            raise StopIteration
