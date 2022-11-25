import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill()
        self.rect = self.image.get_rect()
        self.add(group)
