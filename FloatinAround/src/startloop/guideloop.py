import pygame



class guide:
    BG_COLOR = (0, 0, 0)

    def loop(screen):
        running = True
        current_loop = "guideloop"

        # Events [KC]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False  # ESC zum Beenden

        screen_width, screen_height = screen.get_size()

        # Spiellogic updaten [KC]

        # Background [KC]
        screen.fill(guide.BG_COLOR)

        # Objecte Zeichenen (aufpassen draw order!) [KC]

        return current_loop, running