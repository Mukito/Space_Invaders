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
        self.lasers = pygame.sprite.Group()
        
        # Definindo a cor de fundo
        self.cor_fundo = (0, 0, 0)  # Preto
        self.game_over = False

        self._inicializar_jogo()
        self.create_aliens()

    def _inicializar_jogo(self):
        """Inicializa o jogo e carrega os recursos."""
        icon = pygame.image.load('imagens/icon/spaceship.png')
        pygame.display.set_icon(icon)
        pygame.display.set_caption('Space Invaders')
        
        self.imagem_nave_vida = pygame.image.load('imagens/nave/nave2.png')
        self.imagem_nave_vida = pygame.transform.scale(self.imagem_nave_vida, (40, 25))  # Ajusta o tamanho 

        try:
            self.fundo = pygame.image.load('imagens/cenario/bg.png')
        except Exception as e:
            print(f'Erro ao carregar fundo: {e}')
            raise

        self.nave = Nave('imagens/nave/nave2.png', self.Largura, self.Altura)

        # Variáveis do jogo
        self.score = 0
        self.aliens = pygame.sprite.Group()
        self.aliens_bullets = pygame.sprite.Group()
        self.clock = pygame.time.Clock()

        # Variáveis para controle de alienígenas 
        self.rows = 5
        self.cols = 5
        self.alien_cooldown = 1000
        self.last_alien_shot = pygame.time.get_ticks()

        # Audio
        pygame.mixer.init()
        self.som_tiro = pygame.mixer.Sound('Audio/Audio_Laser.wav')
        self.som_tiro.set_volume(0.25)

    def create_aliens(self):
        """Cria os aliens no jogo."""
        largura_alien = 30
        espacamento_horizontal = 50
        espacamento_vertical = 50
        start_x = (self.Largura - (self.cols * largura_alien + (self.cols - 1) * espacamento_horizontal)) // 2
        for row in range(self.rows):
            for col in range(self.cols):
                x = start_x + col * (largura_alien + espacamento_horizontal)  # Posiciona os aliens
                y = 80 + row * (largura_alien + espacamento_vertical)  # Ajuste a altura conforme necessário
                alien = Aliens(x, y)
                self.aliens.add(alien)
                

    def move_all_aliens_down(self):
        for alien in self.aliens:
            alien.react.y += 10
            
    def run(self):
        loop = True
        while loop:
            
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    loop = False
                
                if self.game_over and evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_r:    #Pressione R para reiniciar
                        self.reiniciar_jogo()
                        self.game_over = False
                        print("Jogo reiniciado!")

                if not self.game_over and evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        if len(self.lasers) < 5:     #Limita a 5 lasers na tela
                            pos = (self.nave.rect.centerx, self.nave.rect.top - 20)
                            laser = Laser(pos, -10, self.Altura)
                            self.lasers.add(laser)
                            self.som_tiro.play()
                            self.score += 1
                        else:
                            print("Limite de Tiros atingido!")    

            if not self.game_over:
                teclas = pygame.key.get_pressed()
                self.nave.mover(teclas)
                self.lasers.update()
                self.aliens.update()
                self.aliens_bullets.update()

                if self.aliens:
                    if any(alien.rect.right >= self.Largura or alien.rect.left <= 0 for alien in self.aliens):
                        print("Aliens atingiram a parede")
                        self.move_all_aliens_down()

                self._atualizar_tiros_aliens()
                self._verificar_colisoes()  # Verifica as colisões
                self._desenhar_tela()
                pygame.display.flip()

            else:
                self._desenhar_game_over()
                pygame.display.flip()           # Atualiza a tela para mostrar Game Over

            self.clock.tick(60)

    def _verificar_colisoes(self):
        """Verifica as colisões entre lasers e aliens, e entre a nave e balas de alien."""
        # Colisões entre lasers e aliens
        for laser in self.lasers:
            alien_hits = pygame.sprite.spritecollide(laser, self.aliens, True)
            if alien_hits:
                self.score += len(alien_hits)
                laser.kill()

        # Colisões entre a nave e balas de alien
        hits = pygame.sprite.spritecollide(self.nave, self.aliens_bullets, True)
        if hits:
            self.nave.vida -= 1
            print(f"A nave foi atingida! Vidas restantes: {self.nave.vida}")

            if self.nave.vida <= 0:
                print("Game Over!")
                self.game_over = True
                pygame.time.delay(3000)  # Espera 3 segundos
                self.reiniciar_jogo()
            else:
                self.reiniciar_aliens()  # Reinicia os aliens após perder a vida

    def _atualizar_tiros_aliens(self):
        """Atualiza a lógica para os tiros dos aliens."""
        current_time = pygame.time.get_ticks()
        if current_time - self.last_alien_shot >= self.alien_cooldown and self.aliens:
            alien = random.choice(self.aliens.sprites())
            bullet = Alien_Bullets(alien.rect.centerx, alien.rect.bottom)
            self.aliens_bullets.add(bullet)
            self.last_alien_shot = current_time

    def _desenhar_tela(self):
        """Desenha todos os elementos na tela."""
        self.tela.fill(self.cor_fundo)  # Preenche a tela com a cor de fundo
        self.tela.blit(self.fundo, (0, 0))
        self.nave.desenhar(self.tela)
        self.lasers.draw(self.tela)
        self.aliens.draw(self.tela)
        self.aliens_bullets.draw(self.tela)
        self.desenhar_score()
        self.desenhar_vidas()

    def desenhar_vidas(self):
        """Desenha a quantidade de vidas restantes na tela."""
        for i in range(self.nave.vida):
            x = self.Largura - 50 - (i * 50)    # Ajusta a posição x para o lado Direito
            self.tela.blit(self.imagem_nave_vida, (x, 10)) # Y = 10 para ficar um pouco acima

    def desenhar_score(self):
        """Desenha a pontuação na tela."""
        fonte = pygame.font.Font(None, 36)
        texto = fonte.render(f'Score: {self.score}', True, (255, 255, 255))
        self.tela.blit(texto, (10, 10))

    def _desenhar_game_over(self):
        """Exibe a tela de Game Over."""
        fonte = pygame.font.Font(None, 74)
        texto = fonte.render("Game Over", True, (255, 0, 0))
        self.tela.blit(texto, (self.Largura // 2 - texto.get_width() // 2, self.Altura // 2 - texto.get_height() // 2))    
        reiniciar_texto = fonte.render("Pressione R para reiniciar", True, (255, 255, 255))
        self.tela.blit(reiniciar_texto, (self.Largura // 2 - reiniciar_texto.get_width() // 2, self.Altura // 2 + 50))

    def reiniciar_aliens(self):
        self.aliens.empty()
        self.create_aliens()

    def reiniciar_jogo(self):
        self.nave.vida = 3
        self.score = 0
        self.lasers.empty()
        self.aliens.empty()
        self.aliens_bullets.empty()
        self.create_aliens()
        self.game_over = False

      