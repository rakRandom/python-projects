from modules.settings import *
from modules.gui_elements import Button, Label


class Language:
    def __init__(self, game):
        self.game = game

        self.title_label = Label(self.game, LANGUAGE_TITLE_POS, TITLE_FONT, LANGUAGE_TITLE_ENG_TEXT, True, self.game.color2)
        self.back_btn = Button(self.game, BACKB_POS, BUTTON1_FONT, BACKB_TEXT, self.game.color2, self.game.color1)
        self.ptbr_btn = Button(self.game, PTBRB_POS, BUTTON1_FONT, PTBRB_ENG_TEXT, self.game.color2, self.game.color1)
        self.eng_btn = Button(self.game, ENGB_POS, BUTTON1_FONT, ENGB_ENG_TEXT, self.game.color2, self.game.color1)
        self.fra_btn = Button(self.game, FRAB_POS, BUTTON1_FONT, FRAB_ENG_TEXT, self.game.color2, self.game.color1)

    def update(self):
        # Hover effect
        if self.back_btn.is_hovered():
            self.back_btn.border = self.game.color2
        else:
            self.back_btn.border = None
        if self.ptbr_btn.is_hovered():
            self.ptbr_btn.border = self.game.color2
        else:
            self.ptbr_btn.border = None
        if self.eng_btn.is_hovered():
            self.eng_btn.border = self.game.color2
        else:
            self.eng_btn.border = None
        if self.fra_btn.is_hovered():
            self.fra_btn.border = self.game.color2
        else:
            self.fra_btn.border = None

        # Going back to clock
        if self.back_btn.is_touched():
            self.game.current_level -= 1

        # Changing language
        if self.ptbr_btn.is_touched():
            # PT-BR
            self.title_label.update(LANGUAGE_TITLE_POS, TITLE_FONT, LANGUAGE_TITLE_PTBR_TEXT, True, self.game.color2)
            self.ptbr_btn.update_text(PTBRB_PTBR_TEXT)
            self.eng_btn.update_text(ENGB_PTBR_TEXT)
            self.fra_btn.update_text(FRAB_PTBR_TEXT)

            # Main
            pg.display.set_caption(WINDOW_PTBR_CAPTION)
            self.game.theme_btn.update_text(THEMEB_PTBR_TEXT)
            self.game.mute_btn.update_text(MUTEB_PTBR_TEXT)
            self.game.lang_btn.update_text(LANGB_PTBR_TEXT)

            # DClock
            self.game.levels[0].title_label.update(DCLOCK_TITLE_POS, TITLE_FONT, DCLOCK_TITLE_PTBR_TEXT, True, self.game.color2)

            self.game.levels[0].week_days = DCLOCK_PTBR_WEEK_DAYS
            self.game.levels[0].months = DCLOCK_PTBR_MONTHS

            self.game.levels[0].get_date()

            if self.game.play_sound:
                self.game.click_sound.play()

        if self.eng_btn.is_touched():
            # English
            self.title_label.update(LANGUAGE_TITLE_POS, TITLE_FONT, LANGUAGE_TITLE_ENG_TEXT, True, self.game.color2)
            self.ptbr_btn.update_text(PTBRB_ENG_TEXT)
            self.eng_btn.update_text(ENGB_ENG_TEXT)
            self.fra_btn.update_text(FRAB_ENG_TEXT)

            # Main
            pg.display.set_caption(WINDOW_ENG_CAPTION)
            self.game.theme_btn.update_text(THEMEB_ENG_TEXT)
            self.game.mute_btn.update_text(MUTEB_ENG_TEXT)
            self.game.lang_btn.update_text(LANGB_ENG_TEXT)

            # DClock
            self.game.levels[0].title_label.update(DCLOCK_TITLE_POS, TITLE_FONT, DCLOCK_TITLE_ENG_TEXT, True, self.game.color2)

            self.game.levels[0].week_days = DCLOCK_ENG_WEEK_DAYS
            self.game.levels[0].months = DCLOCK_ENG_MONTHS

            self.game.levels[0].get_date()

            if self.game.play_sound:
                self.game.click_sound.play()

        if self.fra_btn.is_touched():
            # French
            self.title_label.update(LANGUAGE_TITLE_POS, TITLE_FONT, LANGUAGE_TITLE_FRA_TEXT, True, self.game.color2)
            self.ptbr_btn.update_text(PTBRB_FRA_TEXT)
            self.eng_btn.update_text(ENGB_FRA_TEXT)
            self.fra_btn.update_text(FRAB_FRA_TEXT)

            # Main
            pg.display.set_caption(WINDOW_FRA_CAPTION)
            self.game.theme_btn.update_text(THEMEB_FRA_TEXT)
            self.game.mute_btn.update_text(MUTEB_FRA_TEXT)
            self.game.lang_btn.update_text(LANGB_FRA_TEXT)

            # DClock
            self.game.levels[0].title_label.update(DCLOCK_TITLE_POS, TITLE_FONT, DCLOCK_TITLE_FRA_TEXT, True, self.game.color2)

            self.game.levels[0].week_days = DCLOCK_FRA_WEEK_DAYS
            self.game.levels[0].months = DCLOCK_FRA_MONTHS

            self.game.levels[0].get_date()

            if self.game.play_sound:
                self.game.click_sound.play()

    def draw(self):
        self.title_label.draw()
        self.back_btn.draw()
        self.ptbr_btn.draw()
        self.eng_btn.draw()
        self.fra_btn.draw()
