import pygame
import random

class Aliens(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #super().__init__()
        self.image = pygame.image.load("imagens/aliens/nivel_1/harlien" + str(random.randint(1, 4)) + ".png")
        #self.image = pygame.image.load('imagens/aliens/nivel_2/alien' + str(random.randint(1, 5)) + ".png")
        self.image = pygame.transform.scale(self.image, (50, 50))  # Ajuste o tamanho conforme necessário
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.move_counter = 0
        self.move_direction = 1

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 75:
            self.move_direction *= -1
            self.move_counter *= self.move_direction
            

			#imagens/cenario/bg.png
