from .ibullet import IBullet
from pygame import Surface, Rect, Mask
from pygame.sprite import AbstractGroup, spritecollideany, collide_rect
from pygame.math import Vector2 as Vector
from consts import BULLET_WIDTH, BULLET_HEIGHT


class PlayersBullet(IBullet):
    def __init__(self, x: int, y: int, target_x: int, target_y: int,  speed: int, damage: int, *groups: AbstractGroup):
        super(PlayersBullet, self).__init__(groups)
        self.position: Vector = Vector(x, y)
        self.image: Surface = Surface(BULLET_WIDTH, BULLET_HEIGHT)
        self.rect: Rect = self.image.get_rect()
        self.mask: Mask = self.image.get_masks()
        self.speed: int = speed
        self.damage: int = damage
        self.direction: Vector = Vector(target_x-x, target_y-y)
        self.image.fill((255, 255, 255))

    def update(self) -> None:
        pass

    def fly(self) -> None:
        self.position += self.direction
        self.rect.center = self.position

    def give_damage(self, group: AbstractGroup) -> None:
        collide = []
        for elem in group:
            collide.append(spritecollideany(self, elem, collided=collide_rect))
        for elem in collide:
            if elem is not None:
                try:
                    pass
                except Exception:
                    pass



