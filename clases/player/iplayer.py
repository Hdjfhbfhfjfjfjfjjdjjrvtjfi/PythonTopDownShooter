from pygame.sprite import Sprite, AbstractGroup


class IPlayer(Sprite):

    def update(self) -> None:
        raise NotImplementedError



