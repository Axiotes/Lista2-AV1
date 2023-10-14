import ex05
conversor = ex05.ConversorDeMoedas(cotacao = [],
                                   cotacaoDolar = None,
                                   cotacaoEuro = None,
                                   real = 0,
                                   conversaoRealDolar = 0,
                                   conversaoRealEuro = 0)

op = 0

while op != 3:
    print('Digite 1: VER COTAÇÕES\n',
          'Digite 2: CONVERTER\n',
          'Digite 3: SAIR')
    op = int(input())

    conversor.cotacoesMoedas()
    conversor.valorDolar(conversor.cotacao)
    conversor.valorEuro(conversor.cotacao)

    if op == 1:
        print('Digite 1: VER COTAÇÃO DOLÁR\n',
              'Digite 2: VER COTAÇÃO EURO')
        opCotacao = int(input())

        if opCotacao == 1:
            conversor.cotacaoDolar = '{:.2f}'.format(conversor.cotacaoDolar)
            print(f'Cotação dolár: {conversor.cotacaoDolar}')
        if opCotacao == 2:
            conversor.cotacaoEuro = '{:.2f}'.format(conversor.cotacaoEuro)
            print(f'Cotação euro: {conversor.cotacaoEuro}')
        if opCotacao < 1 or opCotacao > 2:
            print('Opção inválida! Tente novamente')
        # Fim if ver cotação
    # Fim if op == 1
    
    if op == 2:
        print('Digite 1: Converter de real para dolár\n',
              'Digite 2: Converter de real para euro')
        opConversao = int(input())

        if opConversao == 1:
            conversor.real = float(input('Digite o valor em real: '))

            conversor.converterRealDolar(conversor.cotacaoDolar)
            
            conversor.conversaoRealDolar = '{:.2f}'.format(conversor.conversaoRealDolar)
            print(f'Valo em real: {conversor.real}\n',
                  f'Valor em dolár: {conversor.conversaoRealDolar}')
        # Fim if opConversao == 1
            
        if opConversao == 2:
            conversor.real = float(input('Digite o valor em real:'))

            conversor.converterRealEuro(conversor.cotacaoEuro)

            conversor.conversaoRealEuro = '{:.2f}'.format(conversor.conversaoRealEuro)
            print(f'Valo em real: {conversor.real}\n',
                  f'Valor em euro: {conversor.conversaoRealEuro}')
        # Fim if opConversao == 2

        if opConversao < 1 or opConversao > 2:
            print('Opção inválida! Tente novamente')
        # Fim if opConversao < 1 or opConversao > 2
    # Fim if op == 2

    if op < 0 or op > 3:
        print('Opção inválida! Tente novamente')
    # Fim if op < 0 or op > 3
# Fim while op != 3