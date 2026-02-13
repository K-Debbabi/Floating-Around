import pygame


class player_bar():
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    ORANGE = (255, 165, 0)
    BLUE = (0, 150, 255)
    BLACK = (0, 0, 0)

    damagesound = ...

    # lebensleiste
    MAX_HEALTH = 100
    CURRENT_HEALTH = 100
    # hungerleiste
    MAX_HUNGER = 100
    CURRENT_HUNGER = 100
    # durstleiste
    MAX_THIRST = 100
    CURRENT_THIRST = 100

    last_timestamp_d = 0
    last_timestamp_h = 0

    @staticmethod
    def change_bars(new_thirst, new_hunger, new_health):
        """
        ändert die player bars
        Parameters
        ----------
        new_thirst
        new_hunger
        new_health
        """
        player_bar.CURRENT_THIRST += new_thirst
        if player_bar.CURRENT_THIRST > player_bar.MAX_THIRST:
            player_bar.CURRENT_THIRST = player_bar.MAX_THIRST
        player_bar.CURRENT_HUNGER += new_hunger
        if player_bar.CURRENT_HUNGER > player_bar.MAX_HUNGER:
            player_bar.CURRENT_HUNGER = player_bar.MAX_HUNGER
        player_bar.CURRENT_HEALTH  += new_health
        if player_bar.CURRENT_HEALTH > player_bar.MAX_HEALTH:
            player_bar.CURRENT_HEALTH = player_bar.MAX_HEALTH

    @staticmethod
    def get_heatlth():
        """
        gibt die Leben zurück
        Returns
        -------

        """
        return player_bar.CURRENT_HEALTH

    @staticmethod
    def usable_bars():
        timestamp = pygame.time.get_ticks()
        if timestamp - player_bar.last_timestamp_h > 5000:
            player_bar.CURRENT_HUNGER -= 1
            if player_bar.CURRENT_HUNGER <= 0:
                player_bar.CURRENT_HUNGER = 0
                player_bar.CURRENT_HEALTH -= 5
                player_bar.damagesound.play()
            player_bar.last_timestamp_h = timestamp

        if timestamp - player_bar.last_timestamp_d > 2000:
            player_bar.CURRENT_THIRST -= 1
            if player_bar.CURRENT_THIRST <= 0:
                player_bar.CURRENT_THIRST = 0
                player_bar.CURRENT_HEALTH -= 5
                player_bar.damagesound.play()
            player_bar.last_timestamp_d = timestamp

            if player_bar.CURRENT_HEALTH <= 0:
                player_bar.CURRENT_HEALTH = 0
            elif player_bar.CURRENT_HEALTH < player_bar.MAX_HEALTH and player_bar.CURRENT_THIRST > player_bar.MAX_THIRST - 50 and player_bar.CURRENT_HUNGER > player_bar.MAX_HUNGER - 50:
                player_bar.CURRENT_HEALTH += 1
                player_bar.CURRENT_THIRST -= 1
                player_bar.CURRENT_HUNGER -= 1

            if player_bar.CURRENT_HEALTH > player_bar.MAX_HEALTH:
                player_bar.CURRENT_HEALTH = player_bar.MAX_HEALTH


    @staticmethod
    def init():
        """
        initialisiert
        """
        player_bar.damagesound = pygame.mixer.Sound("assets/sounds/damage.mp3")

        player_bar.damagesound.set_volume(0.1)

    def draw(surface, x, y, current, max_value, width, height, bg_color, fg_color, label):
        """
        zeichnet die player bars
        Parameters
        ----------
        x
        y
        current
        max_value
        width
        height
        bg_color
        fg_color
        label
        """
        pygame.draw.rect(surface, bg_color, (x, y, width, height))
        act = current / max_value
        pygame.draw.rect(surface, fg_color, (x, y, width * act, height))
        pygame.draw.rect(surface, player_bar.BLACK, (x, y, width, height), 2)

        font = pygame.font.SysFont(None, 25)
        text = font.render(f"{label}: {int(current)} / {max_value}", True, (255, 255, 255))
        surface.blit(text, (x + 5, y + height // 4))


    def draw_bars(screen):
        """
        zeichnet die Spiler bars
        """
        player_bar.draw(screen, 10, 10, player_bar.CURRENT_HEALTH, player_bar.MAX_HEALTH, 200, 30, player_bar.RED, player_bar.GREEN, "Health")
        player_bar.draw(screen, 10, 50, player_bar.CURRENT_HUNGER, player_bar.MAX_HUNGER, 200, 30, (100, 50, 0), player_bar.ORANGE, "Hunger")
        player_bar.draw(screen, 10, 90, player_bar.CURRENT_THIRST, player_bar.MAX_THIRST, 200, 30, (0, 0, 50), player_bar.BLUE, "Thirst")