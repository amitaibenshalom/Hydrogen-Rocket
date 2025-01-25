import os
import pygame


HEBREW = 0
ENGLISH = 1
ARABIC = 2
LANGUAGES = [HEBREW, ENGLISH, ARABIC]

OPENING = 0
MEASURE = 1
STATES = [OPENING, MEASURE]


MIN_CHARGE = 0.0
MAX_CHARGE = 120.0

MIN_CURRENT = 0.0
MAX_CURRENT = 8.0


# pictures

pygame.init()
VIEW_PORT = pygame.display.Info().current_w, pygame.display.Info().current_h  # get the screen resolution
VIEW_PORT = (607.5, 1080)
# VIEW_PORT = (1080, 1920)

PICTURES = os.path.join(os.path.dirname(__file__), "pictures")  # get the path of the pictures folder
OPEN_HEB = os.path.join(PICTURES, "open_heb.png")
OPEN_ENG = os.path.join(PICTURES, "open_eng.png")
OPEN_ARB = os.path.join(PICTURES, "open_arb.png")
MEASURE_HEB = os.path.join(PICTURES, "main_heb.png")
MEASURE_ENG = os.path.join(PICTURES, "main_eng.png")
MEASURE_ARB = os.path.join(PICTURES, "main_arb.png")
BAR_EMPTY = os.path.join(PICTURES, "bar_empty.png")
GAUGE = os.path.join(PICTURES, "gauge.png")

# load the pictures
open_heb = pygame.image.load(OPEN_HEB)
open_eng = pygame.image.load(OPEN_ENG)
open_arb = pygame.image.load(OPEN_ARB)
measure_heb = pygame.image.load(MEASURE_HEB)
measure_eng = pygame.image.load(MEASURE_ENG)
measure_arb = pygame.image.load(MEASURE_ARB)
bar_empty = pygame.image.load(BAR_EMPTY)
niddle = pygame.image.load(os.path.join(PICTURES, "niddle.png"))
gauge = pygame.image.load(GAUGE)

# transform the pictures to the screen resolution
open_heb = pygame.transform.scale(open_heb, VIEW_PORT)
open_eng = pygame.transform.scale(open_eng, VIEW_PORT)
open_arb = pygame.transform.scale(open_arb, VIEW_PORT)
measure_heb = pygame.transform.scale(measure_heb, VIEW_PORT)
measure_eng = pygame.transform.scale(measure_eng, VIEW_PORT)
measure_arb = pygame.transform.scale(measure_arb, VIEW_PORT)
bar_empty = pygame.transform.scale(bar_empty, VIEW_PORT)
gauge = pygame.transform.scale(gauge, VIEW_PORT)
# niddle is a little tricky:
niddle = pygame.transform.scale(niddle, (int(niddle.get_size()[0] * VIEW_PORT[0] / 1080),
                                         int(niddle.get_size()[1] * VIEW_PORT[1] / 1920)))

NIDDLE_DISPLACEMENT = (0.5 * VIEW_PORT[0], 0.43 * VIEW_PORT[1])  # the position of the niddle on the screen