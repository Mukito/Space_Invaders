import pygame
from telas import TelaPrincipal


def main():
    pygame.init()
    tela = TelaPrincipal()
    tela.run()
    pygame.quit()


if __name__ == "__main__":
    main()









# =========================================================segunda tentativa===============================================================

# Inicializa o Pygame
#pygame.init()

# Variavel display chamando a biblioteca que fala apenas da resolução com (Largura, Altura)
#Largura = 600
#Altura = 800
#tela = pygame.display.set_mode((Largura, Altura))

# Carrega a imagem de Fundo
#cenario = pygame.image.load('imagens/cenario/bg.png')

# Loop principal
#loop = True

#while loop:
#    for evento in pygame.event.get():
#        if evento.type == pygame.QUIT:
#            loop = False
#            pygame.quit()
#            sys.exit()

    #desenha a tela com a imagem
#    tela.blit(cenario, (0, 0))


    # Atualiza a tela
#    pygame.display.flip()


#=========================================================== youtube tem no Bloco de notas ======================================================
#Caption and Icon
#pygame.display.set_caption('MukitoBR')
#icon = pygame.image.load('imagens/icon/spaceship.png')
#pygame.display.set_icon(icon)

#variavel display chamando a biblioteca que fala apenas da resolução com (Largura, Altura)
#Largura = 600
#Altura = 800
#display = pygame.display.set_mode((Largura, Altura))

#cria-se um loop par continuar a tela 
#loop =True
#while loop:

    #lista de eventos (aperta a tecla, arrasta o mouse, etc...)
#    for event in pygame.event.get():
        #Fechamento do loop (QUIT)
#        if event.type == pygame.QUIT:
            #Caso eu aperte o X do QUIT o loop passa ser False e é encerrado
#            loop = False

#        if event.type == pygame.KEYDOWN:
#            if event.key == pygame.K_a:
#                loop = False

    #função fill que preenche a cor
    #display.fill('BLACK')
    #load image
#    bg = pygame.image.load('imagens/cenario/bg.png')
#    pygame.display.flip(bg):