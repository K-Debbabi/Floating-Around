import pygame
from gameloop.water.objects import object
from FloatinAround.src.gameloop.player.player import PLAYER_CORDS


class hook:
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
        erstellen und laden von bildern
        """
        hook.ropesound = pygame.mixer.Sound("assets/sounds/rope_through.mp3")
        hook.ropesound.set_volume(0.5)

    @staticmethod
    def get_cord_till_line(percent, _PLAYER_CORDS):
        """
        berechnet cordinaten des hooks
        Parameters
        ----------
        percent
        _PLAYER_CORDS

        Returns
        -------

        """
        x_partial = _PLAYER_CORDS[0] + (hook.last_hook_pos[0] - _PLAYER_CORDS[0]) * percent
        y_partial = _PLAYER_CORDS[1] + (hook.last_hook_pos[1] -_PLAYER_CORDS[1]) * percent
        partial_end = (x_partial, y_partial)
        return partial_end


    @staticmethod
    def power_bar(left_click):
        """
        power bar display
        Parameters
        ----------
        left_click
        """
        if left_click:
            hook.i += 0.5
            hook.last_click = True
            hook.count = 0
        else:
            hook.count += 1

        if hook.count > 1 and hook.last_click:
            hook.ropesound.play()
            hook.last_i = hook.i
            hook.i = 0
            hook.last_click = False
            x, y = pygame.mouse.get_pos()
            hook.last_hook_pos = (x, y)
            hook.active_hook = True


    @staticmethod
    def draw_hook_bar(screen, left_click, resources, radius, _PLAYER_CORDS, Speed):
        """
        funktionalität vom hook
        Parameters
        ----------
        screen
        left_click
        resources
        radius
        _PLAYER_CORDS
        Speed

        Returns
        -------

        """
        y, x = pygame.mouse.get_pos()
        if left_click:
            pygame.draw.rect(screen, "black", (y - 30, x - 30, 60, 20))
            pygame.draw.rect(screen, "gray", (y - 30 + hook.border_size, x - 30 + hook.border_size, 60 - hook.border_size * 2, 20 - hook.border_size * 2))

            if hook.i > 60 - hook.border_size * 2:
                pygame.draw.rect(screen, "red",(y - 30 + hook.border_size, x - 30 + hook.border_size, 60 - hook.border_size * 2, 20 - hook.border_size * 2))
            elif hook.i > 30 - hook.border_size * 2:
                pygame.draw.rect(screen, "orange", (y - 30 + hook.border_size, x - 30 + hook.border_size, hook.i, 20 - hook.border_size * 2))
            else:
                pygame.draw.rect(screen, ("yellow"),(y - 30 + hook.border_size, x - 30 + hook.border_size, hook.i, 20 - hook.border_size * 2))

        if hook.active_hook:
            if hook.last_i > 60:
                hook.last_i = 60
            hook.length += Speed
            partial_end = hook.get_cord_till_line( hook.length / 100, _PLAYER_CORDS)
            pygame.draw.line(screen, (110, 70, 40), partial_end, (_PLAYER_CORDS[0] + 32, _PLAYER_CORDS[1] + 32), 5)



            if hook.length > hook.last_i * 3:
                hook.length = 0
                hook.active_hook = False
                added_resources = object.put_resources_into_inv(partial_end[0], partial_end[1], radius)
                resources[0] += added_resources[0]
                resources[1] += added_resources[1]
                resources[2] += added_resources[2]
        return resources