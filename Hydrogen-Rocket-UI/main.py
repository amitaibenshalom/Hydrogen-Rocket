"""
File: main.py
Purpose: Main file for the Hydrogen Rocket UI
"""
import pygame
from consts import *
from display import *


def main():
    """
    The main function for the Hydrogen Rocket UI
    """
    pygame.display.set_caption("Hydrogen Rocket")
    screen = pygame.display.set_mode(VIEW_PORT)

    language = HEBREW
    charge = 0.0
    current = 0.0
    state = OPENING

    while True:

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

                if event.key == pygame.K_SPACE:
                    language = (language + 1) % len(LANGUAGES)  # toggle language
                    
                if event.key == pygame.K_UP:
                    charge = min(charge + 1, MAX_CHARGE)

                if event.key == pygame.K_DOWN:
                    charge = max(charge - 1, MIN_CHARGE)

                if event.key == pygame.K_LEFT:
                    current = max(current - 0.2, MIN_CURRENT)

                if event.key == pygame.K_RIGHT:
                    current = min(current + 0.2, MAX_CURRENT)

                if event.key == pygame.K_RETURN:
                    state = (state + 1) % len(STATES)  # toggle state from OPENING to MEASURE
        
        screen.fill((0,0,0))
        display_state(screen, state=state, language=language, charge=charge, current=current)

        pygame.display.flip()
        

main()