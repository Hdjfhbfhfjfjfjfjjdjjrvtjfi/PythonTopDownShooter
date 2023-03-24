import pygame.key as key
import pygame.mouse as mouse
from pygame import Surface
from pygame.sprite import AbstractGroup
from consts import PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_HEALTH
from .iplayer import IPlayer


class Player(IPlayer):
    def __init__(self, *groups: AbstractGroup):
        super(Player, self).__init__(*groups)
        self.image = Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.rect = self.image.get_rect()
        self.mask = self.image.get_masks()
        self.health = PLAYER_HEALTH

    def update(self, groups: list[AbstractGroup]) -> None:
        self.keys = key.get_pressed()
        self.mouse_keys = mouse.get_pressed()
        self.mouse_coordinates = mouse.get_pos()

    def kill(self) -> None:
        self.remove(self.groups())

    def take_damage(self, damage):
        self.health -= damage
        print(self.health)
        if self.health <= 0:
            self.kill()

