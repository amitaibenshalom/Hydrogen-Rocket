"""
Filename: display.py
Purpose: Display functions for the Hydrogen Rocket UI
"""
from consts import *

def display_opening(screen, language):
    """
    Display the opening screen
    :param screen: the screen to display the opening screen on
    :param language: the language to display the opening screen in
    """
    if language == HEBREW:
        screen.blit(open_heb, (0,0))

    elif language == ENGLISH:
        screen.blit(open_eng, (0,0))

    elif language == ARABIC:
        screen.blit(open_arb, (0,0))


def display_measure(screen, language, charge=0, current=0):
    """
    Display the measurement screen
    :param screen: the screen to display the measurement screen on
    :param language: the language to display the measurement screen in
    """
    if language == HEBREW:
        screen.blit(measure_heb, (0,0))

    elif language == ENGLISH:
        screen.blit(measure_eng, (0,0))

    elif language == ARABIC:
        screen.blit(measure_arb, (0,0))

    screen.blit(bar_empty, (0,0))
    screen.blit(gauge, (0,0))
    
    # calculate the angle of the niddle (mapping the current to the angle 0-180)
    angle = 180 * (current - MIN_CURRENT) / (MAX_CURRENT - MIN_CURRENT)
    display_rotated_niddle(screen, angle)

def display_state(screen, state, language=HEBREW, charge=0, current=0):
    """
    Display the state screen
    :param screen: the screen to display the state screen on
    :param language: the language to display the state screen in
    :param state: the state to display
    """
    if state == OPENING:
        display_opening(screen, language=language)

    elif state == MEASURE:
        display_measure(screen, language=language, charge=charge, current=current)


def display_rotated_niddle(screen, angle):
    """
    Display the niddle rotated to the given angle
    :param screen: the screen to display the niddle on
    :param angle: the angle to rotate the niddle to
    """
    # global niddle
    rotated_niddle = pygame.transform.rotate(niddle, -angle)
    rect = rotated_niddle.get_rect(center=NIDDLE_DISPLACEMENT)
    screen.blit(rotated_niddle, rect.topleft)

