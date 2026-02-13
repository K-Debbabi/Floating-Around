import pygame


class Button:
    WHITE = (255, 255, 255)
    GRAY = (30, 30, 30, 128)
    DARK_GRAY = (50, 50, 50)
    RED = (200, 0, 0)
    GREEN = (0, 200, 0)

    font = ...
    BUTTONWIDTH = 300
    BUTTONHEIGHT = 200
    overlay = ...

    @staticmethod
    def init(screen) -> None:
        """
        Macht den text für das clicken und den sound
        """
        Button.font = pygame.font.SysFont(None, 36)

    @staticmethod
    def draw(screen: pygame.Surface) -> None:
        """
        Zeichnet das escape menue mit continue & save and quit
        Parameters
        ----------
        screen die Zeichen ebene
        """
        screen_width, screen_height = screen.get_size()

        pygame.draw.rect(screen, Button.DARK_GRAY, (screen_width / 2 - Button.BUTTONWIDTH / 2, screen_height / 2 - Button.BUTTONHEIGHT / 2, Button.BUTTONWIDTH, Button.BUTTONHEIGHT), border_radius = 20)
        pygame.draw.rect(screen, Button.GREEN, (screen_width / 2 - 100, screen_height / 2 - 25 - 35, 200, 50), border_radius=5)
        text = Button.font.render(f"Resume", True, (255, 255, 255))
        screen.blit(text, (screen_width / 2 - 42, screen_height / 2 - 45))
        pygame.draw.rect(screen, Button.RED, (screen_width / 2 - 100, screen_height / 2 - 25 + 35, 200, 50), border_radius=5)
        text = Button.font.render(f"Save and Quit", True, (255, 255, 255))
        screen.blit(text, (screen_width / 2 - 85, screen_height / 2 + 25))


    @staticmethod
    def is_clicked_resume(screen, left_click):
        """
        schaut ob man weiter spielen will
        Parameters
        ----------
        screen
        left_click

        Returns
        -------

        """
        mouse_x, mous_y = pygame.mouse.get_pos()
        screen_width, screen_height = screen.get_size()
        if screen_width / 2 - 100 < mouse_x < screen_width / 2 - 100 + 200 and screen_height / 2 - 25 - 35  < mous_y < screen_height / 2 - 25 - 35 + 50 and left_click:
            return False
        return True


    @staticmethod
    def is_clicked_save_and_quit(screen, left_click):
        """
        schaut ob man verlässt
        Parameters
        ----------
        screen
        left_click

        Returns
        -------

        """
        mouse_x, mous_y = pygame.mouse.get_pos()
        screen_width, screen_height = screen.get_size()
        if screen_width / 2 - 100 < mouse_x < screen_width / 2 - 100 + 200 and screen_height / 2 - 25 + 35 < mous_y < screen_height / 2 - 25 + 35 + 50 and left_click:
            return "startscreen"
        return "gameloop"

