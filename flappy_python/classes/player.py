from configs.settings import *


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.Surface((30, 30))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(100, SCREEN_HEIGHT / 2))
        self.mask = pg.mask.from_surface(self.image)

        self.speed = pg.math.Vector2(0)
        self.pos = pg.math.Vector2(self.rect.center)
        self.jumped = False

    def move(self, dt):
        keys = pg.key.get_pressed()

        if ((keys[pg.K_w] or keys[pg.K_SPACE]) and
                self.rect.top > 10 and
                self.speed.y > -SPEED_CAP and
                not self.jumped):
            self.speed.y += PLAYER_SPEED
            self.jumped = True
        if not (keys[pg.K_w] or keys[pg.K_SPACE]):
            self.jumped = False

        if self.speed.y < SPEED_CAP:
            self.speed.y += GRAVITY_SPEED * dt

        # Speed Cap
        if self.speed.y < -SPEED_CAP:
            self.speed.y = -SPEED_CAP
        elif self.speed.y > SPEED_CAP:
            self.speed.y = SPEED_CAP

        self.pos += self.speed * dt
        if self.pos.y < self.image.get_size()[0] / 2:
            self.pos.y = self.image.get_size()[0] / 2
            self.speed.y = 0

    def update(self, dt):
        self.move(dt)
        self.rect.center = round(self.pos)
