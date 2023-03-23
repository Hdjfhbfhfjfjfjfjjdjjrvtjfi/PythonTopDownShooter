from pygame.sprite import Sprite
from pygame.math import Vector2 as Vector


class IBullet(Sprite):
    position: Vector
    direction: Vector
    damage: int
    check_collision_speed: int
    bullet_speed: int

    def update(self) -> None:
        raise NotImplementedError

    def __give_damage(self) -> None:
        raise NotImplementedError

    def __check_collides(self):
        raise NotImplementedError
