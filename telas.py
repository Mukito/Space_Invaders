import pygame
import random
from nave import Nave    
from laser import Laser
from alien import Aliens
from alien_bullets import Alien_Bullets


class TelaPrincipal:
    def __init__(self):
        self.Largura = 600
        self.Altura = 800
        self.tela = pygame.display.set_mode((self.Largura, self.Altura))
        pygame.display.set_caption('Space Invanders')
        try:
            self.fundo = pygame.image.load('imagens/cenario/bg.png')
        except Exception as e:
            print(f'Erro ao carregar fundo: {e}')
            raise


        self.nave = Nave('imagens/nave/nave2.png', self.Largura, self.Altura)

        # Variaveis do jogo
        self.score = 0                                  # Inicia a Pontuação
        self.lasers = pygame.sprite.Group()             # Grupo para armazenar os lazers
        self.aliens = pygame.sprite.Group()             # Grupo para Aliens
        self.aliens_bullets = pygame.sprite.Group()     # Grupo para Bala dos Aliens
        self.clock = pygame.time.Clock()

        # Variaveis para Controle de alienigenas 
        self.rows = 5
        self.cols = 5
        self.alien_cooldown = 1000                      #bullet cooldown em millisegundos
        self.last_alien_shot = pygame.time.get_ticks()
        
        self.countdown = 3
        self.last_count = pygame.time.get_ticks()

        # Cria Alieniginas
        self.create_aliens()

    #================================Audio============================================
        pygame.mixer.init()
        self.som_tiro = pygame.mixer.Sound('Audio/Audio_Laser.wav')
        self.som_tiro.set_volume(0.25) # seta o volume do tiro  
    #=================================================================================

# ====================================================================================================
    def create_aliens(self):
        #generate aliens
        for row in range(self.rows):
            for item in range(self.cols):
                alien = Aliens(100 + item * 100, 100 + row * 70)
                self.aliens.add(alien)                          
# =====================================================================================================                   

        #print(f"Altura da nave: {self.nave.rect.height}, Altura da tela: {self.Altura}")
        
        
    def run(self):
        loop = True
        while loop:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    loop = False

             
                # Dispara um laser quando a tecla "espaço" é pressionada
                if evento.type == pygame.KEYDOWN:
                    #print(f"Nave posição: {self.nave.rect.topleft}")

                    if evento.key == pygame.K_SPACE:
                        #Posiçao do bico da nave
                        pos = (self.nave.rect.centerx, self.nave.rect.top - 20)  # Posição da nave
                        laser = Laser(pos, -10, self.Altura)  # Cria um laser (velocidade negativa para subir)
                        #print(f"Lazer criado na posição: {pos}")
                        self.lasers.add(laser)  # Adiciona o laser ao grupo
                        self.som_tiro.play()    #Toca o Som do tiro
                        self.score += 1         # Exemplo de incremento

            
            teclas = pygame.key.get_pressed()       # Captura as teclas pressionadas
            self.nave.mover(teclas)                 # Move a nave com base nas teclas pressionadas
            self.lasers.update()                    # Atualiza os lasers
            self.aliens.update()                    # Atualiza os Aliens
            self.aliens_bullets.update()            # Atualiza as balas dos Aliens

            current_time = pygame.time.get_ticks()
            if current_time - self.last_alien_shot >= self.alien_cooldown:
                if self.aliens:
                    alien = random.choice(self.aliens.sprites())
                    bullet = Alien_Bullets(alien.rect.centerx, alien.rect.bottom)
                    self.aliens_bullets.add(bullet)
                    self.last_alien_shot = current_time     # Atualiza o tempo do ultimo tiro
           
            self.tela.blit(self.fundo, (0, 0))     # Desenha a imagem de fundo 
            self.nave.desenhar(self.tela)          # Desenha a imagem da nave
            self.lasers.draw(self.tela)            # Desenha todos os lasers
            self.aliens.draw(self.tela)
            self.aliens_bullets.draw(self.tela)

            self.desenhar_score()                  # Chama o método para desenhar a pontuação
            
            pygame.display.flip()                  # Atualiza a tela
            self.clock.tick(60)                    #Limita a 60 quadros por segundos


    def desenhar_score(self):
        fonte = pygame.font.Font(None, 36)  # Fonte padrao 36
        texto = fonte.render(f'Score: {self.score}', True, (255, 255, 255))    # Texto Branco
        self.tela.blit(texto, (10, 10))    #Desenha o texto na posição (10, 10)


