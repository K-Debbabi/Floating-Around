import math
import pygame


class raft:

    # Globale variablen von der Klasse [KC]
    RAFTMAP = []
    TILE_SIZE = 64
    RAFTSIZE = 1
    first_tile_pos = []
    images: list[pygame.Surface]
    images2: list[pygame.Surface]
    images3: list[pygame.Surface]

    @staticmethod
    def get_other_otherRAFTMAP():
        """
        gibt raft map zurück
        Returns
        -------

        """
        return raft.RAFTMAP

    @staticmethod
    def set_map(map):
        """
        setzt die map
        Parameters
        ----------
        map
        """
        raft.RAFTMAP = map

    def create(screen: pygame.Surface):
        """
        Macht eine Map aus verschiedenen Symbolen wie 0 für nix und 1 für Floss_Tile
        Parameters
        ----------
        screen der actuelle screena

        [KC]
        """
        # berrechnungen um die MAP zu erstellen [KC]

        screen_width, screen_height = screen.get_size()
        middle = [screen_width / 2 - raft.TILE_SIZE / 2, screen_height / 2 - raft.TILE_SIZE / 2]

        amount_width_tiles = math.floor((screen_width) / raft.TILE_SIZE)
        amount_height_tiles = math.floor((screen_height) / raft.TILE_SIZE) - 1
        raft.first_tile_pos = [middle[0] - (math.floor(amount_width_tiles / 2) * raft.TILE_SIZE), middle[1] - (math.floor(amount_height_tiles / 2) * raft.TILE_SIZE)]

        # erstellt die RAFTMAP und added auch ein je nach raft size große Raft [KC]
        line = []
        for y in range(amount_height_tiles + 1):
            for x in range(amount_width_tiles + 1):
                if (amount_height_tiles / 2) - raft.RAFTSIZE -1 <= y <= (amount_height_tiles / 2) + raft.RAFTSIZE and (amount_width_tiles / 2) - raft.RAFTSIZE -1 <= x <= (amount_width_tiles / 2) + raft.RAFTSIZE:
                    line.append(1)
                else:
                    line.append(0)
            raft.RAFTMAP.append(line)
            line = []

    @staticmethod
    def init():
        """
        initianiliesiert alle raft Bilder:

        raft_tile
        raft_tile_placeable
        raft_tile_not_placeable
        raft_tile_remove

        # später dann vieleicht wenn noch Zeit ist
        net_tile
        net_tile_placeable
        net_tile_not_placeable
        net_tile_remove

        [KC]
        """

        # später so machen das alles in einer Liste und nicht einzelt [KC]

        image = pygame.image.load("assets/raft_assets/raft_tile.png")
        raft.images = pygame.transform.scale(image, (raft.TILE_SIZE, raft.TILE_SIZE))

        image2 = pygame.image.load("assets/raft_assets/raft_tile_placeable.png")
        raft.images2 = pygame.transform.scale(image2, (raft.TILE_SIZE, raft.TILE_SIZE))

        image3 = pygame.image.load("assets/raft_assets/raft_tile_not_placeable.png")
        raft.images3 = pygame.transform.scale(image3, (raft.TILE_SIZE, raft.TILE_SIZE))

    def is_hovering(left_click, Handamound):
        """
        macht hovering und ändert das in der map
        Parameters
        ----------
        Handamound

        Returns
        -------

        """
        if Handamound > 0:
            mouse_pos = pygame.mouse.get_pos()
            for y in range(len(raft.RAFTMAP)):
                for x in range(len(raft.RAFTMAP[y])):
                    if raft.RAFTMAP[y][x] == -1:
                        raft.RAFTMAP[y][x] = 0
                    elif raft.RAFTMAP[y][x] == -2:
                        raft.RAFTMAP[y][x] = 0
                    elif raft.RAFTMAP[y][x] == -3:
                        raft.RAFTMAP[y][x] = 1

            for y in range(len(raft.RAFTMAP)):
                for x in range(len(raft.RAFTMAP[y])):
                    if raft.first_tile_pos[0] + (raft.TILE_SIZE * x) < mouse_pos[0] <= raft.first_tile_pos[0] + (raft.TILE_SIZE * x) + raft.TILE_SIZE and raft.first_tile_pos[1] + (raft.TILE_SIZE * y) < mouse_pos[1] <= raft.first_tile_pos[1] + (raft.TILE_SIZE * y) + raft.TILE_SIZE:
                        if raft.RAFTMAP[y][x] == 0:
                            try:
                                if raft.RAFTMAP[y + 1][x] == 1 or raft.RAFTMAP[y - 1][x] == 1 or raft.RAFTMAP[y][x + 1] == 1 or raft.RAFTMAP[y][x - 1] == 1:
                                    raft.RAFTMAP[y][x] = -2
                                else:
                                    raft.RAFTMAP[y][x] = -1
                            except:
                                pass
                        elif raft.RAFTMAP[y][x] == 1:
                            raft.RAFTMAP[y][x] = -3

            for y in range(len(raft.RAFTMAP)):
                for x in range(len(raft.RAFTMAP[y])):
                    if raft.RAFTMAP[y][x] == -2 and left_click:
                        raft.RAFTMAP[y][x] = 1
                        Handamound -= 1
                    elif raft.RAFTMAP[y][x] == -3 and left_click:
                        raft.RAFTMAP[y][x] = 0
                        Handamound += 1

        return Handamound

    @staticmethod
    def delete_raft_by_cords(pos_x, pos_y):
        """
        für den hai damit er das floss zerstört
        Parameters
        ----------
        pos_x
        pos_y
        """
        for y in range(len(raft.RAFTMAP)):
            for x in range(len(raft.RAFTMAP[y])):
                tile_x = raft.first_tile_pos[0] + x * 64
                tile_y = raft.first_tile_pos[1] + y * 64
                if tile_x <= pos_x < tile_x + 64 and tile_y <= pos_y < tile_y + 64:
                    if raft.RAFTMAP[y][x] == 1:
                        raft.RAFTMAP[y][x] = 0


    @staticmethod
    def draw(screen: pygame.Surface) -> None:
        """
        Gibt das Raft auf den screen aus [KC]
        """
        for y in range(len(raft.RAFTMAP)):
            for x in range(len(raft.RAFTMAP[y])):
                if raft.RAFTMAP[y][x] == 0:
                    pass
                elif raft.RAFTMAP[y][x] == 1:
                    screen.blit(raft.images, (raft.first_tile_pos[0] + (raft.TILE_SIZE * x), raft.first_tile_pos[1] + (raft.TILE_SIZE * y)))


    @staticmethod
    def draw_hover(screen: pygame.Surface) -> None:
        """
        zeigt hovering an
        Parameters
        ----------
        screen
        """
        for y in range(len(raft.RAFTMAP)):
            for x in range(len(raft.RAFTMAP[y])):
                if raft.RAFTMAP[y][x] == 0:
                    pass
                elif raft.RAFTMAP[y][x] == -2:
                    screen.blit(raft.images2, (raft.first_tile_pos[0] + (raft.TILE_SIZE * x), raft.first_tile_pos[1] + (raft.TILE_SIZE * y)))
                elif raft.RAFTMAP[y][x] == -1:
                    screen.blit(raft.images3, (raft.first_tile_pos[0] + (raft.TILE_SIZE * x), raft.first_tile_pos[1] + (raft.TILE_SIZE * y)))
                elif raft.RAFTMAP[y][x] == -3:
                    screen.blit(raft.images3, (raft.first_tile_pos[0] + (raft.TILE_SIZE * x), raft.first_tile_pos[1] + (raft.TILE_SIZE * y)))