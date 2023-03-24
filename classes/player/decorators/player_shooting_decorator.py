from pygame.sprite import AbstractGroup
from pygame import K_1
from pygame.key import ScancodeWrapper

from classes.weapons.iweapon import IWeapon
from classes.player.iplayer import IPlayer
from classes.player.iplayer_decorator import IPlayerDecorator
from classes.weapons.bullets.player_bullet import PlayerBullet


class PlayerShootingDecorator(IPlayerDecorator):
    def __init__(self, decorated: IPlayer, weapons: list[IWeapon], *groups: AbstractGroup, ):
        super().__init__(decorated, *groups)
        self.bullet_cls: PlayerBullet = PlayerBullet
        self.weapons: list[IWeapon] = weapons
        self.current_weapon: IWeapon = weapons[0]

    def switch_weapon(self, keys: ScancodeWrapper):
        if keys[K_1]:
            self.current_weapon = self.weapons[0]

    def update(self, *groups: AbstractGroup) -> None:
        IPlayerDecorator.update(self, *groups)
        self.switch_weapon(self.keys)
        if self.mouse_keys[0]:
            self.current_weapon.shoot(self.rect.center, self.mouse_coordinates, *groups)
