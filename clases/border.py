import pygame


class Border(pygame.sprite.Sprite):
    def __init__(self, size_x, size_y, x, y, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.image.fill((255, 255, 255))
        self.add(group)
