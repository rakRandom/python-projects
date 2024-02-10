from modules.settings import *


class RayCasting:
    def __init__(self, game):
        self.game = game

    def ray_cast(self):
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        ray_angle = self.game.player.angle - HALF_FOV + 0.0001
        for _ in range(NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # Raios horizontais
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

            depth_hor = (y_hor - oy) / sin_a
            x_hor = ox + depth_hor * cos_a

            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for _ in range(MAX_DEPTH):
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map.world_map:
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth

            # Raios verticais
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

            depth_vert = (x_vert - ox) / cos_a
            y_vert = oy + depth_vert * sin_a

            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for _ in range(MAX_DEPTH):
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map.world_map:
                    if ONLY_DRAW_IN_FOV:
                        pg.draw.rect(self.game.screen,
                                     WALL_COLOR,
                                     (tile_vert[0] * self.game.tile_size, tile_vert[1] * self.game.tile_size,
                                      self.game.tile_size, self.game.tile_size),
                                     1)
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            if depth_vert < depth_hor:
                depth = depth_vert
            else:
                depth = depth_hor

            # Mostrando os raios criados
            if SHOW_RAYS:
                pg.draw.line(self.game.screen,
                             RAY_COLOR,
                             (self.game.tile_size * ox, self.game.tile_size * oy),
                             (self.game.tile_size * ox + self.game.tile_size * depth * cos_a,
                              self.game.tile_size * oy + self.game.tile_size * depth * sin_a), 1)

            ray_angle += DELTA_ANGLE

    def update(self):
        self.ray_cast()
