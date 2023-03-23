from pygame.sprite import AbstractGroup
from .player import Player
from consts import PLAYER_HEALTH


class IPlayerDecorator(Player):
    def __init__(self, decorated: Player, *groups: AbstractGroup):
        super(IPlayerDecorator, self).__init__(*groups)
        self._decorated: Player = decorated
        self.health = PLAYER_HEALTH

    def update(self) -> None:
        self._decorated.update()
        self.keys = self._decorated.keys
        self.mouse_keys = self._decorated.mouse_keys

    def take_damage(self, damage: int) -> None:
        self.health -= damage
        if self.health <= 0:
            self.kill_player()

    def kill_player(self):
        self._decorated.kill_player()
        self.kill()

