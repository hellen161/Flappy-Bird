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
        self.contador = 0
        self.pontosTexto = Texto(tela,str(self.pontosValor),10,10,(255,255,255),30)

    def atualizar(self):
        self.estado = 'partida'
        self.jogador.atualizar()
        self.cano.atualizar()

        self.contador +=1
        if self.contador > 60:
            self.pontosValor += 1
            self.contador = 0
            self.pontosTexto.atualizarTexto(str(self.pontosValor))

        if self.cano.detectarColisao(self.jogador.getRect()):
            self.estado = "menu"
            self.jogador.posicao = [100, 100]
            #self.jogador.velocidadeAtual = 0
            self.cano.x = self.tela.get_width()
            self.pontosValor = 0

        self.jogador.desenhar()
        self.cano.desenhar()

        return self.estado
    
class Menu: 
    def __init__(self, tela):
        self.tela = tela
        self.titulo = Texto(tela, "FlappyBird", 100, 20, (255,255,255), 50)
        self.estado = "menu"
        self.botao__jogar = Botao(tela, "jogar", 100, 100, 50, (200,0,0), (255,255,255))

    def atualizar(self):
        self.estado = "menu"
        self.titulo.desenhar()
        self.botao__jogar.desenhar()

        if self.botao__jogar.get_click():
            self.estado = "partida"

        return self.estado