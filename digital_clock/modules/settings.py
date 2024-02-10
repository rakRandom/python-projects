import pygame as pg
import time
import sys

pg.init()

RES = WIDTH, HEIGHT = 540, 320
FPS = 60

TITLE_FONT = pg.font.Font(pg.font.get_default_font(), 26)
HOUR_FONT = pg.font.Font(pg.font.get_default_font(), 80)
DATE_FONT = pg.font.Font(pg.font.get_default_font(), 24)
BUTTON1_FONT = pg.font.Font(pg.font.get_default_font(), 20)
BUTTON2_FONT = pg.font.Font(pg.font.get_default_font(), 16)
FONT = pg.font.Font(pg.font.get_default_font(), 14)

WHITE = "#FDFDFD"
BLACK = "#202020"

# Main
THEMEB_POS = (WIDTH // 2, HEIGHT - 40)
MUTEB_POS = (5, HEIGHT - 5)
LANGB_POS = (WIDTH - 5, HEIGHT - 5)

# DClock
DCLOCK_TITLE_POS = (WIDTH // 2, 40)
HOURL_POS = (WIDTH // 2, 135)
DATEL_POS = (WIDTH // 2, 205)

# Language
LANGUAGE_TITLE_POS = (WIDTH // 2, 40)
BACKB_POS = (35, 25)
PTBRB_POS = (WIDTH // 2, 90)
ENGB_POS = (WIDTH // 2, 130)
FRAB_POS = (WIDTH // 2, 170)

# Texts
BACKB_TEXT = "Back"

# PT-BR
WINDOW_PTBR_CAPTION = "Relógio Digital"

THEMEB_PTBR_TEXT = "Trocar Tema"
MUTEB_PTBR_TEXT = "M para Mutar"
LANGB_PTBR_TEXT = "L para Linguagens"

DCLOCK_TITLE_PTBR_TEXT = "Um Simples Relógio Digital"
DCLOCK_PTBR_WEEK_DAYS = ("Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo")
DCLOCK_PTBR_MONTHS = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

LANGUAGE_TITLE_PTBR_TEXT = "Selecione a linguagem"
PTBRB_PTBR_TEXT = "Português Brasileiro"
ENGB_PTBR_TEXT = "Inglês"
FRAB_PTBR_TEXT = "Francês"

# ENG
WINDOW_ENG_CAPTION = "Digital Clock"

THEMEB_ENG_TEXT = "Change Theme"
MUTEB_ENG_TEXT = "M to Mute"
LANGB_ENG_TEXT = "L to Language"

DCLOCK_TITLE_ENG_TEXT = "A Simple Digital Clock"
DCLOCK_ENG_WEEK_DAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
DCLOCK_ENG_MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

LANGUAGE_TITLE_ENG_TEXT = "Select the language"
PTBRB_ENG_TEXT = "Brazilian Portuguese"
ENGB_ENG_TEXT = "English"
FRAB_ENG_TEXT = "French"

# French
WINDOW_FRA_CAPTION = "Horloge digitale"

THEMEB_FRA_TEXT = "Change le thème"
MUTEB_FRA_TEXT = "M pour Muet"
LANGB_FRA_TEXT = "L à la langue"

DCLOCK_TITLE_FRA_TEXT = "Une Simple Horloge Numérique"
DCLOCK_FRA_WEEK_DAYS = ("Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche")
DCLOCK_FRA_MONTHS = ("Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre")

LANGUAGE_TITLE_FRA_TEXT = "Sélectionnez la langue"
PTBRB_FRA_TEXT = "Portugais Brésilien"
ENGB_FRA_TEXT = "Anglais"
FRAB_FRA_TEXT = "Français"
