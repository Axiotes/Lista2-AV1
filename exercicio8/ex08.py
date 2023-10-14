class CalculoIMC:
    '''Classe para calculo do IMC'''
    def __init__(self, imc, altura, peso):
        self.imc = imc
        self.altura = altura
        self.peso = peso
    # Fim def __init__(self, imc, altura, peso)

    def calculo(self, altura, peso):
        self.imc = self.peso / (self.altura * self.altura)

        return self.imc
    # Fim def calculo(self, altura, peso)