from modules.settings import *


class Button:
    def __init__(self, game, pos, font, text, color, background=None, border=None, orientation=0):
        self.game = game
        self.pos = pos
        self.font = font
        self.text = text
        self.color = color
        self.background = background
        self.border = border

        self.text_label = Label(game, pos, font, text, True, color, background, orientation)
        self.touched = False

    def update(self, pos, font, text, color, background=None, border=None):
        self.pos = pos
        self.font = font
        self.text = text
        self.color = color
        self.background = background
        self.border = border

        self.text_label.update(pos, font, text, True, color, background)

    def update_color(self, color, background=None, border=None):
        self.color = color
        self.background = background
        self.border = border

        self.text_label.update(self.pos, self.font, self.text, True, color, background)

    def update_text(self, text, font=None):
        self.text = text
        self.font = font if font is not None else self.font

        self.text_label.update(self.pos, self.font, text, True, self.color, self.background)

    def draw(self):
        self.text_label.draw()
        if self.border is not None:
            pg.draw.rect(self.game.screen, self.border, self.text_label.rect.inflate(15, 15), 2)

    def is_touched(self):
        if self.is_hovered() and pg.mouse.get_pressed()[0] and not self.touched:
            self.touched = True
            return True
        if not (self.is_hovered() and pg.mouse.get_pressed()[0]):
            self.touched = False
            return False

    def is_hovered(self):
        if self.text_label.rect.inflate(15, 15).collidepoint(pg.mouse.get_pos()):
            return True
        else:
            return False


class Label:
    def __init__(self, game, pos, font, text, antialias, color, background=None, orientation=0):
        self.game = game

        self.pos = pos
        self.font = font
        self.text = text
        self.antialias = antialias
        self.color = color
        self.background = background
        self.orientation = orientation

        self.text_surf = font.render(text, antialias, color, background)
        if orientation == 0:
            self.text_rect = self.text_surf.get_rect(center=pos)
        elif orientation == 1:
            self.text_rect = self.text_surf.get_rect(bottomleft=pos)
        elif orientation == 2:
            self.text_rect = self.text_surf.get_rect(bottomright=pos)

    def update(self, pos, font, text, antialias, color, background=None):
        self.pos = pos
        self.font = font
        self.text = text
        self.antialias = antialias
        self.color = color
        self.background = background

        self.text_surf = font.render(text, antialias, color, background)
        if self.orientation == 0:
            self.text_rect = self.text_surf.get_rect(center=pos)
        elif self.orientation == 1:
            self.text_rect = self.text_surf.get_rect(bottomleft=pos)
        elif self.orientation == 2:
            self.text_rect = self.text_surf.get_rect(bottomright=pos)

    def update_color(self, color, background=None):
        self.color = color
        self.background = background

        self.text_surf = self.font.render(self.text, self.antialias, color, background)

    def update_text(self, text, font=None):
        self.text = text
        self.font = font if font is not None else self.font

        self.text_surf = self.font.render(text, self.antialias, self.color, self.background)

    def draw(self):
        self.game.screen.blit(self.text_surf, self.text_rect)

    @property
    def rect(self):
        return self.text_rect
