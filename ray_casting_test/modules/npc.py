from modules.settings import *


class NPC:
    def __init__(self, game):
        self.game = game
        self.x, self.y = randint(2, MAP_SIZE_X - 2), randint(2, MAP_SIZE_Y - 2)
        self.angle = PLAYER_ANGLE

    def movement(self):
        # Cálculo do ângulo do NPC
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0

        # Cálculo da velocidade relativa ao ângulo
        speed = PLAYER_SPEED * self.game.delta_time / 2
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        # Pegando uma direção aleatória
        direction = randint(0, 4)
        if self.game.player.pos[0] > self.x:
            dx += speed_cos
            dy += speed_sin
        if self.game.player.pos[0] < self.x:
            dx += -speed_cos
            dy += -speed_sin
        if self.game.player.pos[1] > self.y:
            dx += -speed_sin
            dy += speed_cos
        if self.game.player.pos[1] < self.y:
            dx += speed_sin
            dy += -speed_cos

        # Fazendo o movimento se o player não colidir com uma parede
        self.move(dx, dy)

        # Pegando novamente as teclas pressionadas e adicionando a rotação relativa
        # if keys[pg.K_LEFT]:
        #     self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        # if keys[pg.K_RIGHT]:
        #     self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        # self.angle %= math.pi * 2

    def get_path(self, nx, ny, px, py):
        path = [(px, py)]

        if nx == px and ny == py:
            return []

        for i in range(MAP_SIZE_Y * MAP_SIZE_X):
            pass

        return path if path[-1] == (nx, ny) else []

    def check_wall(self, x, y):
        return (x, y) not in self.game.map.world_map

    def move(self, dx, dy):
        if self.check_wall(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy)):
            self.y += dy

    def draw(self):
        # Desenhando o corpo do NPC
        pg.draw.circle(self.game.screen,
                       NPC_COLOR,
                       (self.x * self.game.tile_size, self.y * self.game.tile_size),
                       15, 1)

    def update(self):
        self.movement()
