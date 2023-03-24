from pygame.sprite import AbstractGroup
from .bullets.player_bullet import PlayerBullet


class IWeapon:
    damage: int
    shoot_cooldown: int
    check_collision_speed: int
    speed: int
    cooldown: int
    capacity: int
    max_capacity: int
    reload_cooldown: int
    bullet_cls: PlayerBullet

    @classmethod
    def shoot(cls, coordinates: tuple[int, int], target_coordinates: tuple[int, int], *groups: AbstractGroup) -> None:
        raise NotImplementedError
