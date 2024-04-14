from configs.settings import *


def text_render(screen: pg.Surface,
                font: pg.font.Font,
                text: str,
                antialias: bool,
                color: tuple,
                pos: tuple,
                background: tuple = None,
                relative_to: int = 0):
    text_to_render = font.render(text, antialias, color, background)

    match relative_to:
        case 1:
            rect_to_render = text_to_render.get_rect(center=pos)
        case 2:
            rect_to_render = text_to_render.get_rect(topright=pos)
        case _:
            rect_to_render = text_to_render.get_rect(topleft=pos)

    screen.blit(text_to_render, rect_to_render)
