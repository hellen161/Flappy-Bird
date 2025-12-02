import pygame
from scripts.cano import Cano
from scripts.jogador import Jogador
from scripts.interfaces import Texto
from scripts.interfaces import Botao

class Partida:

    def __init__(self, tela):
        self.tela = tela
        self.jogador = Jogador(tela, 100, 100)
        self.cano = Cano(tela)
        self.estado = 'partida'
        self.pontosValor = 0
        self.pontosTexto = Texto(tela, str(self.pontosValor), 10, 10, (255, 255, 255), 30)
        
        # Controle de pontuação por cano
        self.ultimo_cano_pontuado_id = None
        self.pode_pontuar_novamente = True

    def atualizar(self):
        self.estado = 'partida'
        self.jogador.atualizar()
        self.cano.atualizar()

        # Verifica se o jogador passou pelo cano
        # Usamos um sistema que permite pontuar sempre que o cano é resetado
        if self.cano.jogadorPassou(self.jogador.getRect()):
            self.pontosValor += 1
            self.pontosTexto.atualizarTexto(str(self.pontosValor))
            print(f"Pontuação: {self.pontosValor}")  # Para debug

        if self.cano.detectarColisao(self.jogador.getRect()):
            self.estado = "menu"
            self.resetar_partida()

        self.jogador.desenhar()
        self.cano.desenhar()
        self.pontosTexto.desenhar()

        return self.estado
    
    def resetar_partida(self):
        """Reseta todos os elementos da partida"""
        self.jogador.posicao = [100, 100]
        self.cano.x = self.tela.get_width()
        self.cano.resetar_posicao()
        self.pontosValor = 0
        self.pontosTexto.atualizarTexto(str(self.pontosValor))
        self.ultimo_cano_pontuado_id = None
        self.pode_pontuar_novamente = True


class Menu: 
    def __init__(self, tela):
        self.tela = tela
        self.titulo = Texto(tela, "FlappyBird", 100, 20, (255, 255, 255), 50)
        self.estado = "menu"
        self.botao__jogar = Botao(tela, "jogar", 100, 100, 50, (200, 0, 0), (255, 255, 255))

    def atualizar(self):
        self.estado = "menu"
        self.titulo.desenhar()
        self.botao__jogar.desenhar()

        if self.botao__jogar.get_click():
            self.estado = "partida"

        return self.estado