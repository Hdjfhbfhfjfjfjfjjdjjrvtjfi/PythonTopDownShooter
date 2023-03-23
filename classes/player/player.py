import pygame.key as key
import pygame.mouse as mouse
from pygame import Surface, Mask, Rect
from pygame.key import ScancodeWrapper
from pygame.sprite import AbstractGroup
from consts import PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_HEALTH
from .iplayer import IPlayer



class Player(IPlayer):
    def __init__(self, *groups: AbstractGroup):
        super(Player, self).__init__(*groups)
        self.image: Surface = Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect: Rect = self.image.get_rect()
        self.mask: Mask = self.image.get_masks()
        self.keys: ScancodeWrapper = None
        self.mouse_keys: tuple[bool, bool, bool] = None
        self.health = PLAYER_HEALTH

    def update(self) -> None:
        self.keys = key.get_pressed()
        self.mouse_keys = mouse.get_pressed()

    def take_damage(self, damage: int) -> None:
        self.health -= damage
        if self.health <= 0:
            self.kill_player()

    def kill_player(self):
        self.kill()

