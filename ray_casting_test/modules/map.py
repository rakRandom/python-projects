from modules.settings import *


class Map:
    def __init__(self, game, tile_size) -> None:
        self.game = game
        self.mini_map = BOOL_MAP
        self.world_map = {}
        self.tile_size = tile_size
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self) -> None:
        [pg.draw.rect(self.game.screen,
                      WALL_COLOR,
                      (pos[0] * self.tile_size, pos[1] * self.tile_size, self.tile_size, self.tile_size), 1)
         for pos in self.world_map]
