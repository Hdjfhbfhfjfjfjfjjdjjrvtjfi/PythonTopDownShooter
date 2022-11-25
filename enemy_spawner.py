import pygame


class EnemySpawner:
    def __init__(self, cls):
        self.time = 0
        self.enemy_class = cls

    def update(self, group):
        self.time += 1
        if self.time == 60:
            self.enemy_class(group, (1000, 1000))
            self.enemy_class(group, (500, 1000))
            self.enemy_class(group, (600, 700))
            self.enemy_class(group, (1680, 500))
            self.enemy_class(group, (900, 900))
            self.time = 0

