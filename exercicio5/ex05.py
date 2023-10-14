import requests
import json

class ConversorDeMoedas:
    '''Classe para cotações e conversão de valores'''
    def __init__(self, cotacao, cotacaoDolar, cotacaoEuro, real, conversaoRealDolar, conversaoRealEuro):
        self.cotacao = cotacao
        self.cotacaoDolar = cotacaoDolar
        self.cotacaoEuro = cotacaoEuro
        self.real = real
        self.conversaoRealDolar = conversaoRealDolar
        self.conversaoRealEuro = conversaoRealEuro
    # Fim def __init__(self, cotacao, cotacaoDolar, cotacaoEuro, real, conversaoRealDolar, conversaoRealEuro)
    
    def cotacoesMoedas(self):
        self.cotacao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
        self.cotacao = self.cotacao.json()

        return self.cotacao
    # Fim def cotacoesMoedas(self)
    
    def valorDolar(self, cotacao):
        self.cotacaoDolar = float(self.cotacao['USDBRL']['bid'])

        return self.cotacaoDolar
    # Fim def valorDolar(self, cotacao)
    
    def valorEuro(self, cotacao):
        self.cotacaoEuro = float(self.cotacao['EURBRL']['bid'])

        return self.cotacaoEuro
    # Fim def valorEuro(self, cotacao)
    
    def converterRealDolar(self, cotacaoDolar):
        self.conversaoRealDolar = self.real / self.cotacaoDolar

        return self.conversaoRealDolar
    # Fim def converterRealDolar(self, cotacaoDolar)
    
    def converterRealEuro(self, cotacaoEuro):
        self.conversaoRealEuro = self.real / self.cotacaoEuro

        return self.conversaoRealEuro
    # Fim def converterRealEuro(self, cotacaoEuro)