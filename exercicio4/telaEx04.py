import ex04
operacao = ex04.CaixaEletronico(sacar = None,
                                depositar = None,
                                saldo = 0,
                                saldoAtual = None)

op = 0

while op != 4:
    print('Digite 1: SACAR\n',
          'Digite 2: DEPOSITAR\n',
          'Digite 3: VER SALDO\n',
          'Digite 4: SAIR')
    op = int(input())
    
    if op == 1:
        operacao.sacar = float(input('Valor do saque: '))

        if operacao.saldo > operacao.sacar:
            operacao.saque(operacao.sacar, operacao.saldo)
            
            print(f'Valor do saque: {operacao.sacar}\n',
                  f'Saldo: {operacao.saldo}')
        else:
            print('Saldo insuficiente\n'
                  f'Valor da tentativa de saque: {operacao.sacar}\n'
                  f'Saldo: {operacao.saldo}')
        # Fim if operacao.saldo > operacao.sacar e else saldo insuficiente
    # Fim if op == 1

    if op == 2:
        operacao.depositar = float(input('Valor do depósito: '))

        operacao.deposito(operacao.depositar, operacao.saldo)

        print(f'Valor do depósito: {operacao.depositar}\n',
              f'Saldo: {operacao.saldo}')
    # Fim op == 2

    if op == 3:
        print(f'Saldo: {operacao.saldo}')
    # Fim op == 3

    if op < 1 or op > 4:
        print('Opção inválida! Tente novamente')
#while op != 4