from random import randint
import pygame as pg
import math

pg.init()

# Display
RESOLUTION = WIDTH, HEIGHT = 1280, 960  # Padrão -> 1280, 960
FPS = 60  # Padrão -> 60
FONT = pg.font.Font(pg.font.get_default_font(), 14)


# Map
_ = False
BOOL_MAP = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, 1],
            [1, _, _, _, 1, _, _, _, 1, _, _, 1, 1, 1, 1, 1, 1, 1, _, 1],
            [1, _, _, 1, _, 1, _, 1, _, _, _, 1, _, _, _, _, _, 1, _, 1],
            [1, _, 1, _, _, _, 1, _, _, _, _, _, _, 1, _, 1, _, 1, _, 1],
            [1, _, _, _, _, _, _, _, _, _, _, _, _, 1, _, 1, _, 1, _, 1],
            [1, _, 1, 1, 1, 1, 1, _, 1, 1, _, 1, _, _, _, _, _, 1, _, 1],
            [1, _, _, _, _, _, _, _, _, _, _, 1, 1, _, _, _, 1, 1, _, 1],
            [1, _, 1, _, 1, _, 1, _, _, _, _, 1, _, _, _, _, _, 1, _, 1],
            [1, _, 1, _, 1, _, _, _, 1, 1, _, 1, _, _, 1, _, _, 1, _, 1],
            [1, _, 1, _, 1, 1, 1, _, _, _, _, 1, _, _, _, _, _, 1, _, 1],
            [1, _, 1, _, _, _, _, _, _, _, _, 1, _, _, _, _, _, 1, _, 1],
            [1, _, 1, 1, 1, 1, 1, _, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, _, 1],
            [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Maze Mode - Recomendação: ONLY_DRAW_IN_FOV = True
# BOOL_MAP = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#             [1, _, 1, _, _, _, 1, _, _, _, _, _, 1, _, _, _, 1, _, _, 1],
#             [1, _, 1, 1, 1, _, 1, _, 1, _, 1, _, 1, 1, 1, _, 1, _, 1, 1],
#             [1, _, _, _, _, _, _, _, 1, _, 1, _, _, _, _, _, 1, _, _, 1],
#             [1, _, 1, 1, 1, 1, 1, 1, 1, _, 1, _, 1, 1, 1, _, 1, 1, _, 1],
#             [1, _, 1, _, 1, _, 1, _, _, _, _, _, 1, _, _, _, _, _, _, 1],
#             [1, _, 1, _, 1, _, 1, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, _, 1],
#             [1, _, 1, _, _, _, _, _, 1, _, 1, _, _, _, _, _, _, 1, _, 1],
#             [1, _, 1, 1, 1, _, 1, 1, 1, _, 1, _, 1, 1, _, 1, 1, 1, _, 1],
#             [1, _, _, _, _, _, _, _, _, _, 1, _, _, 1, _, _, _, 1, _, 1],
#             [1, _, 1, 1, 1, _, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, _, 1, _, 1],
#             [1, _, 1, _, _, _, 1, _, 1, _, _, _, _, 1, _, 1, _, _, _, 1],
#             [1, _, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, _, 1],
#             [1, _, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, _, _, _, 1],
#             [1, 1, 1, 1, 1, 1, 1, 1, 1, _, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

MAP_SIZE_X = len(BOOL_MAP[0])
MAP_SIZE_Y = len(BOOL_MAP)


# Player
PLAYER_POS = 1.5, 1.5
# Custom -> (randint(2, MAP_SIZE_X - 2), randint(2, MAP_SIZE_Y - 2))
PLAYER_ANGLE = 0  # Padrão -> 0
PLAYER_SPEED = 0.004  # Padrão -> 0.004
PLAYER_ROT_SPEED = 0.002  # Padrão -> 0.002

FOV = math.pi / 3  # Padrão -> math.pi / 3
HALF_FOV = FOV / 2  # Padrão -> FOV / 2
NUM_RAYS = WIDTH // 2  # Padrão -> WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2  # Padrão -> NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS  # Padrão -> FOV / NUM_RAYS
MAX_DEPTH = MAP_SIZE_X  # Padrão -> MAP_SIZE


# Colors
BACKGROUND_COLOR = (0, 0, 0)  # Padrão -> (0, 0, 0)
WALL_COLOR = (255, 255, 255)  # Padrão -> (255, 255, 255)
PLAYER_COLOR = (50, 170, 100)  # Padrão -> (50, 170, 100)
NPC_COLOR = (200, 25, 25)  # Padrão -> (200, 25, 25)
RAY_COLOR = (242, 255, 0)  # Padrão -> (242, 255, 0)


# Misc
SHOW_RAYS = True  # Padrão -> True
SHOW_DIRECTION = True  # Padrão -> True
SHOW_FPS = False  # Padrão -> False
ONLY_DRAW_IN_FOV = False  # Padrão -> False
# AVISO: Desenvolvimento ainda em alfa