import pygame

class Nave:
    def __init__(self, imagem_path, largura, altura):
        try:
            self.imagem_original = pygame.image.load(imagem_path)
        except pygame.error as e:
            print(f'Erro ao carregar a imagem: {e}')
            raise


        self.imagem = pygame.transform.scale(self.imagem_original, (70, 50))
        
        # Define a posição da nave, centralizando horizontalmente e ajustando a posição vertical
        self.rect = self.imagem.get_rect()
        self.rect.x = (largura - self.imagem.get_width()) // 2     # Centraliza a nave
        self.rect.y = altura - self.imagem.get_height()            # Ajusta a posição Vertical

        #print(f"Altura da nave: {self.imagem.get_height()}, Posição da nave: {self.rect.topleft}, Altura da tela: {altura}")
        #print(f"Nave centralizada na posição: {self.rect.x}, Altura: {self.rect.y}")

        self.velocidade = 3   # velocidade da nave
        

    def mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidade  


         # Mantém a nave dentro dos limites da tela
        if self.rect.left < -15:
            self.rect.left = -15
        if self.rect.right > pygame.display.get_surface().get_width() + 15:
            self.rect.right = pygame.display.get_surface().get_width() + 15     


    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect)        