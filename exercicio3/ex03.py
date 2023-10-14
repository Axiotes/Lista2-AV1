import random

class JogoDaForca:
    def __init__(self, futebol, volei, judo, maca, biscoito, melancia, faca, controle, cadeira, palavras, palavraSelecionada, numeroPalavra, letras, letraUsuario, conjuntoLetras):
        self.futebol = futebol
        self.volei = volei
        self.judo = judo
        self.maca = maca
        self.biscoito = biscoito
        self.melancia = melancia
        self.faca = faca
        self.controle = controle
        self.cadeira = cadeira
        self.palavras = palavras
        self.palavraSelecionada = palavraSelecionada
        self.numeroPalavra = numeroPalavra
        self.letras = letras
        self.letraUsuario = letraUsuario
        self.conjuntoLetras = conjuntoLetras
    
    def palavrasTotal(self, palavras):
        self.futebol = ['F', 'U', 'T', 'E', 'B', 'O', 'L']
        self.volei = ['V', 'Ô', 'L', 'E', 'I']
        self.judo = ['J', 'U', 'D', 'Ô']
        self.maca = ['M', 'A', 'Ç', 'Ã']
        self.biscoito = ['B', 'I', 'S', 'C', 'O', 'I', 'T', 'O']
        self.melancia = ['M', 'E', 'L', 'A', 'N', 'C', 'I', 'A']
        self.faca = ['F', 'A', 'C', 'A']
        self.controle = ['C', 'O', 'N', 'T', 'R', 'O', 'L', 'E']
        self.cadeira = ['C', 'A', 'D', 'E', 'I', 'R', 'A']
        self.palavras = []

        self.palavras.append(self.futebol[:])
        self.palavras.append(self.volei[:])
        self.palavras.append(self.judo[:])
        self.palavras.append(self.maca[:])
        self.palavras.append(self.biscoito[:])
        self.palavras.append(self.melancia[:])
        self.palavras.append(self.faca[:])
        self.palavras.append(self.controle[:])
        self.palavras.append(self.cadeira[:])

        return self.palavras
    
    def selecionarPalavra(self, palavraSelecionada):
        self.palavraSelecionada = []
        self.numeroPalavra = random.randint(0, 8)

        self.palavraSelecionada = self.palavras[self.numeroPalavra]

        return self.palavraSelecionada
    
    def quantidadeDeLetras(self, palavraSelecionada):
        self.letras = len(self.palavraSelecionada)

        return self.letras