import pygame

class Nave:
    def __init__(self, imagem_path, largura, altura):
        self.imagem_original = pygame.image.load(imagem_path)
        self.imagem = pygame.transform.scale(self.imagem_original, (70, 50))

        #self.rect = self.imagem.get_rect(center=(largura // 2, altura - 1))   # 1 pixels acima da borda inferior  
        self.rect = self.imagem.get_rect(center=(largura // 2, altura * 1.2))
        #self.rect.center = [x, y]
        self.velocidade = 0.8   # velocidade da nave
        

    def mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidade


         # Mantém a nave dentro dos limites da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > pygame.display.get_surface().get_width():
            self.rect.right = pygame.display.get_surface().get_width()     


    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect)        