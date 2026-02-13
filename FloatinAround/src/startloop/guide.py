import pygame
import sys

class guide:
    GUIDE_WIDTH = 1100
    GUIDE_HEIGHT  = 700


    @staticmethod
    def loop(screen):
        """
        loop vom Guide wird über startscree ausgegeben
        Parameters
        ----------
        screen

        Returns
        -------

        """
        WIDTH, HEIGHT = screen.get_size()
        clock = pygame.time.Clock()
        font = pygame.font.SysFont("Courier New", 25, bold=True)
        title_font = pygame.font.SysFont("Courier New", 36, bold=True)

        back_button = pygame.Rect(WIDTH - 60, 20, 40, 40)

        guide_text = [
            "+------------------------------------------------------------------+",
            "|                                                                  |",
            "|                    Welcome to Floatin' Around!                   |",
            "|                                                                  |",
            "|                  Controls:                                       |",
            "|              - W/A/S/D: move                                     |",
            "|              - Mouse: throw hook                                 |",
            "|              - Esc: exit                                         |",
            "|                                                                  |",
            "|                  Goals:                                          |",
            "|              - Manage your hunger and thirst to survive          |",
            "|              - Defend your raft from sharks                      |",
            "|              - Build up your raft to a floating base             |",
            "|              - Have fun and let's survive :)                     |",
            "|                                                                  |",
            "|                                                                  |",
            "|                                                                  |",
            "+------------------------------------------------------------------+",
        ]

        running = True
        current_loop = "guideloop"

        while running:
            pygame.draw.rect(screen, "white", ((WIDTH / 2) -  guide.GUIDE_WIDTH / 2, (HEIGHT / 2) -  guide.GUIDE_HEIGHT / 2, guide.GUIDE_WIDTH, guide.GUIDE_HEIGHT), border_radius=20)

            title = title_font.render("HOW TO PLAY?", True, (0, 0, 0))
            screen.blit(title, (WIDTH//2 - title.get_width()//2, 130))

            for i, line in enumerate(guide_text):
                label = font.render(line, True, (0, 0, 0))
                screen.blit(label, (290, 180 + i * 30))

            # Zurück-Button
            mouse_pos = pygame.mouse.get_pos()
            hover = back_button.collidepoint(mouse_pos)
            pygame.draw.rect(screen, (200, 0, 0) if not hover else (220, 20, 60), back_button, border_radius=8)
            back_label = font.render("->", True, (0, 0, 0))
            screen.blit(back_label, back_label.get_rect(center=back_button.center))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "exit", False
                elif event.type == pygame.MOUSEBUTTONDOWN and hover:
                    return "startscreen", True

            pygame.display.flip()
            clock.tick(60)

        return current_loop, True

