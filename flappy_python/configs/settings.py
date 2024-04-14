try:
    import pygame as pg
except ImportError:
    exit()

RESOLUTION = SCREEN_WIDTH, SCREEN_HEIGHT = 720, 480
SCREEN_NAME = "Flappy Python"
FRAMES_PER_SECOND = 60
PLAYER_SPEED = -25000
GRAVITY_SPEED = 750
SPEED_CAP = 300
