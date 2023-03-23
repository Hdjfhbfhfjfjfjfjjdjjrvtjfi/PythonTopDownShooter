from pygame.sprite import AbstractGroup
from .iplayer import IPlayer


class IPlayerDecorator(IPlayer):

    def __init__(self, decorated: IPlayer, *groups: AbstractGroup):
        super(IPlayerDecorator, self).__init__(*groups)
        self._decorated: IPlayer = decorated
        self.rect = self._decorated.rect
        self.mask = self._decorated.mask
        self.image = self._decorated.image
        self.health = self._decorated.health

    def update(self, *groups: AbstractGroup) -> None:
        self._decorated.update()
        self.keys = self._decorated.keys
        self.mouse_keys = self._decorated.mouse_keys
        self.mouse_coordinates = self._decorated.mouse_coordinates

    def take_damage(self, damage: int) -> None:
        self.health -= damage
        if self.health <= 0:
            self.kill_player()

    def kill_player(self):
        self._decorated.kill()
        self.kill()
