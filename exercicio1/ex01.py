class CalculadoraDeNotas:
    '''Classe para fazer calculo da média'''
    def __init__(self, nota1, nota2, media):
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = media
    # Fim def __init__(self, nota1, nota2, media)

    def calculoMedia(self, nota1, nota2):
        self.media = (self.nota1 + self.nota2) / 2

        return self.media
    # Fim def calculoMedia(self, nota1, nota2)