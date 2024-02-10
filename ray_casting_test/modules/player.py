from modules.settings import *


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

    def movement(self):
        # Cálculo do ângulo do player
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0

        # Cálculo da velocidade relativa ao ângulo
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        # Pegando as teclas pressionadas e adicionando a distância relativa
        keys = pg.key.get_pressed()
        if keys[pg.K_w] or keys[pg.K_UP]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s] or keys[pg.K_DOWN]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos

        # Fazendo o movimento se o player não colidir com uma parede
        self.move(dx, dy)

        # Pegando novamente as teclas pressionadas e adicionando a rotação relativa
        if keys[pg.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pg.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.pi * 2

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def move(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy

    def draw(self):
        # Desenhando a direção que o player está olhando
        if not SHOW_RAYS and SHOW_DIRECTION:
            pg.draw.line(self.game.screen,
                         PLAYER_COLOR,
                         (self.x * self.game.tile_size, self.y * self.game.tile_size),
                         (self.x * self.game.tile_size + (self.game.tile_size / 2) * math.cos(self.angle),
                          self.y * self.game.tile_size + (self.game.tile_size / 2) * math.sin(self.angle)), 1)

        # Desenhando o corpo do player
        pg.draw.circle(self.game.screen,
                       PLAYER_COLOR,
                       (self.x * self.game.tile_size, self.y * self.game.tile_size),
                       15, 1)

    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)
