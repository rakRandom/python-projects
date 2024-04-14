from configs.settings import *


class Pipe(pg.sprite.Sprite):
    def __init__(self, y_pos: float):
        super().__init__()

        self.image = pg.Surface((60, SCREEN_HEIGHT - 150))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH + 60, y_pos))
        self.mask = pg.mask.from_surface(self.image)

        self.pos = pg.math.Vector2(self.rect.center)

    def move(self, score, speed, dt):
        self.pos.x -= speed * dt
        if self.pos.x < -30:
            score[0] += 0.5
            self.kill()

    def update(self, score, speed, dt):
        self.move(score, speed, dt)
        self.rect.center = round(self.pos)
