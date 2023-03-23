from pygame.key import ScancodeWrapper
from pygame import K_w, K_s, K_a, K_d
from pygame.sprite import AbstractGroup
from pygame.math import Vector2 as Vector
from .player import Player
from clases.player.iplayer_decorator import IPlayerDecorator
from consts import PLAYER_SPEED, PLAYER_HEALTH


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

    def update(self) -> None:
        IPlayerDecorator.update(self)
        self.movement(self.keys)


class PlayerShootingDecorator(IPlayerDecorator):
    def __init__(self, decorated: Player, *groups: AbstractGroup):
        super().__init__(decorated, *groups)

    def shoot(self, keys: tuple[bool, bool, bool]) -> None:
        if keys[0]:
            print(2)

    def update(self) -> None:
        IPlayerDecorator.update(self)
        self.shoot(self.mouse_keys)
