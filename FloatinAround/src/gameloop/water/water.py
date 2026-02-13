import pygame



class water():

    Background = pygame.Surface
    Background2 = pygame.Surface
    TILE_SIZE = 512
    TILE_SPEED = 2
    x = 0
    y = 0


    def background_init(screen: pygame.Surface):

        width, height = screen.get_size()
        animation = pygame.image.load("assets/water_assets/water.png")
        water.Background = pygame.transform.scale(animation, (width, height))

        animation = pygame.image.load("assets/water_assets/water.png")
        water.Background2 = pygame.transform.scale(animation, (width, height))


    def move(width: int):
        water.x += water.TILE_SPEED
        if water.x >= width:
            water.x = 0
        water.y = water.x - width

    def draw(_screen: pygame.Surface):
        _screen.blit(water.Background, (water.x, 0))
        _screen.blit(water.Background2, (water.y, 0))