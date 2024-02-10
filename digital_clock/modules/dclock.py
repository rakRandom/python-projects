from modules.settings import *
from modules.gui_elements import Label


class DClock:
    def __init__(self, game):
        self.game = game

        self.week_days = DCLOCK_ENG_WEEK_DAYS
        self.months = DCLOCK_ENG_MONTHS

        # Texts
        self.title_label = Label(self.game, DCLOCK_TITLE_POS, TITLE_FONT, DCLOCK_TITLE_ENG_TEXT, True, self.game.color2)
        self.get_hour()
        self.get_date()

    def get_hour(self):
        l_time = time.localtime()

        self.hour_label = Label(self.game,
                                HOURL_POS,
                                HOUR_FONT,
                                f"{l_time.tm_hour} : {l_time.tm_min} : {l_time.tm_sec}",
                                True,
                                self.game.color2)

    def get_date(self):
        l_time = time.localtime()
        week_day = self.week_days[l_time.tm_wday]
        month = self.months[l_time.tm_mon - 1]

        self.date_label = Label(self.game,
                                DATEL_POS,
                                DATE_FONT,
                                f"{week_day} - {l_time.tm_mday} / {month} / {l_time.tm_year}",
                                True,
                                self.game.color2)

    def update(self):
        pass

    def draw(self):
        # Writing the texts in the screen
        self.title_label.draw()  # Title
        self.hour_label.draw()  # Hour/Minute/Second
        self.date_label.draw()  # Week day, Month, Day, Year
