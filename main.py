import pygame
from classes.border import Border
from classes.player.player_builder import PlayerBuilder
from classes.player.player import Player


pygame.init()

HEIGHT = 1050
WIDTH = 1680

screen = pygame.display.set_mode((WIDTH, HEIGHT), vsync=1)
pygame.display.set_caption("123")
clock = pygame.time.Clock()


environment_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
player_builder = PlayerBuilder(Player(player_group))
player = player_builder.add_shooting().add_movement(40, 40).create_player()


Border(20, 1050, -20, 0, environment_group)
Border(20, 1050, 1681, 0, environment_group)
Border(1680, 20, 0, -20, environment_group)
Border(1680, 20, 0, 1051, environment_group)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit()
        if player not in player_group:
            exit()
    screen.fill((0, 0, 0))
    player_group.update()
    player_group.draw(screen)
    pygame.display.flip()
    clock.tick(60)

    # if not player_group.has(player):
    #     exit()
    # screen.fill((0, 0, 0))
    # enemy_spawner.update(walking_enemies_group, shooting_enemies_group)
    # environment_group.draw(screen)
    # bullet_group.update((environment_group, walking_enemies_group, shooting_enemies_group))
    # bullet_group.draw(screen)
    # enemy_bullet_group.update((environment_group, player_group))
    # enemy_bullet_group.draw(screen)
    # walking_enemies_group.update(player.rect.center, player_group)
    # walking_enemies_group.draw(screen)
    # shooting_enemies_group.update(player.rect.center, (player_group, enemy_bullet_group))
    # shooting_enemies_group.draw(screen)
    # player_group.update(bullet_group, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    # player_group.draw(screen)
    # pygame.display.flip()
    # clock.tick_busy_loop(60)
