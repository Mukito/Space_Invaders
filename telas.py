import pygame
from nave import Nave    # Importa a classe Nave

class TelaPrincipal:
    def __init__(self):
        self.Largura = 800
        self.Altura = 600
        self.tela = pygame.display.set_mode((self.Altura, self.Largura))
        pygame.display.set_caption('Principal')
        self.fundo = pygame.image.load('imagens/cenario/bg.png')
        self.nave = Nave('imagens/nave/nave2.png', self.Largura, self.Altura)

        
    def run(self):
        loop = True
        while loop:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    loop = False


            # Captura as teclas pressionadas
            teclas = pygame.key.get_pressed()
            self.nave.mover(teclas)   # Move a nave com base nas teclas pressionadas

            # Desenha a imagem de fundo
            self.tela.blit(self.fundo, (0, 0))
            # Desenha a imagem da nave
            self.nave.desenhar(self.tela)

            # Atualiza a tela
            pygame.display.flip()        