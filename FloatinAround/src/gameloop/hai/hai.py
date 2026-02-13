import pygame
import math
import random
from gameloop.raft_and_building_layer.raft import raft
from gameloop.raft_and_building_layer.building import Building

## KI Anfang ##
## KI: Microsoft Copilot ##
## Prompt: startidee für hai ##
class Shark(pygame.sprite.Sprite):
    screen = pygame.display.set_mode()

    def __init__(self, center_x, center_y, radius):
        super().__init__()
        self.image = pygame.image.load("assets/hai_assets/flosse.png").convert_alpha()
        self.image = self.image.subsurface(0,0, 64, 64)
        self.image2 = pygame.image.load("assets/hai_assets/flosse.png").convert_alpha()
        self.image2 = self.image2.subsurface(64, 0, 64, 64)

        self.rect = self.image.get_rect()

        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.angle = 0

        self.attacking = False
        self.attack_timer = random.randint(200, 4000)  # Zufälliges Intervall für Angriff
        self.speed = 0.01


    def update(self):
        """
        updatet den hai und siene pos
        """
        if self.attacking:
            # Direkt auf das Floß zusteuern

            direction_x = self.center_x - self.rect.x
            direction_y = self.center_y - self.rect.y


            length = math.hypot(direction_x, direction_y)
            if length > 10:  # Stoppt den Angriff, wenn der Hai nahe genug ist
                self.rect.x += direction_x / length * 2  # Angriffsgeschwindigkeit
                self.rect.y += direction_y / length * 2
                raft.delete_raft_by_cords(self.rect.x + 32, self.rect.y + 32)
                Building.delete_building_by_cords(self.rect.x + 32, self.rect.y + 32)

            else:
                self.attacking = False

                self.attack_timer = random.randint(200, 4000)  # Reset des Angriffs
        else:
            # Kreisbewegung um das Floß
            self.angle += self.speed
            self.rect.x = self.center_x + self.radius * math.cos(self.angle)
            self.rect.y = self.center_y + self.radius * math.sin(self.angle)
            self.attack_timer -= 1
            if self.attack_timer <= 0:
                self.attacking = True  # Angriff starten


            t = random.uniform(0.3, 1.0)  # 0.0 = Floßmitte, 1.0 = aktueller Kreisrandpunkt
            self.target_x = self.center_x * (1 - t) + self.rect.x * t
            self.target_y = self.center_y * (1 - t) + self.rect.y * t

screen_width, screen_height = 1568, 868
raft_x, raft_y = screen_width / 2, screen_height / 2
shark = Shark(screen_width / 2, screen_height / 2, 400)
shark_group = pygame.sprite.Group(shark)

## KI Ende ##