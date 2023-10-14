import requests
import json

class PrevisaoDoTempo:
    def __init__(self, tempo, previsao, data, umidade, velocidadeVento):
        self.previsao = previsao
        self.tempo = tempo
        self.data = data
        self.umidade = umidade
        self.velocidadeVento = velocidadeVento
    # Fim def __init__(self, tempo, previsao, data, umidade, velocidadeVento)
        
    
    def previsaoDoTempoSP(self):
        self.previsao = requests.get('https://api.hgbrasil.com/weather')
        self.previsao = self.previsao.json()

        return self.previsao
    # Fim def previsaoDoTempoSP(self)
    
    def tempoEmSP(self, previsao):
        self.tempo = self.previsao['results']['description']

        return self.tempo
    # Fim def tempoEmSP(self, previsao)
    
    def dia(self, previsao):
        self.data = self.previsao['results']['date']

        return self.data
    # Fim def dia(self, previsao)
    
    def umidadeSP(self, previsao):
        self.umidade = self.previsao['results']['humidity']

        return self.umidade
    # Fim def umidadeSP(self, previsao)
    
    def velocidadeDoVento(self, previsao):
        self.velocidadeVento = self.previsao['results']['wind_speedy']

        return self.velocidadeVento
    # Fim def velocidadeDoVento(self, previsao)