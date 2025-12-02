import pygame
import random

class Cano:
    def __init__(self, tela):
        self.imagem = pygame.image.load('assets/cano.png')
        self.tela = tela 
        self.altura_base = random.randint(100, 300)
        self.x = tela.get_width()
        self.distancia = 50
        self.cano_cima = self.altura_base - self.imagem.get_height() - self.distancia
        self.cano_baixo = self.altura_base + self.distancia
        self.velocidade = 2
        
        # Flag para controlar se o jogador já passou por este cano
        self.pontuado = False
        
        # Posição do centro do cano (para detectar passagem)
        self.centro_x = self.x + self.imagem.get_width() / 2

    def atualizar(self):
        self.x -= self.velocidade
        # Atualiza a posição do centro do cano
        self.centro_x = self.x + self.imagem.get_width() / 2
        
        if self.x < -self.imagem.get_width():
            self.resetar_posicao()
    
    def resetar_posicao(self):
        """Reseta o cano para a posição inicial direita da tela"""
        self.x = self.tela.get_width()
        self.altura_base = random.randint(100, 300)
        self.cano_cima = self.altura_base - self.imagem.get_height() - self.distancia
        self.cano_baixo = self.altura_base + self.distancia
        self.centro_x = self.x + self.imagem.get_width() / 2
        self.pontuado = False  # Reseta a flag de pontuação

    def desenhar(self):
        imagem_invertida = pygame.transform.flip(self.imagem, False, True)
        self.tela.blit(imagem_invertida, (self.x, self.cano_cima))
        self.tela.blit(self.imagem, (self.x, self.cano_baixo))

    def detectarColisao(self, rectJogador):
        rectCanoCima = pygame.Rect((self.x, self.cano_cima), self.imagem.get_size())
        rectCanoBaixo = pygame.Rect((self.x, self.cano_baixo), self.imagem.get_size())

        if rectJogador.colliderect(rectCanoCima) or rectJogador.colliderect(rectCanoBaixo):
            return True
        else:
            return False
    
    def jogadorPassou(self, rect_jogador):
        """
        Verifica se o jogador passou pelo cano.
        Retorna True se o jogador ultrapassou o centro do cano.
        """
        # Se já pontuou este cano, não conta novamente
        if self.pontuado:
            return False
        
        # Verifica se o jogador passou pelo centro do cano
        # O centro é usado como referência para detectar a passagem
        if rect_jogador.left > self.centro_x:
            self.pontuado = True
            return True
        
        return False
    
    def get_posicao_x(self):
        """Retorna a posição X do cano"""
        return self.x
    
    def get_centro_x(self):
        """Retorna a posição X do centro do cano"""
        return self.centro_x
    
    def get_largura(self):
        """Retorna a largura do cano"""
        return self.imagem.get_width()