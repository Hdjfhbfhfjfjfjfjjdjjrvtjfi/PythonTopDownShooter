from .ibullet import IBullet
from ...player.player import Player
from ...border import Border
from pygame.sprite import AbstractGroup, spritecollideany, collide_rect, Sprite, spritecollide, groupcollide, collide_mask
from pygame.math import Vector2 as Vector
from pygame import Surface


class PlayerBullet(IBullet):
    def __init__(self, coordinates: tuple[int, int], target_coordinates: tuple[int, int], damage: int,
                 check_collision_speed: int, bullet_speed: int, *groups: AbstractGroup):
        super().__init__(*groups)
        self.image = Surface((3, 3))
        self.rect = self.image.get_rect()
        self.mask = self.image.get_masks()
        self.position = Vector(coordinates[0], coordinates[1])
        self.direction = Vector(target_coordinates[0] - coordinates[0], target_coordinates[1] - coordinates[1])
        self.damage = damage
        self.check_collision_speed = self.direction
        self.check_collision_speed.scale_to_length(check_collision_speed)
        self.bullet_speed = bullet_speed
        self.image.fill((255, 255, 255))

    def update(self, *groups: AbstractGroup) -> None:
        self.move(*groups)

    def move(self, *groups: AbstractGroup) -> None:
        for _ in range(self.bullet_speed):
            self.position = self.position + self.check_collision_speed
            self.rect.center = self.position
            try:
                self.check_collides(*groups)
            except StopIteration:
                pass
    """Изменить класс объекта"""
    def check_collides(self, *groups: AbstractGroup) -> None:
        for group in list(iter(groups)):
            collided = spritecollideany(self, group, collide_rect)
            if spritecollideany(self, group, collide_rect) is not None:
                # if isinstance(collided, Player):
                #     collided.take_damage(self.damage)
                #     self.kill()
                #     raise StopIteration
                if isinstance(collided, Border):
                    self.kill()
                    raise StopIteration
