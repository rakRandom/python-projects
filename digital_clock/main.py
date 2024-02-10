from modules.settings import *
from modules import gui_elements, dclock, language


class Main:
    def __init__(self):
        pg.init()

        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        pg.display.set_caption(WINDOW_ENG_CAPTION)
        pg.display.set_icon(pg.image.load("assets/images/clock.png").convert_alpha())

        # Variables
        self.show_fps = False
        self.unlock_fps = False
        self.play_sound = True
        self.theme = False  # False = Light Theme - True = Dark Theme
        self.current_level = 0
        self.color1 = WHITE
        self.color2 = BLACK

        self.levels = []
        self.levels.append(dclock.DClock(self))
        self.levels.append(language.Language(self))

        # GUI elements
        self.theme_btn = gui_elements.Button(self, THEMEB_POS, BUTTON1_FONT, THEMEB_ENG_TEXT, self.color2, self.color1, self.color2)
        self.mute_btn = gui_elements.Button(self, MUTEB_POS, BUTTON2_FONT, MUTEB_ENG_TEXT, self.color2, self.color1, orientation=1)
        self.lang_btn = gui_elements.Button(self, LANGB_POS, BUTTON2_FONT, LANGB_ENG_TEXT, self.color2, self.color1, orientation=2)

        # Events
        self.update_hour = pg.USEREVENT + 3
        self.update_date = pg.USEREVENT + 4

        pg.time.set_timer(self.update_hour, 100)
        pg.time.set_timer(self.update_date, 5000)

        # Sound
        self.click_sound = pg.mixer.Sound("assets/audios/click-sound.mp3")

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

            if event.type == self.update_hour:
                self.levels[0].get_hour()  # Get hour

            if event.type == self.update_date:
                self.levels[0].get_date()  # Get date

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_INSERT:
                    self.show_fps = False if self.show_fps else True
                if event.key == pg.K_k:
                    self.unlock_fps = False if self.unlock_fps else True
                if event.key == pg.K_m:
                    # Mute or desmute (pressing the key)
                    self.play_sound = False if self.play_sound else True
                if event.key == pg.K_l:
                    # Change to language selection or digital clock (pressing the key)
                    self.current_level = 0 if self.current_level else 1

    def update(self):
        self.levels[self.current_level].update()

        # Set cursor
        if self.theme_btn.is_hovered():
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
        elif self.mute_btn.is_hovered():
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
        elif self.lang_btn.is_hovered():
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
        else:
            pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)

        # Change theme
        if self.theme_btn.is_touched():
            if self.play_sound:
                self.click_sound.play()

            # Changing the colors
            if self.theme:
                self.color1 = WHITE
                self.color2 = BLACK
                self.theme = False
            else:
                self.color1 = BLACK
                self.color2 = WHITE
                self.theme = True

            # Updating the theme
            self.levels[0].title_label.update_color(self.color2, self.color1)
            self.levels[0].hour_label.update_color(self.color2, self.color1)
            self.levels[0].date_label.update_color(self.color2, self.color1)

            self.levels[1].title_label.update_color(self.color2, self.color1)
            self.levels[1].back_btn.update_color(self.color2, self.color1)
            self.levels[1].ptbr_btn.update_color(self.color2, self.color1)
            self.levels[1].eng_btn.update_color(self.color2, self.color1)
            self.levels[1].fra_btn.update_color(self.color2, self.color1)

            self.theme_btn.update(THEMEB_POS, BUTTON1_FONT, self.theme_btn.text, self.color2, self.color1, self.color2)
            self.mute_btn.update(MUTEB_POS, BUTTON2_FONT, self.mute_btn.text, self.color2, self.color1)
            self.lang_btn.update(LANGB_POS, BUTTON2_FONT, self.lang_btn.text, self.color2, self.color1)

        # Mute or desmute (clicking the button)
        if self.mute_btn.is_touched():
            self.play_sound = False if self.play_sound else True
        # Change to language selection or digital clock (clicking the button)
        if self.lang_btn.is_touched():
            self.current_level = 0 if self.current_level else 1

        if self.unlock_fps:
            self.clock.tick(0)
        else:
            self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(self.color1)

        # Writing the texts in the screen
        self.levels[self.current_level].draw()
        self.theme_btn.draw()
        self.mute_btn.draw()
        self.lang_btn.draw()

        if self.show_fps:
            self.screen.blit(FONT.render(f"{self.clock.get_fps():.1f}", False, self.color2), (0, 0))

        pg.display.update()

    def run(self):
        while True:
            self.event_handler()
            self.update()
            self.draw()
