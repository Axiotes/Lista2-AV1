class AgendaDeContatos:
    '''Classe para ações na lista de contatos'''
    def __init__(self, contatos, adicionar, remover):
        self.contatos = contatos
        self.adicionar = adicionar
        self.remover = remover
    # Fim def __init__(self, contatos)

    def listaDeContatos(self, contatos):
        self.contatos = []

        return self.contatos
    # Fim def listaDeContatos(self, contatos)

    def addContato(self, adicionar):
        self.contatos.append(self.adicionar)

        return self.contatos
    # Fim def addContato(self, adicionar)

    def removerContato(self, remover):
        self.contatos.remove(self.remover)

        return self.contatos
    # Fim def removerContato(self, remover)