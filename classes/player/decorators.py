from pygame.key import ScancodeWrapper
from pygame import K_w, K_s, K_a, K_d
from pygame.sprite import AbstractGroup
from pygame.math import Vector2 as Vector
from .player import Player
from .iplayer_decorator import IPlayerDecorator
from consts import PLAYER_SPEED
from ..weapons.bullets.player_bullet import PlayerBullet


class PlayerMoveDecorator(IPlayerDecorator):
    def __init__(self, decorated: Player, *groups: AbstractGroup, x: int, y: int):
        super().__init__(decorated, *groups)
        self.position: Vector = Vector(x, y)
        self.speed: int = PLAYER_SPEED
        self.image.fill((100, 100, 100))

    def movement(self, keys: ScancodeWrapper) -> None:
        if keys[K_w]:
            self.position = Vector(self.position.x, self.position.y - self.speed)
        if keys[K_s]:
            self.position = Vector(self.position.x, self.position.y + self.speed)
        if keys[K_a]:
            self.position = Vector(self.position.x - self.speed, self.position.y)
        if keys[K_d]:
            self.position = Vector(self.position.x + self.speed, self.position.y)
        self.rect.center = self.position

    def update(self, *groups: AbstractGroup) -> None:
        IPlayerDecorator.update(self)
        self.movement(self.keys)


class PlayerShootingDecorator(IPlayerDecorator):
    def __init__(self, decorated: Player, *groups: AbstractGroup):
        super().__init__(decorated, *groups)
        self.bullet_cls: PlayerBullet = PlayerBullet

    def shoot(self, keys: tuple[bool, bool, bool], groups) -> None:
        if keys[0]:
            self.bullet_cls((self.rect.x, self.rect.y), self.mouse_coordinates, 1, 10, 50, groups)

    def update(self, *groups: AbstractGroup) -> None:
        IPlayerDecorator.update(self)
        self.shoot(self.mouse_keys, groups)
