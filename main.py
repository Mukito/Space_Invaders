import pygame
from telas import TelaPrincipal
#from Laser import Laser


def main():
    pygame.init()
    try:
        tela = TelaPrincipal()
        tela.run()
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()