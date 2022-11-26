import pygame

from bullet import Bullet
from enemies import Enemy
from enemy_spawner import EnemySpawner
from environment import Border
from player import Player

#
pygame.init()

HEIGHT = 1050
WIDTH = 1680

screen = pygame.display.set_mode((WIDTH, HEIGHT), vsync=1)
pygame.display.set_caption("123")
clock = pygame.time.Clock()


player_group = pygame.sprite.Group()
environment_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()


Border(20, 1050, -20, 0, environment_group)
Border(20, 1050, 1681, 0, environment_group)
Border(1680, 20, 0, -20, environment_group)
Border(1680, 20, 0, 1051, environment_group)
enemy_spawner = EnemySpawner(Enemy)
player = Player(player_group, Bullet)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit()
    if not player_group.has(player):
        exit()
    screen.fill((0, 0, 0))
    enemy_spawner.update(enemies_group)
    environment_group.draw(screen)
    bullet_group.update((environment_group, enemies_group))
    bullet_group.draw(screen)
    enemies_group.update(player.rect.center, player_group)
    enemies_group.draw(screen)
    player_group.update(bullet_group, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    player_group.draw(screen)
    pygame.display.flip()
    clock.tick_busy_loop(60)
