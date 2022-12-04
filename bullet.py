import pygame


class Bullet(pygame.sprite.Sprite):
    SPEED = 100

    def __init__(self, x, y, mouse_x, mouse_y, group, damage):
        pygame.sprite.Sprite.__init__(self)
        self.damage = damage
        self.position = pygame.math.Vector2(x, y)
        self.speed = pygame.math.Vector2(mouse_x - x, mouse_y - y)
        self.speed.scale_to_length(4)
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.add(group)

    def update(self, group):
        self.movement(group)

    def movement(self, group):
        for _ in range(self.SPEED):
            self.position += self.speed
            self.rect.center = self.position
            try:
                self.collide(group)
            except StopIteration:
                break

    def collide(self, group):
        collides = (pygame.sprite.spritecollideany(sprite=self, group=group[0], collided=pygame.sprite.collide_rect),
                    pygame.sprite.spritecollideany(sprite=self, group=group[1], collided=pygame.sprite.collide_rect),
                    pygame.sprite.spritecollideany(sprite=self, group=group[2], collided=pygame.sprite.collide_rect),)
        for i in range(0, 3):
            if collides[i] is not None:
                try:
                    collides[i].take_damage(self.damage)
                except(AttributeError):
                    pass
                self.kill()
                raise StopIteration




class EnemyBullet(Bullet):
    SPEED = 10

    def __init__(self, x, y, player_x, player_y, group, damage):
        Bullet.__init__(self, x, y, player_x, player_y, group, damage)
        self.speed.scale_to_length(1)
