from gameloop.inventory.inventory import inventory
import pygame
import random

#strc strv von anderem file (hook)
class fishing:
    count = 0
    last_click = False
    border_size = 3
    last_hook_pos = (0, 0)
    i = 0
    last_i = 0
    length = 0
    active_hook = False

    ropesound = ...

    @staticmethod
    def init():
        """
        laden von sound
        """
        fishing.ropesound = pygame.mixer.Sound("assets/sounds/rope_through.mp3")
        fishing.ropesound.set_volume(0.5)

    @staticmethod
    def get_cord_till_line(percent, _PLAYER_CORDS):
        """
        gibt die actuellen cords zurück
        Parameters
        ----------
        percent
        _PLAYER_CORDS

        Returns
        -------

        """
        x_partial = _PLAYER_CORDS[0] + (fishing.last_hook_pos[0] - _PLAYER_CORDS[0]) * percent
        y_partial = _PLAYER_CORDS[1] + (fishing.last_hook_pos[1] -_PLAYER_CORDS[1]) * percent
        partial_end = (x_partial, y_partial)
        return partial_end


    @staticmethod
    def power_bar(left_click):
        """
        Zeigt die power bar
        Parameters
        ----------
        left_click
        """
        if left_click:
            fishing.i += 0.5
            fishing.last_click = True
            fishing.count = 0
        else:
            fishing.count += 1

        if fishing.count > 1 and fishing.last_click:
            fishing.ropesound.play()
            fishing.last_i = fishing.i
            fishing.i = 0
            fishing.last_click = False
            x, y = pygame.mouse.get_pos()
            fishing.last_hook_pos = (x, y)
            fishing.active_hook = True


    @staticmethod
    def draw_hook_bar(screen, left_click, _PLAYER_CORDS, Speed):
        """
        zeichnet die power bar
        Parameters
        ----------
        screen
        left_click
        _PLAYER_CORDS
        Speed
        """
        y, x = pygame.mouse.get_pos()
        if left_click:
            pygame.draw.rect(screen, "black", (y - 30, x - 30, 60, 20))
            pygame.draw.rect(screen, "gray", (y - 30 + fishing.border_size, x - 30 + fishing.border_size, 60 - fishing.border_size * 2, 20 - fishing.border_size * 2))

            if fishing.i > 60 - fishing.border_size * 2:
                pygame.draw.rect(screen, "red",(y - 30 + fishing.border_size, x - 30 + fishing.border_size, 60 - fishing.border_size * 2, 20 - fishing.border_size * 2))
            elif fishing.i > 30 - fishing.border_size * 2:
                pygame.draw.rect(screen, "orange", (y - 30 + fishing.border_size, x - 30 + fishing.border_size, fishing.i, 20 - fishing.border_size * 2))
            else:
                pygame.draw.rect(screen, ("yellow"),(y - 30 + fishing.border_size, x - 30 + fishing.border_size, fishing.i, 20 - fishing.border_size * 2))

        if fishing.active_hook:
            if fishing.length > fishing.last_i * 3:
                fishing.active_hook = False
                fishchrng = random.randint(0, 1000)
                if fishchrng * fishing.length / 40 > 900:
                    inventory.crafting([0, 0, 0], [0, 0, 0], "raw fish")
                fishing.length = 0

            if fishing.last_i > 30:
                fishing.last_i = 30
            fishing.length += Speed
            partial_end = fishing.get_cord_till_line( fishing.length / 100, _PLAYER_CORDS)
            pygame.draw.line(screen, (110, 70, 40), partial_end, (_PLAYER_CORDS[0] + 32, _PLAYER_CORDS[1] + 32), 5)

