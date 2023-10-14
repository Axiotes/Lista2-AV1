import ex06
gerenciamento = ex06.GerenciadorDeTarefas(adicionar = None,
                                          remover = None,
                                          concluido = None,
                                          tarefas = [],
                                          tarefaConcluida = [])

op = 0

while op != 5:
    print('Digite 1: VER LISTA DE TAREFAS\n',
          'Digite 2: ADICIONAR TAREFA\n',
          'Digite 3: REMOVER TAREFA\n',
          'Digite 4: MARCAR COMO CONCLUIDA\n',
          'Digite 5: SAIR')
    op = int(input())

    if op == 1:
        print(f'Tarefas para ser realizadas: {gerenciamento.tarefas}\n',
              f'Tarefas concluídas {gerenciamento.tarefaConcluida}')
    # Fim op == 1

    if op == 2:
        gerenciamento.adicionar = input('Digite a tarefa: ')
        gerenciamento.adicionar = gerenciamento.adicionar.upper()

        if gerenciamento.adicionar in gerenciamento.tarefas:
            print(f'Tarefa {gerenciamento.adicionar} já existente na lista')
        else:
            gerenciamento.adicionarTarefa(gerenciamento.adicionar)

            print(f'{gerenciamento.adicionar} foi adicionado a sua lista de tarefa')
        # Fim if conferir se a tarefa adicionada já existe na lista
    # Fim op == 2

    if op == 3:
        gerenciamento.remover = input('Digite a tarefa: ')
        gerenciamento.remover = gerenciamento.remover.upper()
        
        if gerenciamento.remover in gerenciamento.tarefas:
            gerenciamento.removerTarefa(gerenciamento.remover)

            print(f'{gerenciamento.remover} foi excluído da sua lista de tarefas')
        else:
            print(f'A tarefa {gerenciamento.remover} não existe')
        # Fim if conferir se a tarefa removida existe
    # Fim op == 3

    if op == 4:
        gerenciamento.concluido = input('Digite a tarefa: ')
        gerenciamento.concluido = gerenciamento.concluido.upper()

        if gerenciamento.concluido in gerenciamento.tarefas:
            gerenciamento.marcarConcluido(gerenciamento.concluido)

            print(f'{gerenciamento.concluido} foi marcado como concluído')
        else:
            print(f'A tarefa {gerenciamento.concluido} não existe')
        # Fim if conferir se a tarefa concluida existe
    # Fim op == 4

    if op < 1 or op > 5:
        print('Opção inválida! Tente novamente')
    # Fim if op < 1 or op > 5
# Fim while != 5