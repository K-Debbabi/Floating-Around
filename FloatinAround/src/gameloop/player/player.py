import pygame
import FloatinAround.src.globals.globals as g
from FloatinAround.src.globals.globals import PLAYER_SPEED

PLAYER_CORDS = pygame.Vector2([765, 434])
running_up = []
running_down = []
running_left = []
running_right = []
current_animation = 0
last_timestamp = 0

def get_cords():
    """
    gibt spieler cordinaten zurück
    Returns
    -------

    """
    return PLAYER_CORDS


def move_valid_and_move(screen_width: int, screen_height: int) -> None:
    """
    checkt den move auf ihre validität
    Parameters
    ----------
    screen_width
    screen_height
    """
    global PLAYER_CORDS
    if PLAYER_CORDS[0] < 0:
        PLAYER_CORDS[0] = 0
    if PLAYER_CORDS[0] > screen_width - 64:
        PLAYER_CORDS[0] = screen_width - 64
    if PLAYER_CORDS[1] < 0:
        PLAYER_CORDS[1] = 0
    if PLAYER_CORDS[1] > screen_height - 64:
        PLAYER_CORDS[1] = screen_height - 64


def player_init() -> None:
    """
    ladet die bilder
    """
    global image
    image = pygame.image.load("assets/player_assets/hero.png")
    #image = pygame.transform.scale(image, (g.PLAYER_SIZE_PX * 4, g.PLAYER_SIZE_PX))
    global running_up, running_down, running_left, running_right
    for a in range(4):
        sub_image_up = image.subsurface(g.PLAYER_SIZE_PX * a, 0, g.PLAYER_SIZE_PX, g.PLAYER_SIZE_PX)
        sub_image = pygame.transform.scale(sub_image_up, (64, 64))
        running_up.append(sub_image)
    for b in range(4):
        sub_image_down = image.subsurface((g.PLAYER_SIZE_PX * b) + 64, 0, g.PLAYER_SIZE_PX, g.PLAYER_SIZE_PX)
        sub_image = pygame.transform.scale(sub_image_down, (64, 64))
        running_down.append(sub_image)
    for c in range(4):
        sub_image_left = image.subsurface(g.PLAYER_SIZE_PX * c, 16, g.PLAYER_SIZE_PX, g.PLAYER_SIZE_PX)
        sub_image = pygame.transform.scale(sub_image_left, (64, 64))
        running_left.append(sub_image)
    for d in range(4):
        sub_image_right = image.subsurface((g.PLAYER_SIZE_PX * d) + 64, 16, g.PLAYER_SIZE_PX, g.PLAYER_SIZE_PX)
        sub_image = pygame.transform.scale(sub_image_right, (64, 64))
        running_right.append(sub_image)


def draw_player(screen):
    """
    Animations ausgabe
    Parameters
    ----------
    screen
    """
    global current_animation, last_timestamp
    timestamp = pygame.time.get_ticks()
    if timestamp - last_timestamp > 100:
        current_animation += 1
        if current_animation >= 4:
            current_animation = 0
        last_timestamp = timestamp
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
        screen.blit(running_up[current_animation], (PLAYER_CORDS[0], PLAYER_CORDS[1]))
    elif pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
        screen.blit(running_down[current_animation], (PLAYER_CORDS[0], PLAYER_CORDS[1]))
    elif pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
        screen.blit(running_left[current_animation], (PLAYER_CORDS[0], PLAYER_CORDS[1]))
    elif pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
        screen.blit(running_right[current_animation], (PLAYER_CORDS[0], PLAYER_CORDS[1]))
    else:
        screen.blit(running_down[current_animation], (PLAYER_CORDS[0], PLAYER_CORDS[1]))


def player_move(screen_width, screen_height):
    """
    bewegt den spieler
    Parameters
    ----------
    screen_width
    screen_height
    """
    #global current_frame, frame_counter, current_animation
    pressed_keys = pygame.key.get_pressed()
    #movement = False
    if pressed_keys[pygame.K_w] or pressed_keys[pygame.K_UP]:
        PLAYER_CORDS[1] -= PLAYER_SPEED
        #current_animation == running_up
        #movement = True
    if pressed_keys[pygame.K_s] or pressed_keys[pygame.K_DOWN]:
        PLAYER_CORDS[1] += PLAYER_SPEED
    if pressed_keys[pygame.K_a] or pressed_keys[pygame.K_LEFT]:
        PLAYER_CORDS[0] -= PLAYER_SPEED
    if pressed_keys[pygame.K_d] or pressed_keys[pygame.K_RIGHT]:
        PLAYER_CORDS[0] += PLAYER_SPEED

    move_valid_and_move(screen_width, screen_height)

