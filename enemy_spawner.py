class EnemySpawner:
    def __init__(self, enemy_cls, bullet_cls):
        self.time = 0
        self.walking_enemy_class = enemy_cls[0]
        self.shooting_enemy_class = enemy_cls[1]
        self.bullet_cls = bullet_cls

    def update(self, walking_enemy, shooting_enemy):
        self.time += 1
        if self.time == 60:
            self.shooting_enemy_class(shooting_enemy, (1000, 1000), self.bullet_cls)
            self.walking_enemy_class(walking_enemy, (500, 1000))
            self.walking_enemy_class(walking_enemy, (600, 700))
            self.walking_enemy_class(walking_enemy, (1680, 500))
            self.walking_enemy_class(walking_enemy, (900, 900))
            self.time = 0

