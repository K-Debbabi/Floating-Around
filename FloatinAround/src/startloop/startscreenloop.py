import pygame
from startloop.guide import guide

def draw_font(screen):
    """
    macht die font
    Parameters
    ----------
    screen
    """
    spiel_titel = pygame.image.load("assets/backgrounds/titel.png").convert_alpha()

    screen.blit(spiel_titel, (-100, -200))


# nachoben versetzt [KC]
def draw_highscore(screen: pygame.Surface, font: pygame.font.Font, scores: list[int], screen_width: int, screen_height: int):
    """Zeichnet das Ranking unten rechts. Ist aber nicht active

    Parameters
    ----------
    screen
    font
    scores
    screen_width
    screen_height
    """
    bold_font = pygame.font.SysFont("Courier New", 25, bold=True)
    bold_font.set_underline(True)
    title = bold_font.render("Top-Ranking", True, (255, 255, 255))
    x = screen_width - 20
    y = screen_height - (len(scores) + 1) * 30 - 10
    screen.blit(title, title.get_rect(topright=(x, y)))

    for i, score in enumerate(scores):
        label = f"{i + 1}.  {score} h"
        text = font.render(label, True, (200, 200, 200))
        screen.blit(text, text.get_rect(topright=(x, y + (i + 1) * 30)))

class startscreen:
    # Jegliche Variablen etc für die jeweiligen funktionen werden hier erschaffen (sozusagen Globals aber nur für die funktion) [KC]

    # Farben [KC]
    WHITE = (255, 255, 255)
    BLUE = (50, 120, 200)
    LIGHTBLUE = (100, 170, 255)
    RED = (200, 50, 50)
    BG_COLOR = (30, 30, 30)

    # Knöpfe [KC]
    buttons = []
    labels = ["New Game", "Load", "Guide", "Exit", ]

    # Button-Erstellung
    button_width, button_height = 180, 50
    button_margin = 10

    def loop(screen_width: int, screen_height: int, screen: pygame.Surface, highscores: list[any]):
        """
        Macht die Start screen loop also den loop bei dem starten (hintergrund bild etc)
        Parameters
        ----------
        screen_height
        screen
        highscores

        Returns
        -------

        """
        # Fonts [KC]

        # Für performence und generely bessere übersicht wäre es noch schön das nach drausen zutun,
        # weil dann muss es die font nicht die Ganze Zeit neu definiert :) [KC] (todo)

        font = pygame.font.SysFont("Courier New", 25, bold=True)

        for i, label in enumerate(startscreen.labels):
            x = startscreen.button_margin
            y = screen_height - ((startscreen.button_height + startscreen.button_margin) * (len(startscreen.labels) - i))  # 4 zu den Anzahl der Buttons geändert [KC]
            rect = pygame.Rect(x, y, startscreen.button_width, startscreen.button_height)
            startscreen.buttons.append({"label": label, "rect": rect})

        # Schließen-Button oben rechts
        close_button = pygame.Rect(screen_width - 40, 10, 30, 30)

        running = True
        current_loop = "startscreen"

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False  # ESC zum Beenden
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_click = True

        # Background [KC]
        bg_image = pygame.image.load("assets/backgrounds/background.png")
        background_image = pygame.transform.scale(bg_image, (screen_width, screen_height))
        screen.blit(background_image, (0, 0))

        # KI-Anfang
        # KI: ChatGPT
        # prompt: zeichne mir die Buttons inkl. dem hovering mit der maus über die Buttons
        for btn in startscreen.buttons:
            hovered = btn["rect"].collidepoint(mouse_pos)
            color = startscreen.LIGHTBLUE if hovered else startscreen.BLUE
            pygame.draw.rect(screen, color, btn["rect"], border_radius=5)
            text = font.render(btn["label"], True, startscreen.WHITE)
            screen.blit(text, text.get_rect(center=btn["rect"].center))
            if hovered and mouse_click:
                if btn["label"] == "Exit":
                    running = False
                if btn["label"] == "New Game": # Anfang von Karim code[KC]
                    current_loop = "gameloop"
                if btn["label"] == "Guide":
                    current_loop = "guideloop"  # Ende von Karim code[KC]
                if btn["label"] == "Load":
                    current_loop = "load"
        # KI-Ende

        # Bestenliste unten rechts anzeigen
        #draw_highscore(screen, font, highscores, screen_width, screen_height)
        draw_font(screen)

        return current_loop, running
