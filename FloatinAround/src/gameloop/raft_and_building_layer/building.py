import math
import pygame
from gameloop.raft_and_building_layer.raft import raft

from FloatinAround.src.gameloop.inventory.inventory import inventory


class Building:

    # Globale variablen von der Klasse [KC]
    RAFTMAP = []
    TILE_SIZE = 64
    RAFTSIZE = 0
    first_tile_pos = []
    active = False
    imagesC: list[pygame.Surface]
    imagesC2: list[pygame.Surface]
    imagesC3: list[pygame.Surface]
    campfireimage = pygame.Surface

    @staticmethod
    def set_map(map):
        Building.RAFTMAP = map

    @staticmethod
    def get_campfires():
        """
        gibt campfire zurück
        Returns
        -------

        """
        return Building.RAFTMAP

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
        middle = [screen_width / 2 - Building.TILE_SIZE / 2, screen_height / 2 - Building.TILE_SIZE / 2]

        amount_width_tiles = math.floor((screen_width) / Building.TILE_SIZE)
        amount_height_tiles = math.floor((screen_height) / Building.TILE_SIZE) - 1
        Building.first_tile_pos = [middle[0] - (math.floor(amount_width_tiles / 2) * Building.TILE_SIZE), middle[1] - (math.floor(amount_height_tiles / 2) * Building.TILE_SIZE)]

        line = []
        for y in range(amount_height_tiles + 1):
            for x in range(amount_width_tiles + 1):
                line.append(0)
            Building.RAFTMAP.append(line)
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


        Building.imageC = pygame.image.load("assets/raft_assets/campfire_tile.png")
        Building.imagesC = pygame.transform.scale(Building.imageC, (Building.TILE_SIZE, Building.TILE_SIZE))

        Building.imageC2 = pygame.image.load("assets/raft_assets/campfire_tile_placeable.png")
        Building.imagesC2 = pygame.transform.scale(Building.imageC2, (Building.TILE_SIZE, Building.TILE_SIZE))

        Building.imageC3 = pygame.image.load("assets/raft_assets/campfire_tile_not_placeable.png")
        Building.imagesC3 = pygame.transform.scale(Building.imageC3, (Building.TILE_SIZE, Building.TILE_SIZE))

        Building.campfireimage = pygame.image.load("assets/inventory_assets/campfire_menue.png")

    def is_hovering(left_click, Handamound):
        """
        wenn man mit der maus über bildschirm hovert displayed das ob man das campfire placen kann oder nicht und macht das dann mit links click
        Parameters
        ----------
        Handamound

        Returns
        -------

        """
        if Handamound > 0:
            otherRAFTMAP = raft.get_other_otherRAFTMAP()
            mouse_pos = pygame.mouse.get_pos()
            for y in range(len(Building.RAFTMAP)):
                for x in range(len(Building.RAFTMAP[y])):
                    if Building.RAFTMAP[y][x] == -1:
                        Building.RAFTMAP[y][x] = 0
                    elif Building.RAFTMAP[y][x] == -2:
                        Building.RAFTMAP[y][x] = 0
                    elif Building.RAFTMAP[y][x] == -3:
                        Building.RAFTMAP[y][x] = 1
            for y in range(len(Building.RAFTMAP)):
                for x in range(len(Building.RAFTMAP[y])):
                    if Building.first_tile_pos[0] + (Building.TILE_SIZE * x) < mouse_pos[0] <= Building.first_tile_pos[0] + (Building.TILE_SIZE * x) + Building.TILE_SIZE and Building.first_tile_pos[1] + (Building.TILE_SIZE * y) < mouse_pos[1] <= Building.first_tile_pos[1] + (Building.TILE_SIZE * y) + Building.TILE_SIZE:

                        if Building.RAFTMAP[y][x] == 0:
                            try:
                                if otherRAFTMAP[y][x] == 1:
                                    Building.RAFTMAP[y][x] = -2
                                else:
                                    Building.RAFTMAP[y][x] = -1
                            except:
                                pass
                        elif Building.RAFTMAP[y][x] == 1:
                            Building.RAFTMAP[y][x] = -3

            for y in range(len(Building.RAFTMAP)):
                for x in range(len(Building.RAFTMAP[y])):
                    if Building.RAFTMAP[y][x] == -2 and left_click:
                        Building.RAFTMAP[y][x] = 1
                        Handamound -= 1
                    elif Building.RAFTMAP[y][x] == -3 and left_click:
                        Building.RAFTMAP[y][x] = 0
                        Handamound += 1

        return Handamound

    @staticmethod
    def delete_building_by_cords(pos_x, pos_y):
        """
        deletes a tile if your hovring over it and press left click
        Parameters
        ----------
        pos_x
        pos_y
        """
        for y in range(len(Building.RAFTMAP)):
            for x in range(len(Building.RAFTMAP[y])):
                tile_x = Building.first_tile_pos[0] + x * 64
                tile_y = Building.first_tile_pos[1] + y * 64
                if tile_x <= pos_x < tile_x + 64 and tile_y <= pos_y < tile_y + 64:
                    if Building.RAFTMAP[y][x] == 1:
                        Building.RAFTMAP[y][x] = 0


    @staticmethod
    def draw(screen: pygame.Surface) -> None:
        """
        Gibt das Raft auf den screen aus [KC]
        """
        for y in range(len(Building.RAFTMAP)):
            for x in range(len(Building.RAFTMAP[y])):
                if Building.RAFTMAP[y][x] == 0:
                    pass
                elif Building.RAFTMAP[y][x] == 1:
                    screen.blit(Building.imagesC, (Building.first_tile_pos[0] + (Building.TILE_SIZE * x), Building.first_tile_pos[1] + (Building.TILE_SIZE * y)))


    @staticmethod
    def draw_hover(screen: pygame.Surface) -> None:
        """
        drawed the hovering of the campfire
        Parameters
        ----------
        screen
        """
        for y in range(len(Building.RAFTMAP)):
            for x in range(len(Building.RAFTMAP[y])):
                if Building.RAFTMAP[y][x] == 0:
                    pass
                elif Building.RAFTMAP[y][x] == -2:
                    screen.blit(Building.imagesC2, (Building.first_tile_pos[0] + (Building.TILE_SIZE * x), Building.first_tile_pos[1] + (Building.TILE_SIZE * y)))
                elif Building.RAFTMAP[y][x] == -1:
                    screen.blit(Building.imagesC3, (Building.first_tile_pos[0] + (Building.TILE_SIZE * x), Building.first_tile_pos[1] + (Building.TILE_SIZE * y)))
                elif Building.RAFTMAP[y][x] == -3:
                    screen.blit(Building.imagesC3, (Building.first_tile_pos[0] + (Building.TILE_SIZE * x), Building.first_tile_pos[1] + (Building.TILE_SIZE * y)))

    @staticmethod
    def open_campfire(pos_x, pos_y, left_click):
        """
        opens the campfire
        Parameters
        ----------
        pos_x
        pos_y
        left_click
        """
        for y in range(len(Building.RAFTMAP)):
            for x in range(len(raft.RAFTMAP[0])):
                tile_x = Building.first_tile_pos[0] + x * 64
                tile_y = Building.first_tile_pos[1] + y * 64
                if tile_x <= pos_x < tile_x + 64 and tile_y <= pos_y < tile_y + 64 and left_click and \
                        Building.RAFTMAP[y][x] == 1:
                    if Building.active != True:
                        Building.active = True

    #oder auch nicht gehend  ich check nicht warum inventory.inventory_slots gelöscht und wieder exestend gemacht wird

    def working_campfire(screen, left_click, resources):
        """
        macht das campfire funktional
        Parameters
        ----------
        left_click
        resources

        Returns
        -------

        """
        if Building.active:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            screen_width, screen_height = screen.get_size()
            screen.blit(Building.campfireimage, (screen_width / 2 - 475 / 2, screen_height / 2 - 216 / 2))
            if screen_width / 2 + 475 / 2 - 25 < mouse_x < screen_width / 2 + 475 / 2 - 25 + 25 and screen_height / 2 - 216 / 2 < mouse_y < screen_height / 2 - 216 / 2 + 25 and left_click:
                Building.active = False
            if screen_width / 2 + 165 < mouse_x < screen_width / 2 + 165 + 25 and screen_height / 2 - 85 < mouse_y < screen_height / 2 - 85 + 25 and left_click:
                if inventory.check_and_delete_item("raw fish"):
                    print(1)
                    resources = inventory.crafting(resources, [3, 0, 0], "cooked fish")
            elif screen_width / 2 + 165 < mouse_x < screen_width / 2 + 165 + 25 and screen_height / 2 + 25 < mouse_y < screen_height / 2 + 25 + 25 and left_click:
                if inventory.check_and_delete_item("raw fish"):
                    print(2)
                    resources = inventory.crafting(resources, [10, 0, 0], "smoked fish")
        return resources
        # pygame.draw.rect(screen, "red", (screen_width/2 + 475 / 2 - 25, screen_height/2 - 216 / 2, 25, 25))
        # pygame.draw.rect(screen, "red", (screen_width/2 + 165, screen_height/2 - 85, 50,50))
        # pygame.draw.rect(screen, "red", (screen_width/2 + 165, screen_height/2 + 25, 50,50))


    @staticmethod
    def get_active():
        """
        gibt den status des campfire menues zurück
        Returns
        -------

        """
        return Building.active