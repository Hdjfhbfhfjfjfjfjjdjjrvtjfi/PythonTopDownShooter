from pygame.sprite import Sprite


class IBullet(Sprite):
    def update(self) -> None:
        raise NotImplementedError
