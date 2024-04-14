from configs.settings import *
from configs.functions import text_render
from classes.player import Player
from classes.pipe import Pipe
from time import time
from time import sleep
from random import randrange


class Main:
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode(RESOLUTION)
        self.clock = pg.time.Clock()
        pg.display.set_caption(SCREEN_NAME)
        pg.mouse.set_cursor(pg.cursors.diamond)

        self.pipes = pg.sprite.Group()
        self.player = pg.sprite.GroupSingle()

        self.show_fps: bool = False
        self.in_game: bool = False
        self.game_speed: int = 150
        self.player_score: list[float] = [0]
        self.dt: float = 0

        self.spawn_pipe = pg.USEREVENT + 2
        pg.time.set_timer(self.spawn_pipe, 375000 // self.game_speed)

        self.title_font = pg.font.Font(pg.font.get_default_font(), 68)
        self.play_button_font = pg.font.Font(pg.font.get_default_font(), 36)
        self.score_font = pg.font.Font(pg.font.get_default_font(), 24)
        self.fps_font = pg.font.Font(pg.font.get_default_font(), 18)

        self.player.add(Player())

        self.looping()

    def looping(self):
        self.play_button_timer = time()
        self.last_frame = time()
        while True:
            self.dt = time() - self.last_frame
            self.last_frame = time()

            self.events()
            self.update()
            self.render()

            pg.display.update()
            self.clock.tick(FRAMES_PER_SECOND)

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit(0)

            if event.type == pg.KEYDOWN and event.key == pg.K_INSERT:
                self.show_fps = False if self.show_fps else True

            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and not self.in_game:
                self.in_game = True

            if self.in_game:
                if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                    self.game_over()

                if event.type == self.spawn_pipe:
                    height = randrange(60 - (SCREEN_HEIGHT - 150) // 2, (SCREEN_HEIGHT - 150) // 2, 1)
                    self.pipes.add(Pipe(height))
                    self.pipes.add(Pipe((SCREEN_HEIGHT - 150) + height + 150))

    def update(self):
        if self.in_game:
            self.player.update(self.dt)
            self.pipes.update(self.player_score, self.game_speed, self.dt)

            if (self.player.sprite.rect.collideobjects(self.pipes.sprites()) or
                    self.player.sprite.pos.y > SCREEN_HEIGHT - 15):
                self.game_over()

    def render(self):
        self.screen.fill((0, 0, 0))

        if self.in_game:
            self.player.draw(self.screen)
            self.pipes.draw(self.screen)

            text_render(
                self.screen,
                self.score_font,
                f"SCORE: {self.player_score[0]:.0f}",
                True,
                (255, 255, 255),
                (SCREEN_WIDTH / 2, 25),
                relative_to=1
            )
        else:
            text_render(
                self.screen,
                self.title_font,
                "FLAPPY PYTHON",
                True,
                (255, 255, 255),
                (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150),
                relative_to=1
            )

            if time() - self.play_button_timer > 0.5:
                text_render(
                    self.screen,
                    self.play_button_font,
                    "PRESS SPACE TO PLAY",
                    True,
                    (255, 255, 0),
                    (SCREEN_WIDTH / 2, SCREEN_HEIGHT / (3 / 2)),
                    relative_to=1
                )
            if time() - self.play_button_timer > 1:
                self.play_button_timer = time()

        if self.show_fps:
            text_render(
                self.screen,
                self.fps_font,
                f"FPS: {self.clock.get_fps():.0f}",
                True,
                (255, 255, 255),
                (10, 10)
            )

    def game_over(self):
        self.player_score[0] = 0
        self.pipes.empty()
        self.player.add(Player())
        self.in_game = False
        sleep(1)


if __name__ == '__main__':
    Main()
