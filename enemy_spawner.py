class EnemySpawner:
    def __init__(self, enemy_cls, bullet_cls):
        self.time = 0
        self.walking_enemy_class = enemy_cls[0]
        self.shooting_enemy_class = enemy_cls[1]
        self.bullet_cls = bullet_cls

