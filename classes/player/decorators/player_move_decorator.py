from pygame import Vector2 as Vector, K_w, K_s, K_a, K_d, K_LSHIFT
from pygame.key import ScancodeWrapper
from pygame.sprite import AbstractGroup
from classes.player.iplayer import IPlayer
from classes.player.iplayer_decorator import IPlayerDecorator
from consts import PLAYER_SPEED


class PlayerMoveDecorator(IPlayerDecorator):
    def __init__(self, decorated: IPlayer, *groups: AbstractGroup, x: int, y: int):
        super().__init__(decorated, *groups)
        self.position: Vector = Vector(x, y)
        self.direction: Vector = (0, 0)
        self.image.fill((100, 100, 100))

    def movement(self, keys: ScancodeWrapper) -> None:
        self.direction = Vector(0, 0)
        if keys[K_w]:
            self.direction += Vector(0, -1 * PLAYER_SPEED)
        if keys[K_s]:
            self.direction += Vector(0, PLAYER_SPEED)
        if keys[K_a]:
            self.direction += Vector(-1 * PLAYER_SPEED, 0)
        if keys[K_d]:
            self.direction += Vector(PLAYER_SPEED, 0)
        if keys[K_LSHIFT] and self.direction.length() != 0:
            self.direction.scale_to_length(PLAYER_SPEED * 2)
        self.position += self.direction
        if self.position[0] > 1670:
            self.position[0] = 1670
        elif self.position[0] < 10:
            self.position[0] = 10
        if self.position[1] > 1040:
            self.position[1] = 1040
        elif self.position[1] < 10:
            self.position[1] = 10
        self.rect.center = self.position

    def update(self, *groups: AbstractGroup) -> None:
        IPlayerDecorator.update(self, *groups)
        self.movement(self.keys)
