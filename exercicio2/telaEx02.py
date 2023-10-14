import ex02
lista = ex02.AgendaDeContatos(contatos = [],
                              adicionar = None,
                              remover = None)

op = 0

while op != 4:
    print('Digite 1: VER LISTA DE CONTATOS\n',
          'Digite 2: ADICIONAR CONTATO\n',
          'Digite 3: REMOVER CONTATO\n',
          'Digite 4: SAIR')
    op = int(input())

    if op == 1:
        print(lista.contatos)
    # Fim op == 1

    if op == 2:
        print('Digite o contato da seguinte forma: Nome do contato - ddd 9XXXX-XXXX')

        lista.adicionar = input('Contato: ')
        lista.adicionar = lista.adicionar.upper()

        if lista.adicionar not in lista.contatos:
            lista.addContato(lista.adicionar)

            print(f'Contato {lista.adicionar} adicionado com sucesso')
        else:
            print(f'O contato {lista.adicionar} já existe na agenda')
    # Fim op == 2

    if op == 3:
        print('Digite o contato da seguinte forma: Nome do contato - ddd 9XXXX-XXXX')

        lista.remover = input('Contato: ')
        lista.remover = lista.remover.upper()

        print(f'Você tem certeza que deseja excluir {lista.remover} ?\n',
              'Digite 1: CONFIRMAR REMOÇÃO DO CONTATO\n',
              'Digite 2: CANCELAR REMOÇÃO DO CONTATO')
        confirmacao = int(input())

        if confirmacao == 1:
            lista.removerContato(lista.remover)

            print(f'Contato {lista.remover} excluído com sucesso')
        if confirmacao == 2:
            print('Remoção cancelada')
        if confirmacao < 1 or confirmacao > 2:
            print('Opção inválida! Tente novamente')
        # Fim if confirmação
    # Fim if op == 3

    if op < 1 or op > 4:
        print('Opção inválida! Tente novamente')
    # Fim if op < 1 or op > 4
# Fim while op != 4