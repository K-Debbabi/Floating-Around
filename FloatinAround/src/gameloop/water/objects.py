from lib2to3.pygram import python_grammar_no_print_and_exec_statement

import pygame
import random


class object():
    ticks_between_spawning = 2000
    spawning_rate = 30
    last_timestamp = 0
    object_list = []
    OBJ_TILESIZE = 64
    floating_wood_image = pygame.Surface
    floating_leather_image = pygame.Surface
    floating_rope_image = pygame.Surface
    FLOATING_SPEED = 4
    pickup = ...

    @staticmethod
    def init():
        object.floating_wood_image = pygame.image.load("assets/water_assets/wood_floating.png").convert_alpha()
        object.floating_leather_image = pygame.image.load("assets/water_assets/leather_floating.png").convert_alpha()
        object.floating_rope_image = pygame.image.load("assets/water_assets/rope_floating.png").convert_alpha()
        object.pickup = pygame.mixer.Sound("assets/sounds/pickup.mp3")
        object.pickup.set_volume(1)


    @staticmethod
    def create(screen_height):
        timestamp = pygame.time.get_ticks()
        if timestamp - object.last_timestamp > object.ticks_between_spawning:
            if random.randint(0,100) > object.spawning_rate:
                what_object = random.randint(1, 3)
                if what_object == 1:
                    new_object = {
                        "material": 1,
                        "pos":(-object.OBJ_TILESIZE, random.randint(0, screen_height)),
                        }
                elif what_object == 2:
                    new_object = {
                        "material": 2,
                        "pos": (-object.OBJ_TILESIZE, random.randint(0, screen_height)),
                        }
                elif what_object == 3:
                    new_object = {
                        "material": 3,
                        "pos": (-object.OBJ_TILESIZE, random.randint(0, screen_height)),
                    }
                object.object_list.append(new_object)
            object.last_timestamp = timestamp


    @staticmethod
    def move(screen_width):
        for i, floater in enumerate(reversed(object.object_list)):
            floater["pos"] = (floater["pos"][0] + object.FLOATING_SPEED, floater["pos"][1])
            if floater["pos"][0] > screen_width:
                object.object_list.remove(floater)

    @staticmethod
    def draw(screen):
        for floater in object.object_list:
            if floater["material"] == 1:
                screen.blit(object.floating_wood_image, floater["pos"])
            elif floater["material"] == 2:
                screen.blit(object.floating_leather_image, floater["pos"])
            elif floater["material"] == 3:
                screen.blit(object.floating_rope_image, floater["pos"])

#mein code
    """@staticmethod
    def put_resources_into_inv(pos_x, pos_y, radius):
        added_resources = [0, 0, 0]
        for i in reversed(range(len(object.object_list))):
            if pos_x - radius < object.object_list[i]["pos"][0] + 32 < pos_x + radius and pos_y - radius < object.object_list[i]["pos"][0] + 32 < pos_y + radius and object.object_list[i]["material"] == 1:
                added_resources[0] += 1
                object.object_list.pop(i)
            elif pos_x - radius < object.object_list[i]["pos"][0] + 32 < pos_x + radius and pos_y - radius < object.object_list[i]["pos"][0] + 32 < pos_y + radius and object.object_list[i]["material"] == 2:
                added_resources[1] += 1
                object.object_list.pop(i)
            elif pos_x - radius < object.object_list[i]["pos"][0] + 32 < pos_x + radius and pos_y - radius < object.object_list[i]["pos"][0]  +32 < pos_y + radius and object.object_list[i]["material"] == 3:
                added_resources[2] += 1
                object.object_list.pop(i)
        return added_resources"""

#von ChatGPT verbesserter code irgendwas habe ich flasch gemacht das die Hitbox vom hacken nicht über eingestimmt hat
#prompt fixe mir den oberigen code (der nicht geklappt hat)
#ChatGPT anfang
    def put_resources_into_inv(pos_x, pos_y, radius):
        added_resources = [0, 0, 0]
        for i in reversed(range(len(object.object_list))):
            if pos_x - radius < object.object_list[i]["pos"][0] < pos_x + radius and pos_y - radius < object.object_list[i]["pos"][1] < pos_y + radius and object.object_list[i]["material"] == 1:
                added_resources[2] += 1
                object.object_list.pop(i)
                object.pickup.play()
            elif pos_x - radius < object.object_list[i]["pos"][0] < pos_x + radius and pos_y - radius < object.object_list[i]["pos"][1] < pos_y + radius and object.object_list[i]["material"] == 2:
                added_resources[0] += 1
                object.object_list.pop(i)
                object.pickup.play()
            elif pos_x - radius < object.object_list[i]["pos"][0] < pos_x + radius and pos_y - radius < object.object_list[i]["pos"][1] < pos_y + radius and object.object_list[i]["material"] == 3:
                added_resources[1] += 1
                object.object_list.pop(i)
                object.pickup.play()
        return added_resources
# ChatGPT Ende