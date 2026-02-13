from abc import abstractmethod

import pygame

from save_load.save import save
from save_load.load import load
from gameloop.hai import hai
from gameloop.bars.player_bars import player_bar
from gameloop.player.player import draw_player, player_move, get_cords
from gameloop.raft_and_building_layer.raft import raft
from gameloop.raft_and_building_layer.building import Building
from gameloop.water.water import water
from gameloop.water.objects import object
from gameloop.hook.hook import hook
from gameloop.fishing.fishing import fishing
from gameloop.popups.pause_menue import Button
#from FloatinAround.src.gameloop.player.player import PLAYER_CORDS
from gameloop.inventory.inventory import inventory


class gameloop:
    creates = True
    inits = True
    paused = False
    left_lift = False
    right_click = False
    resources = [0, 0, 0]# wood, leather, rope
    drinking = ...
    eating = ...
    death = ...

    @staticmethod
    def loop(screen: pygame.Surface, take_from_save = False):
        """
        Fügt eine spiel loop hinzu wo das Hauptspiel gestarted wird
        Parameters geladen
        ----------
        screen ausgabe fenster
        take_from_save laden
        Returns
        -------

        """
        screen_width, screen_height = screen.get_size()
        running = True
        current_loop = "gameloop"

        # reseten von clicks [KD]
        left_click = False
        left_arrow_single = False
        right_arrow_single = False
        left_click_single = False
        e_press = False
        gameloop.left_click = False
        gameloop.left_lift = False
        gameloop.right_click = False





        if gameloop.creates:
            # Erstellungen [KC]
            #gameloop.resources = [0, 0, 0]
            raft.create(screen)
            Building.create(screen)
            inventory.create_newslots()
            gameloop.creates = False

        if gameloop.inits:
            # Initialisierung [KC]
            gameloop.drinking = pygame.mixer.Sound("assets/sounds/drinking.mp3")
            gameloop.eating = pygame.mixer.Sound("assets/sounds/eating.mp3")
            gameloop.death = pygame.image.load("assets/inventory_assets/deathscreen.png")
            fishing.init()
            player_bar.init()
            inventory.init()
            Button.init(screen)
            water.background_init(screen)
            object.init()
            raft.init()
            Building.init()
            hook.init()
            gameloop.inits = False

        if take_from_save:
            filefound, resources, inv, Map_R, Map_C = load.read()
            if filefound:
                gameloop.resources = [int(resources[0]), int(resources[1]), int(resources[2])]
                inventory.set_inv(inv)
                Building.set_map(Map_C)
                raft.set_map(Map_R)
            else:
                return "startscreen", True



        hearts = player_bar.get_heatlth()
        if hearts == 0:
            screen_width, screen_height = screen.get_size()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    running = True
                    current_loop = "startscreen"

            screen.blit(gameloop.death, (screen_width / 2 - 314 / 2,screen_height / 2 - 189 / 2))


        elif gameloop.paused:
            # when man im escape menue ist:

            mouse_button = pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    if gameloop.paused:
                        gameloop.paused = False
                    else:
                        gameloop.paused = True
            if mouse_button[0]:  # Linke Maustaste ist gedrückt [KD]
                left_click = True
            Button.draw(screen)
            current_loop = Button.is_clicked_save_and_quit(screen, left_click)
            if current_loop != "gameloop":
                gameloop.paused = False
                gameloop.creates = True
            if gameloop.paused != False:
                gameloop.paused = Button.is_clicked_resume(screen, left_click)


        else:
            # Events [KC]
            mouse_button = pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    if gameloop.paused:
                        gameloop.paused = False
                    else:
                        gameloop.paused = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                    e_press = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    left_arrow_single = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    right_arrow_single = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Linke Maustaste ist gedrückt [KD]
                    left_click_single = True
                if event.type == 3 and event.type == pygame.MOUSEBUTTONDOWN:
                    gameloop.right_click = True
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    gameloop.left_lift = True

            if mouse_button[0]:  # Linke Maustaste ist gedrückt [KD]
                left_click = True

            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Spiellogic updaten [KC]
            player_bar.usable_bars()
            inventory.delete_unessasary_amounds()
            inventory.open_and_close_inventory(e_press)
            inventory.turn_page(left_click_single, right_arrow_single, left_arrow_single, screen)

            player_move(screen_width, screen_height)
            water.move(screen_width)


            # Background [KC]
            water.draw(screen)

            hai.shark_group.update()
            hai.shark_group.draw(screen)

            object.draw(screen)
            raft.draw(screen)
            Building.draw(screen)


            # Objecte Zeichenen (aufpassen draw order!) [KC]
            player_bar.draw_bars(screen)
            draw_player(screen)

            # hand object zeichnen im game
            inventory.display_slot_items(screen, 5, screen_width - 80, screen_height - 80)
            # checkt welches item gerade benutzt wird
            inv_active, hand_item = inventory.get_hand_item()
            if inv_active == False and hand_item:
                if hand_item == "leather bottle":
                    if left_click_single:
                        player_bar.change_bars(100, 0, 0)
                        amound = inventory.get_amound()
                        inventory.change_amound_off_Hand(amound-1)
                        gameloop.drinking.play()
                elif hand_item == "raft tile":
                    amound = inventory.get_amound()
                    amound = raft.is_hovering(left_click_single, amound)
                    raft.draw_hover(screen)
                    inventory.change_amound_off_Hand(amound)
                elif hand_item == "campfire":
                    amound = inventory.get_amound()
                    amound = Building.is_hovering(left_click_single, amound)
                    Building.draw_hover(screen)
                    inventory.change_amound_off_Hand(amound)
                elif hand_item == "fishing rod":
                    _PLAYER_CORDS = get_cords()
                    fishing.power_bar(gameloop.left_click)
                    fishing.power_bar(left_click)
                    fishing.draw_hook_bar(screen, left_click, _PLAYER_CORDS,  1)
                elif hand_item == "hook MAX" or hand_item == "hook LV1" or hand_item == "hook LV2" or hand_item == "hook":
                    radius = 50
                    Speed = 3
                    if hand_item == "hook LV1":
                        radius = 70
                        Speed = 6
                    if hand_item == "hook LV2":
                        radius = 100
                        Speed = 9
                    if hand_item == "hook MAX":
                        radius = 150
                        Speed = 15
                    _PLAYER_CORDS = get_cords()
                    hook.power_bar(gameloop.left_click)
                    hook.power_bar(left_click)
                    gameloop.resources = hook.draw_hook_bar(screen, left_click, gameloop.resources, radius, _PLAYER_CORDS, Speed)
                elif hand_item == "raw fish":
                    if left_click_single:
                        player_bar.change_bars(0, 20, 0)
                        amound = inventory.get_amound()
                        inventory.change_amound_off_Hand(amound - 1)
                        gameloop.eating.play()
                elif hand_item == "cooked fish":
                    if left_click_single:
                        player_bar.change_bars(0, 50, 0)
                        amound = inventory.get_amound()
                        inventory.change_amound_off_Hand(amound - 1)
                        gameloop.eating.play()
                elif hand_item == "smored fish":
                    if left_click_single:
                        player_bar.change_bars(0, 100, 0)
                        amound = inventory.get_amound()
                        inventory.change_amound_off_Hand(amound - 1)
                        gameloop.eating.play()
                elif hand_item == "empty":
                    active2 = Building.open_campfire(mouse_x, mouse_y, left_click_single)
                    Building.working_campfire(screen, left_click, gameloop.resources)


            object.move(screen_width)
            object.create(screen_height)


            #inventar Zeichnen
            inventory.draw_page(screen)
            inventory.inventory_page(screen, left_click_single, gameloop.left_lift)
            inventory.show_resources(screen, gameloop.resources)
            inventory.page_3_4_crafting(screen, gameloop.resources, left_click_single)

        if current_loop != "gameloop":
            inv = inventory.get_inv()
            mapR = raft.get_other_otherRAFTMAP()
            mapC = Building.get_campfires()

            gameloop.creates = True
            gameloop.inits = True

            save.store(gameloop.resources, inv, mapR, mapC)

        return current_loop, running
