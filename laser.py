import pygame
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, speed, screen_height, color=(255, 255, 0), size=(4,20)):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color)                              # Preenche a superficie com a cor amarela
        self.rect = self.image.get_rect(center = pos)
        self.speed = speed
        self.height_y_constraint = screen_height

    def check_bounds(self):
        #verifica se o laser saiu da tela
        if self.rect.y <= -50 or self.rect.y >= self.height_y_constraint + 50:
            self.kill()             # print("Laser saiu pela parte superior")

    def update(self):
        self.rect.y += self.speed   # move o laser
        self.check_bounds()         # Verifica se deve ser destruido    