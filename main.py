import pygame
from player import Player
from environment import Border
from bullet import Bullet
from enemies import Enemy

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
Enemy(enemies_group, (1000, 1000))
Enemy(enemies_group, (900, 900))
player = Player(player_group)


while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or\
                (not player_group.has(player)):
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            Bullet(player.rect.centerx, player.rect.centery, pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], bullet_group)
    screen.fill((0, 0, 0))
    environment_group.draw(screen)
    bullet_group.update((environment_group, enemies_group))
    bullet_group.draw(screen)
    enemies_group.update(player.rect.center, player_group)
    enemies_group.draw(screen)
    player_group.update()
    player_group.draw(screen)
    pygame.display.flip()
    clock.tick_busy_loop(60)
