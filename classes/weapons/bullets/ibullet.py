from pygame.sprite import Sprite
from pygame.math import Vector2 as Vector
from pygame.sprite import AbstractGroup
from pygame import Surface, Rect, Mask


class IBullet(Sprite):
    image: Surface
    rect: Rect
    mask: Mask
    position: Vector
    direction: Vector
    damage: int
    check_collision_speed: Vector
    bullet_speed: int

    def update(self, group: AbstractGroup) -> None:
        raise NotImplementedError

    def move(self, group: AbstractGroup) -> None:
        raise NotImplementedError

    def check_collides(self, group: AbstractGroup) -> None:
        raise NotImplementedError
