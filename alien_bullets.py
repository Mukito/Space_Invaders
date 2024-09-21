import pygame

class Alien_Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("imagens/aliens/alien_bullet.png")
        self.image = pygame.transform.scale(self.image, (10, 20))  # Ajuste o tamanho conforme necessário
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y += 2  # Mova os tiros para baixo
        if self.rect.top > pygame.display.get_surface().get_height():
            self.kill()
