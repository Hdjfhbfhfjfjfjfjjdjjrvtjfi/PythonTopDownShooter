import pygame
import abc


class IBullet(pygame.sprite.Sprite):
    __metaclass__ = abc.ABCMeta

    @property
    def SPEED(self):
        pass

    @abc.abstractmethod
    def __init__(self, x, y, mouse_x, mouse_y, group, damage):
        super().__init__()
        self.damage = damage
        self.position = pygame.math.Vector2(x, y)
        self.speed = pygame.math.Vector2(mouse_x - x, mouse_y - y)
        self.speed.scale_to_length(4)
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.add(group)

    @abc.abstractmethod
    def update(self, group):
        self.movement(group)

    @abc.abstractmethod
    def movement(self, group):
        for _ in range(self.SPEED):
            self.position += self.speed
            self.rect.center = self.position
            try:
                self.collide(group)
            except StopIteration:
                break

    @abc.abstractmethod
    def collide(self, group):
        collides = []
        for i in range(len(group)):
            collides.append(pygame.sprite.spritecollideany(sprite=self, group=group[i],
                                                           collided=pygame.sprite.collide_rect))
        for i in range(len(collides)):
            if collides[i] is not None:
                try:
                    collides[i].take_damage(self.damage)
                except AttributeError:
                    pass
                self.kill()
                raise StopIteration


class Bullet(IBullet, abc.ABC):
    SPEED = 100


class EnemyBullet(IBullet, abc.ABC):
    SPEED = 10

    def __init__(self, x, y, player_x, player_y, group, damage):
        super().__init__(x, y, player_x, player_y, group, damage)
        self.speed.scale_to_length(2)
