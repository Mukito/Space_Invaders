import pygame

class Nave:
    def __init__(self, imagem_path, largura, altura):
        """
        Inicializa a nave.

        :param imagem_path: Caminho para a imagem da nave.
        :param largura: Largura da tela do jogo.
        :param altura: Altura da tela do jogo.
        """
        try:
            self.imagem_original = pygame.image.load(imagem_path)
        except pygame.error as e:
            print(f'Erro ao carregar a imagem: {e}')
            raise

        self.imagem = pygame.transform.scale(self.imagem_original, (70, 50))
        # Define a posição da nave, centralizando horizontalmente e ajustando a posição vertical
        self.rect = self.imagem.get_rect()
        self.rect.x = (largura - self.imagem.get_width()) // 2  # Centraliza a nave
        self.rect.y = altura - self.imagem.get_height()  # Ajusta a posição vertical
        
        self.velocidade = 3  # Velocidade da nave
        self.vida = 3    # Atributo de Vida


    def mover(self, teclas):
        """Move a nave com base nas teclas pressionadas."""
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidade  

        # Mantém a nave dentro dos limites da tela
        if self.rect.left < 0:  # Ajustado para 0 em vez de -15
            self.rect.left = 0
        if self.rect.right > pygame.display.get_surface().get_width():  # Ajustado para não ultrapassar a tela
            self.rect.right = pygame.display.get_surface().get_width()

    def desenhar(self, tela):
        """Desenha a nave na tela."""
        tela.blit(self.imagem, self.rect)

    def desenhar_vida(self, tela):
        """Desenha a barra de vida na tela."""
        largura_barra = 50
        altura_barra = 10
        for i in range(self.vida):
            pygame.draw.rect(tela, (0, 255, 0), (10 + i * (largura_barra + 5), 10, largura_barra, altura_barra))
        cor_barra = (255, 0, 0)  # Vermelho
        cor_fundo = (0, 0, 0)    # Preto


        # Desenha fundo da barra
        pygame.draw.rect(tela, cor_fundo, (10, 50, largura_barra, altura_barra))
        # Calcula a largura da vida restante
        largura_atual = largura_barra * (self.vida / 3)
        # Desenha a barra de vida
        pygame.draw.rect(tela, cor_barra, (10, 50, largura_atual, altura_barra))
