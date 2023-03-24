from pygame.sprite import AbstractGroup
from .iweapon import IWeapon
from consts import PISTOL_CAPACITY, PISTOL_DAMAGE, PISTOL_SHOOT_COOLDOWN, PISTOL_RELOAD_COOLDOWN, PLAYER_BULLET_SPEED, \
    PLAYER_BULLET_CHECK_COLLISION_SPEED
from .bullets.player_bullet import PlayerBullet


class Pistol(IWeapon):
    damage = PISTOL_DAMAGE
    shoot_cooldown = PISTOL_SHOOT_COOLDOWN
    cooldown = 0
    check_collision_speed = PLAYER_BULLET_CHECK_COLLISION_SPEED
    speed = PLAYER_BULLET_SPEED
    capacity = PISTOL_CAPACITY
    max_capacity = PISTOL_CAPACITY
    reload_cooldown = PISTOL_RELOAD_COOLDOWN
    bullet_cls = PlayerBullet

    @classmethod
    def shoot(cls, coordinates: tuple[int, int], target_coordinates: tuple[int, int], *groups: AbstractGroup) -> None:
        if cls.cooldown == 0:
            cls.bullet_cls(coordinates, target_coordinates, cls.damage, cls.check_collision_speed, cls.speed, *groups)
            cls.capacity -= 1
            if cls.capacity == 0:
                cls.cooldown = cls.reload_cooldown
                cls.capacity = PISTOL_CAPACITY
            else:
                cls.cooldown = cls.shoot_cooldown
        else:
            cls.cooldown -= 1
