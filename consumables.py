import pygame


class IConsumable(pygame.sprite.Sprite):

    def __init__(self, x, y, group):
        super().__init__()
        self.position = pygame.math.Vector2(x, y)
        self.image = pygame.Surface(10, 10)
        self.rect = self.image.get_rect()
        self.image.fill((255, 255, 0))
        self.add(group)

    def affection(self):
        pass

