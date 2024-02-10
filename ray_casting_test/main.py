from modules.settings import *
from modules import *
from debug import Debug
import sys


class Main:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Ray Casting")

        self.screen = pg.display.set_mode(RESOLUTION)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.tile_size = WIDTH / MAP_SIZE_X

        self.map = map.Map(self, self.tile_size)
        self.npc = npc.NPC(self)
        self.player = player.Player(self)
        self.ray_casting = raycasting.RayCasting(self)
        self.debug = Debug(self.screen)

    def update(self):
        self.npc.update()
        self.player.update()
        self.ray_casting.update()
        pg.display.update()
        self.delta_time = self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.npc.draw()
        self.player.draw()

        if not ONLY_DRAW_IN_FOV:
            self.map.draw()
        if SHOW_FPS:
            self.debug.show(f"FPS: {self.clock.get_fps():.1f}")

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_p:
                    print(f"{self.player.pos}\n{self.player.map_pos}\n")

    def run(self):
        while True:
            self.event_handler()
            self.update()
            self.draw()
