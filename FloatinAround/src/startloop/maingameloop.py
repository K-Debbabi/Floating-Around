import pygame
import sys

#import
from startloop.startscreenloop import startscreen
from startloop.guideloop import guide
from gameloop.gameloop import gameloop
from gameloop.player.player import player_init
from startloop.guide import guide


def main_gameloop():
    """
    Das ist die Haupt funktion, welche die Zuständigkeit hat, alle "Unter_loops" auszuführen (beispiele für
    diese währen startloop, gameloop, settingsloop... ) und pygame zu starten. [KC]
    """

    pygame.init()
    pygame.mixer.init()
    player_init()

    # Starte im Fullscreen-Modus mit aktueller Auflösung
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, pygame.SRCALPHA)
    pygame.display.set_caption("FloatinAround")

    clock = pygame.time.Clock()

    # Dynamische Bildschirmgröße
    screen_width, screen_height = screen.get_size()

    # Bestenliste-Platzhalter
    highscores = [99, 98, 76, 45, 30]

    # Wichtige Loop Variablen [KC]
    running = True # Status des Programmes [KC]
    current_loop = "startscreen" # Actueller screen [KC]

    # loop beginnt ab hier [KC] ----- ----- -----

    while running:

        # Je nachdem welche loop, die derzeit gebraucht wird, wird ein unterschiedlicher code ausgeführt (z.B gameloop, startloop ...) [KC]
        if current_loop == "startscreen":
            current_loop, running = startscreen.loop(screen_width, screen_height, screen, highscores)

        elif current_loop == "gameloop":
            current_loop, running = gameloop.loop(screen, False)

        elif current_loop == "guideloop":
            current_loop, running = guide.loop(screen)

        elif current_loop == "load":
            current_loop, running = gameloop.loop(screen, True)

        pygame.display.flip()
        clock.tick(60)


    # Projekt schließung
    pygame.quit()
    sys.exit()