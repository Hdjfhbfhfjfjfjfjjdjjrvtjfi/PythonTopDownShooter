import pygame

from bullet import Bullet, EnemyBullet
from enemies import WalkingEnemy, ShootingEnemy
from enemy_spawner import EnemySpawner
from environment import Border
from player import Player
from consumables import IConsumable


pygame.init()

HEIGHT = 1050
WIDTH = 1680

screen = pygame.display.set_mode((WIDTH, HEIGHT), vsync=1)
pygame.display.set_caption("123")
clock = pygame.time.Clock()


player_group = pygame.sprite.Group()
environment_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
walking_enemies_group = pygame.sprite.Group()
shooting_enemies_group = pygame.sprite.Group()
consumable_group = pygame.sprite.Group()

Border(20, 1050, -20, 0, environment_group)
Border(20, 1050, 1681, 0, environment_group)
Border(1680, 20, 0, -20, environment_group)
Border(1680, 20, 0, 1051, environment_group)
enemy_spawner = EnemySpawner((WalkingEnemy, ShootingEnemy), EnemyBullet, (IConsumable, ))
player = Player(player_group, Bullet)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit()
    if not player_group.has(player):
        exit()
    screen.fill((0, 0, 0))
    enemy_spawner.update(walking_enemies_group, shooting_enemies_group)
    environment_group.draw(screen)
    bullet_group.update((environment_group, walking_enemies_group, shooting_enemies_group))
    bullet_group.draw(screen)
    enemy_bullet_group.update((environment_group, player_group))
    enemy_bullet_group.draw(screen)
    walking_enemies_group.update(player.rect.center, player_group)
    walking_enemies_group.draw(screen)
    shooting_enemies_group.update(player.rect.center, (player_group, enemy_bullet_group))
    shooting_enemies_group.draw(screen)
    player_group.update(bullet_group, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    player_group.draw(screen)
    pygame.display.flip()
    clock.tick_busy_loop(60)
