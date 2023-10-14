class GerenciadorDeTarefas:
    def __init__(self, adicionar, remover, concluido, tarefas, tarefaConcluida):
        self.adicionar = adicionar
        self.remover = remover
        self.concluido = concluido
        self.tarefas = tarefas
        self.tarefaConcluida = tarefaConcluida
    # Fim def __init__(self, adicionar, remover, concluido, tarefas)

    def listaDeTarefas(self, tarefas):
        self.tarefas = []

        return self.tarefas
    # Fim def listaDeTarefas(self, tarefas)

    def adicionarTarefa(self, adicionar):
        self.tarefas.append(self.adicionar)

        return self.tarefas
    # Fim def adicionarTarefa(self, adicionar)

    def marcarConcluido(self, concluido):
        self.tarefas.remove(self.concluido)

        self.tarefaConcluida = []
        self.tarefaConcluida.append(self.concluido)

        return self.tarefaConcluida
    # Fim def marcarConcluido(self, concluido)

    def removerTarefa(self, remover):
        self.tarefas.remove(self.remover)

        return self.tarefas
    # Fim def removerTarefa(self, remover)