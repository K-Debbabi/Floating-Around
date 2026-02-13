import pygame

#from FloatinAround.src.gameloop.hai.hai import screen_width, screen_height


class inventory():

    inventory_slots = []
    page_size = [1048, 605]
    page_0 = pygame.Surface
    page_1 = pygame.Surface
    page_2 = pygame.Surface
    page_3 = pygame.Surface
    page_4 = pygame.Surface
    slotitems_images = []
    turnpagesound = ...
    bookopensound = ...
    deletesound = ...
    craftsound = ...
    blob = ...

    curent_page = [0, 3] #die actuelle seite und die Höchste Seite
    active = False # schaut ob das Inv offen ist
    inventory = ...
    mouse_item = {"last_slot_idx": 0, "slot_item": "empty", "amound": 0, "description": "", "distance_to_item_y": 0,"distance_to_item_x": 0}
    font = ...



    @staticmethod
    def get_hand_item():
        """
        gibt hand item zurück
        Returns
        -------

        """
        return inventory.active, inventory.inventory_slots[5]["slot_item"]

    @staticmethod
    def get_amound():
        """
        gibt den amound zurück
        Returns
        -------

        """
        return inventory.inventory_slots[5]["amound"]

    @staticmethod
    def change_amound_off_Hand(amound):
        """
        ändert den hand amound
        Parameters
        ----------
        amound
        """
        inventory.inventory_slots[5]["amound"] = amound


    @staticmethod
    def get_inv():
        """
        gibt das inventar zurück
        Returns
        -------

        """
        return inventory.inventory_slots

    @staticmethod
    def set_inv(inv):
        """
        setzt das inventar
        Parameters
        ----------
        inv
        """
        inventory.inventory_slots = inv
        for i in range(len(inventory.inventory_slots)):
            inventory.inventory_slots[i]["amound"] = int(inventory.inventory_slots[i]["amound"])

    @staticmethod
    def init() -> None:
            """
            Initialisiert alle Buch seiten und souds
            """
            inventory.turnpagesound = pygame.mixer.Sound("assets/sounds/pageturn.mp3")
            inventory.bookopensound = pygame.mixer.Sound("assets/sounds/book-opening.mp3")
            inventory.deletesound = pygame.mixer.Sound("assets/sounds/trash-sound.mp3")
            inventory.craftsound = pygame.mixer.Sound("assets/sounds/craftingsound.mp3")
            inventory.blob = pygame.mixer.Sound("assets/sounds/blob.mp3")

            inventory.blob.set_volume(1)
            inventory.craftsound.set_volume(0.5)
            inventory.bookopensound.set_volume(1)
            inventory.turnpagesound.set_volume(0.3)
            inventory.deletesound.set_volume(0.5)

            inventory.page_0 = pygame.image.load("assets/inventory_assets/page_0.png")# first pages vom Buch
            inventory.page_1 = pygame.image.load("assets/inventory_assets/page_1.png")# Resources und inventory
            inventory.page_2 = pygame.image.load("assets/inventory_assets/page_2.png")# crafting
            inventory.page_3 = pygame.image.load("assets/inventory_assets/page_3.png")# crafting
            inventory.page_4 = pygame.image.load("assets/inventory_assets/page_4.png")  # crafting

            inventory.font = pygame.font.SysFont(None, 25)

            slot_image = pygame.image.load("assets/inventory_assets/slots.png")
            for i in range(14):
                if i < 5:
                    x = 0
                    i2 = i * 64
                elif 5 <= i < 10:
                    x = 64
                    i2 = (i - 5) * 64
                else:
                    x = 128
                    i2 = (i - 10) * 64

                sub_image = slot_image.subsurface(i2, x, 64, 64)
                inventory.slotitems_images.append(sub_image)


    @staticmethod
    def open_and_close_inventory(e_press: bool) -> None:
        """
        Öffnet und schließt das Inventar
        Parameters
        ----------
        e_press Sagt ob e gedrückt wurde
        """
        if e_press:
            inventory.bookopensound.play()
            if inventory.active:
                inventory.active = False
            else:
                inventory.active = True

    @staticmethod
    def create_newslots() -> None:
        """
        creates all the slots for the new inventory
        """
        inventory.inventory_slots = []
        armor_slot1 = {"type_slot":"helmet", "slot_item":"empty", "amound":0, "description":""}
        armor_slot2 = {"type_slot": "chestplate", "slot_item": "empty", "amound":0, "description":""}
        armor_slot3 = {"type_slot": "leggins", "slot_item": "empty", "amound":0, "description":""}
        armor_slot4 = {"type_slot": "boot", "slot_item": "empty", "amound":0, "description":""}
        inventory.inventory_slots.append(armor_slot1)
        inventory.inventory_slots.append(armor_slot2)
        inventory.inventory_slots.append(armor_slot3)
        inventory.inventory_slots.append(armor_slot4)
        handslot = {"type_slot": "hand", "slot_item": "empty", "amound":0, "description":""}
        inventory.inventory_slots.append(handslot)
        infoslot = {"type_slot": "info", "slot_item": "empty", "amound":0, "description":""}
        inventory.inventory_slots.append(infoslot)
        for i in range(10):
            normalslot = {"type_slot": "normal", "slot_item": "empty", "amound": 0, "description":""}
            inventory.inventory_slots.append(normalslot)

        inventory.inventory_slots[5]["slot_item"] = "hook"
        inventory.inventory_slots[5]["amound"] = 1



    @staticmethod
    def putdownitem(idx):
        """
        mahct das man item hinlegt
        Parameters
        ----------
        idx
        """
        if inventory.inventory_slots[idx]["slot_item"] == inventory.mouse_item["slot_item"]:
            inventory.inventory_slots[idx]["amound"] += inventory.mouse_item["amound"]
        else:
            inventory.inventory_slots[idx]["amound"] = inventory.mouse_item["amound"]
            inventory.inventory_slots[idx]["slot_item"] = inventory.mouse_item["slot_item"]
        inventory.mouse_item = {"last_slot_idx": 0, "slot_item": "empty", "amound": 0, "description": "",
                                "distance_to_item_y": 0, "distance_to_item_x": 0}

    @staticmethod
    def display_slot_items(screen: pygame.Surface, slot: int, x: float, y: float) -> None:
        """
        zeichnet die Items in ihren slots
        Parameters
        ----------
        screen der Display der Ausgabe
        slot der slot der ausgegeben werden soll
        x cord
        y cord
        """
        if inventory.inventory_slots[slot]["slot_item"] == "leather bottle":
            screen.blit(inventory.slotitems_images[0], (x, y))
            if inventory.inventory_slots[slot]["amound"] > 1:
                text = inventory.font.render(f"{inventory.inventory_slots[slot]["amound"]}", True, (0, 0, 0))
                screen.blit(text, (x + 55, y + 55))
        elif inventory.inventory_slots[slot]["slot_item"] == "campfire":
            screen.blit(inventory.slotitems_images[1], (x, y))
            if inventory.inventory_slots[slot]["amound"] > 1:
                text = inventory.font.render(f"{inventory.inventory_slots[slot]["amound"]}", True, (0, 0, 0))
                screen.blit(text, (x + 55, y + 55))
        elif inventory.inventory_slots[slot]["slot_item"] == "cap":
            screen.blit(inventory.slotitems_images[2], (x, y))
            if inventory.inventory_slots[slot]["amound"] > 1:
                text = inventory.font.render(f"{inventory.inventory_slots[slot]["amound"]}", True, (0, 0, 0))
                screen.blit(text, (x + 55, y + 55))
        elif inventory.inventory_slots[slot]["slot_item"] == "jacket":
            screen.blit(inventory.slotitems_images[3], (x, y))
            if inventory.inventory_slots[slot]["amound"] > 1:
                text = inventory.font.render(f"{inventory.inventory_slots[slot]["amound"]}", True, (0, 0, 0))
                screen.blit(text, (x + 55, y + 55))
        elif inventory.inventory_slots[slot]["slot_item"] == "leggins":
            screen.blit(inventory.slotitems_images[4], (x, y))
            if inventory.inventory_slots[slot]["amound"] > 1:
                text = inventory.font.render(f"{inventory.inventory_slots[slot]["amound"]}", True, (0, 0, 0))
                screen.blit(text, (x + 55, y + 55))
        elif inventory.inventory_slots[slot]["slot_item"] == "boots":
            screen.blit(inventory.slotitems_images[5],( x, y))
            if inventory.inventory_slots[slot]["amound"] > 1:
                text = inventory.font.render(f"{inventory.inventory_slots[slot]["amound"]}", True, (0, 0, 0))
                screen.blit(text, (x + 55, y + 55))
        elif inventory.inventory_slots[slot]["slot_item"] == "raft tile":
            screen.blit(inventory.slotitems_images[6], (x, y))
            if inventory.inventory_slots[slot]["amound"] > 1:
                text = inventory.font.render(f"{inventory.inventory_slots[slot]["amound"]}", True, (0, 0, 0))
                screen.blit(text, (x + 55, y + 55))
        elif inventory.inventory_slots[slot]["slot_item"] == "fishing rod":
            screen.blit(inventory.slotitems_images[7], (x, y))
            if inventory.inventory_slots[slot]["amound"] > 1:
                text = inventory.font.render(f"{inventory.inventory_slots[slot]["amound"]}", True, (0, 0, 0))
                screen.blit(text, (x + 55, y + 55))
        elif inventory.inventory_slots[slot]["slot_item"] == "hook":
            screen.blit(inventory.slotitems_images[8], (x, y))
            if inventory.inventory_slots[slot]["amound"] > 1:
                text = inventory.font.render(f"{inventory.inventory_slots[slot]["amound"]}", True, (0, 0, 0))
                screen.blit(text, (x + 55, y + 55))
        elif inventory.inventory_slots[slot]["slot_item"] == "hook LV1":
            screen.blit(inventory.slotitems_images[9], (x, y))
            if inventory.inventory_slots[slot]["amound"] > 1:
                text = inventory.font.render(f"{inventory.inventory_slots[slot]["amound"]}", True, (0, 0, 0))
                screen.blit(text, (x + 55, y + 55))
        elif inventory.inventory_slots[slot]["slot_item"] == "hook LV2":
            screen.blit(inventory.slotitems_images[10], (x, y))
            if inventory.inventory_slots[slot]["amound"] > 1:
                text = inventory.font.render(f"{inventory.inventory_slots[slot]["amound"]}", True, (0, 0, 0))
                screen.blit(text, (x + 55, y + 55))
        elif inventory.inventory_slots[slot]["slot_item"] == "hook MAX":
            screen.blit(inventory.slotitems_images[11], (x, y))
            if inventory.inventory_slots[slot]["amound"] > 1:
                text = inventory.font.render(f"{inventory.inventory_slots[slot]["amound"]}", True, (0, 0, 0))
                screen.blit(text, (x + 55, y + 55))
        elif inventory.inventory_slots[slot]["slot_item"] == "raw fish":
            screen.blit(inventory.slotitems_images[12], (x, y))
            if inventory.inventory_slots[slot]["amound"] > 1:
                text = inventory.font.render(f"{inventory.inventory_slots[slot]["amound"]}", True, (0, 0, 0))
                screen.blit(text, (x + 55, y + 55))
        elif inventory.inventory_slots[slot]["slot_item"] == "cooked fish":
            screen.blit(inventory.slotitems_images[13], (x, y))
            if inventory.inventory_slots[slot]["amound"] > 1:
                text = inventory.font.render(f"{inventory.inventory_slots[slot]["amound"]}", True, (0, 0, 0))
                screen.blit(text, (x + 55, y + 55))
        elif inventory.inventory_slots[slot]["slot_item"] == "smoked fish":
            screen.blit(inventory.slotitems_images[14], (x, y))
            if inventory.inventory_slots[slot]["amound"] > 1:
                text = inventory.font.render(f"{inventory.inventory_slots[slot]["amound"]}", True, (0, 0, 0))
                screen.blit(text, (x + 55, y + 55))
        #else:
        #    exit("wrong item description")

    @staticmethod
    def show_resources(screen: pygame.Surface, resources: list[int]) -> None:
        """
        zeigt resourcen an auf seite 2
        Parameters
        ----------
        screen
        resources
        """
        if inventory.curent_page[0] == 1 and inventory.active:
            width, height = screen.get_size()

            text = inventory.font.render(f"{resources[0]}", True, (0, 0, 0))
            screen.blit(text, (width / 2 + 400, height / 2 - 200))

            text = inventory.font.render(f"{resources[1]}", True, (0, 0, 0))
            screen.blit(text, (width / 2 + 400, height / 2 - 100))

            text = inventory.font.render(f"{resources[2]}", True, (0, 0, 0))
            screen.blit(text, (width / 2 + 400, height / 2))

    @staticmethod
    def inventory_page(screen: pygame.Surface, left_click: bool,  left_lift: bool):
        """
        macht das inventar auf seite 2 funktionell
        Parameters
        ----------
        screen the display screen
        left_click bewegen
        left_lift ablegen
        """
        # leather waterbottel
        # campfire
        # leather cap
        # leather jacket
        # leather leggins
        # leather boots
        # raft tile
        # fishing rod
        # hook better hook

        if inventory.curent_page[0] == 1 and inventory.active:
            width, height = screen.get_size()



            #displays all the normal inventory slots
            if inventory.inventory_slots[0]["slot_item"] != "empty":
                inventory.display_slot_items(screen,0, width / 2 - 480, height / 2 - 260)
            if inventory.inventory_slots[1]["slot_item"] != "empty":
                inventory.display_slot_items(screen,1, width / 2 - 395, height / 2 - 260)
            if inventory.inventory_slots[2]["slot_item"] != "empty":
                inventory.display_slot_items(screen, 2, width / 2 - 225, height / 2 - 260)
            if inventory.inventory_slots[3]["slot_item"] != "empty":
                inventory.display_slot_items(screen,3, width / 2 - 310, height / 2 - 260)
            if inventory.inventory_slots[4]["slot_item"] != "empty":
                inventory.display_slot_items(screen,4, width / 2 - 405, height / 2 - 133)
            if inventory.inventory_slots[5]["slot_item"] != "empty":
                inventory.display_slot_items(screen,5, width / 2 - 115, height / 2 - 260)
            if inventory.inventory_slots[6]["slot_item"] != "empty":
                inventory.display_slot_items(screen, 6, width / 2 - 460, height / 2)
            if inventory.inventory_slots[7]["slot_item"] != "empty":
                inventory.display_slot_items(screen,7, width / 2 - 375, height / 2)
            if inventory.inventory_slots[8]["slot_item"] != "empty":
                inventory.display_slot_items(screen,8, width / 2 - 290, height / 2)
            if inventory.inventory_slots[9]["slot_item"] != "empty":
                inventory.display_slot_items(screen,9, width / 2 - 210, height / 2)
            if inventory.inventory_slots[10]["slot_item"] != "empty":
                inventory.display_slot_items(screen,10, width / 2 - 130, height / 2)
            if inventory.inventory_slots[11]["slot_item"] != "empty":
                inventory.display_slot_items(screen,11, width / 2 - 460, height / 2 + 80)
            if inventory.inventory_slots[12]["slot_item"] != "empty":
                inventory.display_slot_items(screen,12, width / 2 - 375, height / 2 + 80)
            if inventory.inventory_slots[13]["slot_item"] != "empty":
                inventory.display_slot_items(screen,13, width / 2 - 290, height / 2 + 80)
            if inventory.inventory_slots[14]["slot_item"] != "empty":
                inventory.display_slot_items(screen,14, width / 2 - 210, height / 2 + 80)
            if inventory.inventory_slots[15]["slot_item"] != "empty":
                inventory.display_slot_items(screen,15, width / 2 - 130, height / 2 + 80)




            #makes you able to pick up all items
            mouse_x, mouse_y = pygame.mouse.get_pos()
            #inventory.mouse_item = {"last_slot_idx":0, "slot_item": "empty", "amound":0, "description":"", "distance_to_item_y":0, "distance_to_item_x":0}

            if left_click and inventory.mouse_item["slot_item"] == "empty":
                #Findet heraus ob und welches Item du verschieben möchtest
                # hilfe von Chatgpt, weil ich irgenwo irgendweinen fehler gemacht habe (hier noch mein ursprünglichser code:)
                """
                 if left_click:
                if width / 2 - 460 < mouse_x < width / 2 - 460 + 64 and  height / 2 < mouse_y < height / 2 + 64:
                    inventory.mouse_item = {"last_slot_idx": 6, "slot_item": f"{inventory.inventory_slots[6]["slot_item"]}", "amound": inventory.inventory_slots[6]["amound"], "distance_to_item_y": 0,"distance_to_item_x": 0}
                if width / 2 - 374 < mouse_x < width / 2 - 375 + 64 and  height / 2 < mouse_y < height / 2 + 64:
                    inventory.mouse_item = {"last_slot_idx": 7, "slot_item": f"{inventory.inventory_slots[7]["slot_item"]}", "amound": inventory.inventory_slots[7]["amound"], "distance_to_item_y": 0,"distance_to_item_x": 0}
                if width / 2 - 290 < mouse_x < width / 2 - 290 + 64 and  height / 2 < mouse_y < height / 2 + 64:
                    inventory.mouse_item = {"last_slot_idx": 8, "slot_item": f"{inventory.inventory_slots[8]["slot_item"]}", "amound": inventory.inventory_slots[8]["amound"], "distance_to_item_y": 0,"distance_to_item_x": 0}
                if width / 2 - 210 < mouse_x < width / 2 - 210 + 64 and  height / 2 < mouse_y < height / 2 + 64:
                    inventory.mouse_item = {"last_slot_idx": 9, "slot_item": f"{inventory.inventory_slots[9]["slot_item"]}", "amound": inventory.inventory_slots[9]["amound"], "distance_to_item_y": 0,"distance_to_item_x": 0}
                if width / 2 - 460 < mouse_x < width / 2 - 130 + 64 and  height / 2 < mouse_y < height / 2 + 64:
                    inventory.mouse_item = {"last_slot_idx": 10, "slot_item": f"{inventory.inventory_slots[10]["slot_item"]}", "amound": inventory.inventory_slots[10]["amound"], "distance_to_item_y": 0,"distance_to_item_x": 0}
                if width / 2 - 460 < mouse_x < width / 2 - 460 + 64 and  height / 2 + 80< mouse_y < height / 2 + 80 + 64:
                    inventory.mouse_item = {"last_slot_idx": 11, "slot_item": f"{inventory.inventory_slots[11]["slot_item"]}", "amound": inventory.inventory_slots[11]["amound"], "distance_to_item_y": 0,"distance_to_item_x": 0}
                if width / 2 - 374 < mouse_x < width / 2 - 375 + 64 and  height / 2 + 80< mouse_y < height / 2+ 80 + 64:
                    inventory.mouse_item = {"last_slot_idx": 12, "slot_item": f"{inventory.inventory_slots[12]["slot_item"]}", "amound": inventory.inventory_slots[12]["amound"], "distance_to_item_y": 0,"distance_to_item_x": 0}
                if width / 2 - 290 < mouse_x < width / 2 - 290 + 64 and  height / 2 + 80< mouse_y < height / 2+ 80 + 64:
                    inventory.mouse_item = {"last_slot_idx": 13, "slot_item": f"{inventory.inventory_slots[13]["slot_item"]}", "amound": inventory.inventory_slots[13]["amound"], "distance_to_item_y": 0,"distance_to_item_x": 0}
                if width / 2 - 210 < mouse_x < width / 2 - 210 + 64 and  height / 2 + 80< mouse_y < height / 2+ 80 + 64:
                    inventory.mouse_item = {"last_slot_idx": 14, "slot_item": f"{inventory.inventory_slots[14]["slot_item"]}", "amound": inventory.inventory_slots[14]["amound"], "distance_to_item_y": 0,"distance_to_item_x": 0}
                if width / 2 - 460 < mouse_x < width / 2 - 130 + 64 and  height / 2 + 80< mouse_y < height / 2+ 80 + 64:
                    inventory.mouse_item = {"last_slot_idx": 15, "slot_item": f"{inventory.inventory_slots[15]["slot_item"]}", "amound": inventory.inventory_slots[15]["amound"], "distance_to_item_y": 0,"distance_to_item_x": 0}
                """

                if width / 2 - 480 < mouse_x < width / 2 - 480 + 64 and height / 2 - 260 < mouse_y < height / 2 - 260 + 64:
                    inventory.mouse_item = {"last_slot_idx": 0,"slot_item": f"{inventory.inventory_slots[0]['slot_item']}","amound": inventory.inventory_slots[0]["amound"], "distance_to_item_y": 0,"distance_to_item_x": 0}
                    inventory.inventory_slots[0]["slot_item"] = "empty"
                if width / 2 - 395 < mouse_x < width / 2 - 395 + 64 and height / 2 - 260 < mouse_y < height / 2 - 260 + 64:
                    inventory.mouse_item = {"last_slot_idx": 1,"slot_item": f"{inventory.inventory_slots[1]['slot_item']}","amound": inventory.inventory_slots[1]["amound"], "distance_to_item_y": 0,"distance_to_item_x": 0}
                    inventory.inventory_slots[1]["slot_item"] = "empty"
                if width / 2 - 225 < mouse_x < width / 2 - 225 + 64 and height / 2 - 260 < mouse_y < height / 2 - 260 + 64:
                    inventory.mouse_item = {"last_slot_idx": 2,"slot_item": f"{inventory.inventory_slots[2]['slot_item']}","amound": inventory.inventory_slots[2]["amound"], "distance_to_item_y": 0,"distance_to_item_x": 0}
                    inventory.inventory_slots[2]["slot_item"] = "empty"
                if width / 2 - 310 < mouse_x < width / 2 - 310 + 64 and height / 2 - 260 < mouse_y < height / 2 - 260 + 64:
                    inventory.mouse_item = {"last_slot_idx": 3,"slot_item": f"{inventory.inventory_slots[3]['slot_item']}","amound": inventory.inventory_slots[3]["amound"], "distance_to_item_y": 0,"distance_to_item_x": 0}
                    inventory.inventory_slots[3]["slot_item"] = "empty"
                if width / 2 - 405 < mouse_x < width / 2 - 405 + 64 and height / 2 - 133 < mouse_y < height / 2 - 133 + 64:
                    inventory.mouse_item = {"last_slot_idx": 4,"slot_item": f"{inventory.inventory_slots[4]['slot_item']}","amound": inventory.inventory_slots[4]["amound"], "distance_to_item_y": 0,"distance_to_item_x": 0}
                    inventory.inventory_slots[4]["slot_item"] = "empty"
                if width / 2 - 115 < mouse_x < width / 2 - 115 + 64 and height / 2 - 260 < mouse_y < height / 2 - 260 + 64:
                    inventory.mouse_item = {"last_slot_idx": 5,"slot_item": f"{inventory.inventory_slots[5]['slot_item']}","amound": inventory.inventory_slots[5]["amound"], "distance_to_item_y": 0,"distance_to_item_x": 0}
                    inventory.inventory_slots[5]["slot_item"] = "empty"
                if width / 2 - 460 < mouse_x < width / 2 - 460 + 64 and height / 2 < mouse_y < height / 2 + 64 and inventory.inventory_slots[6] != "empty":
                    inventory.mouse_item = {"last_slot_idx": 6,"slot_item": f"{inventory.inventory_slots[6]['slot_item']}","amound": inventory.inventory_slots[6]["amound"], "distance_to_item_y": 0,"distance_to_item_x": 0}
                    inventory.inventory_slots[6]["slot_item"] = "empty"
                if width / 2 - 375 < mouse_x < width / 2 - 375 + 64 and height / 2 < mouse_y < height / 2 + 64 and inventory.inventory_slots[7] != "empty":
                    inventory.mouse_item = {"last_slot_idx": 7,"slot_item": f"{inventory.inventory_slots[7]['slot_item']}","amound": inventory.inventory_slots[7]["amound"], "distance_to_item_y": 0,"distance_to_item_x": 0}
                    inventory.inventory_slots[7]["slot_item"] = "empty"
                if width / 2 - 290 < mouse_x < width / 2 - 290 + 64 and height / 2 < mouse_y < height / 2 + 64 and inventory.inventory_slots[8] != "empty":
                    inventory.mouse_item = {"last_slot_idx": 8,"slot_item": f"{inventory.inventory_slots[8]['slot_item']}","amound": inventory.inventory_slots[8]["amound"], "distance_to_item_y": 0,"distance_to_item_x": 0}
                    inventory.inventory_slots[8]["slot_item"] = "empty"
                if width / 2 - 210 < mouse_x < width / 2 - 210 + 64 and height / 2 < mouse_y < height / 2 + 64 and inventory.inventory_slots[9] != "empty":
                    inventory.mouse_item = {"last_slot_idx": 9,"slot_item": f"{inventory.inventory_slots[9]['slot_item']}","amound": inventory.inventory_slots[9]["amound"], "distance_to_item_y": 0,"distance_to_item_x": 0}
                    inventory.inventory_slots[9]["slot_item"] = "empty"
                if width / 2 - 120 < mouse_x < width / 2 - 120 + 64 and height / 2 < mouse_y < height / 2 + 64 and inventory.inventory_slots[10] != "empty":
                    inventory.mouse_item = {"last_slot_idx": 10,"slot_item": f"{inventory.inventory_slots[10]['slot_item']}","amound": inventory.inventory_slots[10]["amound"], "distance_to_item_y": 0,"distance_to_item_x": 0}
                    inventory.inventory_slots[10]["slot_item"] = "empty"
                if width / 2 - 460 < mouse_x < width / 2 - 460 + 64 and height / 2 + 80 < mouse_y < height / 2 + 80 + 64 and inventory.inventory_slots[11] != "empty":
                    inventory.mouse_item = {"last_slot_idx": 11,"slot_item": f"{inventory.inventory_slots[11]['slot_item']}","amound": inventory.inventory_slots[11]["amound"], "distance_to_item_y": 0,"distance_to_item_x": 0}
                    inventory.inventory_slots[11]["slot_item"] = "empty"
                if width / 2 - 375 < mouse_x < width / 2 - 375 + 64 and height / 2 + 80 < mouse_y < height / 2 + 80 + 64 and inventory.inventory_slots[12] != "empty":
                    inventory.mouse_item = {"last_slot_idx": 12,"slot_item": f"{inventory.inventory_slots[12]['slot_item']}","amound": inventory.inventory_slots[12]["amound"], "distance_to_item_y": 0,"distance_to_item_x": 0}
                    inventory.inventory_slots[12]["slot_item"] = "empty"
                if width / 2 - 290 < mouse_x < width / 2 - 290 + 64 and height / 2 + 80 < mouse_y < height / 2 + 80 + 64 and inventory.inventory_slots[13] != "empty":
                    inventory.mouse_item = {"last_slot_idx": 13,"slot_item": f"{inventory.inventory_slots[13]['slot_item']}","amound": inventory.inventory_slots[13]["amound"], "distance_to_item_y": 0,"distance_to_item_x": 0}
                    inventory.inventory_slots[13]["slot_item"] = "empty"
                if width / 2 - 210 < mouse_x < width / 2 - 210 + 64 and height / 2 + 80 < mouse_y < height / 2 + 80 + 64 and inventory.inventory_slots[14] != "empty":
                    inventory.mouse_item = {"last_slot_idx": 14,"slot_item": f"{inventory.inventory_slots[14]['slot_item']}","amound": inventory.inventory_slots[14]["amound"], "distance_to_item_y": 0,"distance_to_item_x": 0}
                    inventory.inventory_slots[14]["slot_item"] = "empty"
                if width / 2 - 120 < mouse_x < width / 2 - 120 + 64 and height / 2 + 80 < mouse_y < height / 2 + 80 + 64 and inventory.inventory_slots[15] != "empty":
                    inventory.mouse_item = {"last_slot_idx": 15,"slot_item": f"{inventory.inventory_slots[15]['slot_item']}","amound": inventory.inventory_slots[15]["amound"], "distance_to_item_y": 0,"distance_to_item_x": 0}
                    inventory.inventory_slots[15]["slot_item"] = "empty"

            #displays the current hold item
            if inventory.mouse_item["slot_item"] != "empty":
                x, y = mouse_x - inventory.mouse_item["distance_to_item_x"], mouse_y - inventory.mouse_item["distance_to_item_y"]
                if inventory.mouse_item["slot_item"] == "leather bottle":
                    screen.blit(inventory.slotitems_images[0], (x, y))
                elif inventory.mouse_item["slot_item"] == "campfire":
                    screen.blit(inventory.slotitems_images[1], (x, y))
                elif inventory.mouse_item["slot_item"] == "cap":
                    screen.blit(inventory.slotitems_images[2], (x, y))
                elif inventory.mouse_item["slot_item"] == "jacket":
                    screen.blit(inventory.slotitems_images[3], (x, y))
                elif inventory.mouse_item["slot_item"] == "leggins":
                    screen.blit(inventory.slotitems_images[4], (x, y))
                elif inventory.mouse_item["slot_item"] == "boots":
                    screen.blit(inventory.slotitems_images[5], (x, y))
                elif inventory.mouse_item["slot_item"] == "raft tile":
                    screen.blit(inventory.slotitems_images[6], (x, y))
                elif inventory.mouse_item["slot_item"] == "fishing rod":
                    screen.blit(inventory.slotitems_images[7], (x, y))
                elif inventory.mouse_item["slot_item"] == "hook":
                    screen.blit(inventory.slotitems_images[8], (x, y))
                elif inventory.mouse_item["slot_item"] == "hook LV1":
                    screen.blit(inventory.slotitems_images[9], (x, y))
                elif inventory.mouse_item["slot_item"] == "hook LV2":
                    screen.blit(inventory.slotitems_images[10], (x, y))
                elif inventory.mouse_item["slot_item"] == "hook MAX":
                    screen.blit(inventory.slotitems_images[11], (x, y))
                elif inventory.mouse_item["slot_item"] == "raw fish":
                    screen.blit(inventory.slotitems_images[12], (x, y))
                elif inventory.mouse_item["slot_item"] == "cooked fish":
                    screen.blit(inventory.slotitems_images[13], (x, y))
                elif inventory.mouse_item["slot_item"] == "smored fish":
                    screen.blit(inventory.slotitems_images[14], (x, y))

            # Item hinlegen
            if left_lift and inventory.mouse_item["slot_item"] != "empty":
                if width / 2 - 480 < mouse_x < width / 2 - 480 + 64 and height / 2 - 260 < mouse_y < height / 2 - 260 + 64 and (inventory.inventory_slots[0]["slot_item"] == inventory.mouse_item["slot_item"] or inventory.inventory_slots[0]["slot_item"] == "empty" and inventory.mouse_item["slot_item"] == "cap"):
                    inventory.putdownitem(0)
                elif width / 2 - 395 < mouse_x < width / 2 - 395 + 64 and height / 2 - 260 < mouse_y < height / 2 - 260 + 64 and (inventory.inventory_slots[1]["slot_item"] == inventory.mouse_item["slot_item"] or inventory.inventory_slots[1]["slot_item"] == "empty" and inventory.mouse_item["slot_item"] == "jacket"):
                    inventory.putdownitem(1)
                elif width / 2 - 225 < mouse_x < width / 2 - 225 + 64 and height / 2 - 260 < mouse_y < height / 2 - 260 + 64 and (inventory.inventory_slots[2]["slot_item"] == inventory.mouse_item["slot_item"] or inventory.inventory_slots[2]["slot_item"] == "empty" and inventory.mouse_item["slot_item"] == "boots"):
                    inventory.putdownitem(2)
                elif width / 2 - 310 < mouse_x < width / 2 - 310 + 64 and height / 2 - 260 < mouse_y < height / 2 - 260 + 64 and (inventory.inventory_slots[3]["slot_item"] == inventory.mouse_item["slot_item"] or inventory.inventory_slots[3]["slot_item"] == "empty" and inventory.mouse_item["slot_item"] == "leggins"):
                    inventory.putdownitem(3)
                elif width / 2 - 405 < mouse_x < width / 2 - 405 + 64 and height / 2 - 133 < mouse_y < height / 2 - 133 + 64 and (inventory.inventory_slots[4]["slot_item"] == inventory.mouse_item["slot_item"] or inventory.inventory_slots[4]["slot_item"] == "empty"):
                    inventory.putdownitem(4)
                elif width / 2 - 115 < mouse_x < width / 2 - 115 + 64 and height / 2 - 260 < mouse_y < height / 2 - 260 + 64 and (inventory.inventory_slots[5]["slot_item"] == inventory.mouse_item["slot_item"] or inventory.inventory_slots[5]["slot_item"] == "empty"):
                    inventory.putdownitem(5)
                elif width / 2 - 460 < mouse_x < width / 2 - 460 + 64 and height / 2 < mouse_y < height / 2 + 64 and (inventory.inventory_slots[6]["slot_item"] == inventory.mouse_item["slot_item"] or inventory.inventory_slots[6]["slot_item"] == "empty"):
                    inventory.putdownitem(6)
                elif width / 2 - 375 < mouse_x < width / 2 - 375 + 64 and height / 2 < mouse_y < height / 2 + 64 and (inventory.inventory_slots[7]["slot_item"] == inventory.mouse_item["slot_item"] or inventory.inventory_slots[7]["slot_item"] == "empty"):
                    inventory.putdownitem(7)
                elif width / 2 - 290 < mouse_x < width / 2 - 290 + 64 and height / 2 < mouse_y < height / 2 + 64 and (inventory.inventory_slots[8]["slot_item"] == inventory.mouse_item["slot_item"] or inventory.inventory_slots[8]["slot_item"] == "empty"):
                    inventory.putdownitem(8)
                elif width / 2 - 210 < mouse_x < width / 2 - 210 + 64 and height / 2 < mouse_y < height / 2 + 64 and (inventory.inventory_slots[9]["slot_item"] == inventory.mouse_item["slot_item"] or inventory.inventory_slots[9]["slot_item"] == "empty"):
                    inventory.putdownitem(9)
                elif width / 2 - 120 < mouse_x < width / 2 - 120 + 64 and height / 2 < mouse_y < height / 2 + 64 and (inventory.inventory_slots[10]["slot_item"] == inventory.mouse_item["slot_item"] or inventory.inventory_slots[10]["slot_item"] == "empty"):
                    inventory.putdownitem(10)
                elif width / 2 - 460 < mouse_x < width / 2 - 460 + 64 and height / 2 + 80 < mouse_y < height / 2 + 80 + 64 and (inventory.inventory_slots[11]["slot_item"] == inventory.mouse_item["slot_item"] or inventory.inventory_slots[11]["slot_item"] == "empty"):
                    inventory.putdownitem(11)
                elif width / 2 - 375 < mouse_x < width / 2 - 375 + 64 and height / 2 + 80 < mouse_y < height / 2 + 80 + 64 and (inventory.inventory_slots[12]["slot_item"] == inventory.mouse_item["slot_item"] or inventory.inventory_slots[12]["slot_item"] == "empty"):
                    inventory.putdownitem(12)
                elif width / 2 - 290 < mouse_x < width / 2 - 290 + 64 and height / 2 + 80 < mouse_y < height / 2 + 80 + 64 and (inventory.inventory_slots[13]["slot_item"] == inventory.mouse_item["slot_item"] or inventory.inventory_slots[13]["slot_item"] == "empty"):
                    inventory.putdownitem(13)
                elif width / 2 - 210 < mouse_x < width / 2 - 210 + 64 and height / 2 + 80 < mouse_y < height / 2 + 80 + 64 and (inventory.inventory_slots[14]["slot_item"] == inventory.mouse_item["slot_item"] or inventory.inventory_slots[14]["slot_item"] == "empty"):
                    inventory.putdownitem(14)
                elif width / 2 - 120 < mouse_x < width / 2 - 120 + 64 and height / 2 + 80 < mouse_y < height / 2 + 80 + 64 and (inventory.inventory_slots[15]["slot_item"] == inventory.mouse_item["slot_item"] or inventory.inventory_slots[15]["slot_item"] == "empty"):
                    inventory.putdownitem(15)

                # delete items
                elif width / 2 - 110 < mouse_x < width / 2 - 110 + 64 and height / 2 + 175 < mouse_y < height / 2 + 175 + 80:
                    inventory.deletesound.play()
                    inventory.mouse_item = {"last_slot_idx":0, "slot_item": "empty", "amound":0, "description":"", "distance_to_item_y":0, "distance_to_item_x":0}


            """pygame.draw.rect(screen, "red", (width / 2 - 480, height / 2 - 260, 64, 64))
            pygame.draw.rect(screen, "red", (width / 2 - 395, height / 2 - 260, 64, 64))
            pygame.draw.rect(screen, "red", (width / 2 - 310, height / 2 - 260, 64, 64))
            pygame.draw.rect(screen, "red", (width / 2 - 225, height / 2 - 260, 64, 64))
            pygame.draw.rect(screen, "red", (width / 2 - 115, height / 2 - 260, 64, 64))

            pygame.draw.rect(screen, "red", (width / 2 - 405, height / 2 - 133, 64, 64))


            pygame.draw.rect(screen, "red", (width / 2 - 460, height / 2, 64, 64))
            pygame.draw.rect(screen, "red", (width / 2 - 375, height / 2, 64, 64))
            pygame.draw.rect(screen, "red", (width / 2 - 290, height / 2, 64, 64))
            pygame.draw.rect(screen, "red", (width / 2 - 210, height / 2, 64, 64))
            pygame.draw.rect(screen, "red", (width / 2 - 210, height / 2, 64, 64))

            pygame.draw.rect(screen, "red", (width / 2 - 460, height / 2 + 80, 64, 64))
            pygame.draw.rect(screen, "red", (width / 2 - 375, height / 2 + 80, 64, 64))
            pygame.draw.rect(screen, "red", (width / 2 - 290, height / 2 + 80, 64, 64))
            pygame.draw.rect(screen, "red", (width / 2 - 210, height / 2 + 80, 64, 64))
            pygame.draw.rect(screen, "red", (width / 2 - 130, height / 2 + 80, 64, 64))"""




    @staticmethod
    def turn_page(left_click: bool, right_arrow: bool, left_arrow: bool, screen: object) -> None:
        """
        Parameters
        ----------
        right_arrow is pressed? [Button press]
        left_arrow is pressed?  [Button press]
        """
        if inventory.active:
            mous_x, mous_y = pygame.mouse.get_pos()
            width, height = screen.get_size()

            if width/2+415 < mous_x < width/2+545 and height / 2 +184 < mous_y < height / 2 +314 and left_click or right_arrow:
                inventory.turnpagesound.play()
                inventory.curent_page[0] += 1

            if width/2 - 535 < mous_x < width/2 - 405 and height / 2 + 184 < mous_y < height / 2 + 314 and left_click or left_arrow:
                inventory.turnpagesound.play()
                inventory.curent_page[0] -= 1

            if inventory.curent_page[0] < 0:
                inventory.curent_page[0] = 0
            elif inventory.curent_page[0] > inventory.curent_page[1]:
                inventory.curent_page[0] = inventory.curent_page[1]

    @staticmethod
    def draw_page(screen: pygame.Surface):
        """
        Zeichnet die actuelle Seite
        Parameters
        ----------
        screen der Screen wo das Invenar ausgegeben werden soll
        """
        if inventory.active:
            width, height = screen.get_size()
            if inventory.curent_page[0] == 0:
                screen.blit(inventory.page_1, (width / 2 -inventory.page_size[0] / 2, height / 2 - inventory.page_size[1]/2))
            elif inventory.curent_page[0] == 1:
                screen.blit(inventory.page_2,(width / 2 - inventory.page_size[0] / 2, height / 2 - inventory.page_size[1] / 2))
            elif inventory.curent_page[0] == 2:
                screen.blit(inventory.page_3,(width / 2 - inventory.page_size[0] / 2, height / 2 - inventory.page_size[1] / 2))
            elif inventory.curent_page[0] == 3:
                screen.blit(inventory.page_4,(width / 2 - inventory.page_size[0] / 2, height / 2 - inventory.page_size[1] / 2))


    @staticmethod
    def check_resources(resources, costs):
        """
        schaut ob man genug resourcen hat
        Parameters
        ----------
        resources
        costs

        Returns
        -------

        """
        wood_c = costs[0]
        string_c = costs[1]
        leather_c = costs[2]

        wood_a = resources[2]
        string_a = resources[1]
        leather_a = resources[0]

        if 0 <= wood_a - wood_c and 0 <= string_a - string_c and 0 <= leather_a - leather_c:
            return True
        else:
            return False

    @staticmethod
    def crafting(resources, costs, matrial):
        """
        crafting von verschiedenen objekten
        Parameters
        ----------
        resources
        costs
        matrial

        Returns
        -------

        """
        if inventory.check_resources(resources, [costs[0], costs[1], costs[2]]):
            for i in range(6, len(inventory.inventory_slots) - 1):
                if inventory.inventory_slots[i]["slot_item"] == "empty":
                    inventory.inventory_slots[i]["amound"] += 1
                    inventory.inventory_slots[i]["slot_item"] = matrial
                    resources[0] -= costs[1]
                    resources[1] -= costs[2]
                    resources[2] -= costs[0]
                    if matrial == "raw fish" or matrial == "smoked fish" or matrial == "cooked fish":
                        inventory.blob.play()
                    else:
                        inventory.craftsound.play()
                    return resources
                else:
                    inventory.deletesound.play()
        else:
            inventory.deletesound.play()
        return resources

    @staticmethod
    def check_and_delete_item(matrial):
        """
        deleted items zum craften
        Parameters
        ----------
        matrial

        Returns
        -------

        """
        for i in range(6, len(inventory.inventory_slots) - 1):
            if inventory.inventory_slots[i]["slot_item"] == matrial:
                if inventory.inventory_slots[i]["amound"] > 1:
                    inventory.inventory_slots[i]["amound"] -= 1
                else:
                    inventory.inventory_slots[i]["amound"] = 0
                    inventory.inventory_slots[i]["slot_item"] = "empty"
                return True
        return False

    @staticmethod
    def delete_unessasary_amounds():
        """
        bug fix
        """
        for i in range(0, 16):
            if inventory.inventory_slots[i]["slot_item"] == "empty" or inventory.inventory_slots[i]["amound"] == 0:
                inventory.inventory_slots[i]["amound"] = 0
                inventory.inventory_slots[i]["slot_item"] = "empty"

    @staticmethod
    def page_3_4_crafting(screen, resources, left_click):
        """
        crafting seiten
        Parameters
        ----------
        screen
        resources
        left_click

        Returns
        -------

        """
        inventory.delete_unessasary_amounds()
        if inventory.curent_page[0] == 2 and inventory.active:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            width, height = screen.get_size()
            if width / 2 - 60 < mouse_x < width / 2 - 60 + 50 and height / 2 - 140 < mouse_y < height / 2 - 140 + 50 and left_click:
                resources = inventory.crafting(resources, [0, 5, 5], "hook")
            elif width / 2 - 60 < mouse_x < width / 2 - 60 + 50 and height / 2 - 16 < mouse_y < height / 2 - 16 + 50 and left_click:
                if inventory.check_and_delete_item("hook"):
                    resources = inventory.crafting(resources, [0, 0, 10], "hook LV1")
            elif width / 2 - 55 < mouse_x < width / 2 - 55 + 50 and height / 2 + 98 < mouse_y < height / 2 + 98 + 50 and left_click:
                if inventory.check_and_delete_item("hook LV1"):
                    resources = inventory.crafting(resources, [0, 0, 50], "hook LV2")
            elif width / 2 - 60 < mouse_x < width / 2 - 60 + 50 and height / 2 + 222 < mouse_y < height / 2 + 222 + 50 and left_click:
                if inventory.check_and_delete_item("hook LV2"):
                    resources = inventory.crafting(resources, [100, 0, 0], "hook MAX")
            elif width / 2 + 420 < mouse_x < width / 2 + 420 + 50 and height / 2 - 225 < mouse_y < height / 2 - 225 + 50 and left_click:
                resources = inventory.crafting(resources, [0, 25, 5], "cap")
            elif width / 2 + 420 < mouse_x < width / 2 + 420 + 50 and height / 2 - 135 < mouse_y < height / 2 - 135 + 50 and left_click:
                resources = inventory.crafting(resources, [0, 40, 5], "jacket")
            elif width / 2 + 420 < mouse_x < width / 2 + 420 + 50 and height / 2 - 20 < mouse_y < height / 2 - 20 + 50 and left_click:
                resources = inventory.crafting(resources, [0, 30, 5], "leggins")
            elif width / 2 + 420 < mouse_x < width / 2 + 420 + 50 and height / 2 + 95 < mouse_y < height / 2 + 95 + 50 and left_click:
                resources = inventory.crafting(resources, [0, 20, 5], "boots")
            elif width / 2 + 420 < mouse_x < width / 2 + 420 + 50 and height / 2 + 137 < mouse_y < height / 2 + 137 + 50 and left_click:
                resources = inventory.crafting(resources, [0, 5, 5], "leather bottle")




            #pygame.draw.rect(screen, "red", (screen_width / 2 - 60, screen_height / 2 - 140 , 50, 50))
            #pygame.draw.rect(screen, "red", (screen_width / 2 - 60, screen_height / 2 - 16 , 50, 50))
            #pygame.draw.rect(screen, "red", (screen_width / 2 - 55, screen_height / 2 + 98 , 50, 50))
            #pygame.draw.rect(screen, "red", (screen_width / 2 - 55, screen_height / 2 + 222 , 50, 50))

            #pygame.draw.rect(screen, "red", (screen_width / 2 + 420, screen_height / 2 - 225 , 50, 50))
            #pygame.draw.rect(screen, "red", (screen_width / 2 + 420, screen_height / 2 - 135 , 50, 50))
            #pygame.draw.rect(screen, "red", (screen_width / 2 + 420, screen_height / 2 - 20 , 50, 50))
            #pygame.draw.rect(screen, "red", (screen_width / 2 + 420, screen_height / 2 + 95 , 50, 50))
            #pygame.draw.rect(screen, "red", (screen_width / 2 + 420, screen_height / 2 + 137, 50, 50))

        if inventory.curent_page[0] == 3 and inventory.active:
            width, height = screen.get_size()
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if width / 2 - 75 < mouse_x < width / 2 - 75 + 50 and height / 2 - 200 < mouse_y < height / 2 - 200 + 50 and left_click:
                resources = inventory.crafting(resources, [5, 0, 10], "fishing rod")
            elif width / 2 - 75 < mouse_x < width / 2 - 75 + 50 and height / 2 - 76 < mouse_y < height / 2 - 76 + 50 and left_click:
                resources = inventory.crafting(resources, [10, 0, 0], "raft tile")
            elif width / 2 - 75 < mouse_x < width / 2 - 75 + 50 and height / 2 + 38 < mouse_y < height / 2 + 38 + 50 and left_click:
                resources = inventory.crafting(resources, [25, 0, 0], "campfire")
        return resources
            #pygame.draw.rect(screen, "red", (screen_width / 2 - 75, screen_height / 2 - 200 , 50, 50))
            #pygame.draw.rect(screen, "red", (screen_width / 2 - 75, screen_height / 2 - 76 , 50, 50))
            #pygame.draw.rect(screen, "red", (screen_width / 2 - 75, screen_height / 2 + 38 , 50, 50))
