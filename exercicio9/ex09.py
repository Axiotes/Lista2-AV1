class Cinema:
    def __init__(self, filme, filmeSelecionado, horario0, horario1, horario2, horario3, horarioSelecionado, assento0, assento1, assento2, assentoSelecionado):
        self.filme = filme
        self.filmeSelecionado = filmeSelecionado
        self.horario0 = horario0
        self.horario1 = horario1
        self.horario2 = horario2
        self.horario3 = horario3
        self.horarioSelecionado = horarioSelecionado
        self.assento0 = assento0
        self.assento1 = assento1
        self.assento2 = assento2
        self.assentoSelecionado = assentoSelecionado
    # Fim def __init__(self, filme, filmeSelecionado, horario0, horario1, horario2, horario3, horarioSelecionado, assento0, assento1, assento2, assentoSelecionado)
    
    def escolherFilme(self):
        self.filme = ['HOMEM-ARANHA', 'BATMAN', 'TRANSFORMERS', 'CREED']

        return self.filme
    # Fim def escolherFilme(self)
    
    def horarioFilme0(self):
        self.horario0 = ['17:00', '18:15', '20:30']

        return self.horario0
    # Fim def horarioFilme0(self)
    
    def horarioFilme1(self):
        self.horario1 = ['19:00', '20:50', '21:30']

        return self.horario1
    # Fim def horarioFilme1(self)
    
    def horarioFilme2(self):
        self.horario2 = ['16:45', '18:20', '19:40']

        return self.horario2
    # Fim def horarioFilme2(self)
    
    def horarioFilme3(self):
        self.horario3 = ['20:10', '21:40', '22:20']

        return self.horario3
    # Fim def horarioFilme3(self)
    
    def assentoHorario0(self):
        self.assento0 = ['A1', 'A2', 'A3', 'A4',
                         'B1', 'B2', 'B3', 'B4',
                         'C1', 'C2', 'C3', 'C4',
                         'D1', 'D2', 'D3', 'D4']
        
        return self.assento0
    # Fim def assentoHorario0(self)
    
    def assentoHorario1(self):
        self.assento1 = ['A1', 'A2', 'A3', 'A4',
                         'B1', 'B2', 'B3', 'B4',
                         'C1', 'C2', 'C3', 'C4',
                         'D1', 'D2', 'D3', 'D4']
        
        return self.assento1
    # Fim def assentoHorario1(self)
    
    def assentoHorario2(self):
        self.assento2 = ['A1', 'A2', 'A3', 'A4',
                         'B1', 'B2', 'B3', 'B4',
                         'C1', 'C2', 'C3', 'C4',
                         'D1', 'D2', 'D3', 'D4']
        
        return self.assento2
    # Fim def assentoHorario2(self)
    
    def removerAssento0(self, assentoSelecionado):
        self.assento0.remove(self.assentoSelecionado)

        return self.assento0
    # Fim def removerAssento0(self, assentoSelecionado)
    
    def removerAssento1(self, assentoSelecionado):
        self.assento0.remove(self.assentoSelecionado)

        return self.assento0
    # Fim def removerAssento1(self, assentoSelecionado)
    
    def removerAssento2(self, assentoSelecionado):
        self.assento2.remove(self.assentoSelecionado)

        return self.assento2
    # Fim def removerAssento2(self, assentoSelecionado)