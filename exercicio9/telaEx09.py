import ex09
assistir = ex09.Cinema(filme = [],
                       filmeSelecionado = None,
                       horario0 = [],
                       horario1 = [],
                       horario2 = [],
                       horario3 = [],
                       horarioSelecionado = None,
                       assento0 = [],
                       assento1 = [],
                       assento2 = [],
                       assentoSelecionado = None)

op = 0

while op != 2:
    print('Digite 1: ESCOLHER FILME\n',
          'Digite 2: SAIR')
    op = int(input())

    if op == 1:
        print('Escolha o filme que você deseja assistir!')

        assistir.escolherFilme()

        print(f'Digite 1: {assistir.filme[0]}\n',
              f'Digite 2: {assistir.filme[1]}\n',
              f'Digite 3: {assistir.filme[2]}\n',
              f'Digite 4: {assistir.filme[3]}')
        assistir.filmeSelecionado = int(input())

        if assistir.filmeSelecionado == 1:
            assistir.horarioFilme0()

            print('Escolha o horário desejado!')

            print(f'Digite 1: {assistir.horario0[0]}\n',
                  f'Digite 2: {assistir.horario0[1]}\n',
                  f'Digite 3: {assistir.horario0[2]}\n')
        # Fim if assistir.filmeSelecionado == 1
        
        if assistir.filmeSelecionado == 2:
            assistir.horarioFilme1()

            print('Escolha o horário desejado!')

            print(f'Digite 1: {assistir.horario1[0]}\n',
                  f'Digite 2: {assistir.horario1[1]}\n',
                  f'Digite 3: {assistir.horario1[2]}\n')
        # Fim if assistir.filmeSelecionado == 2
        
        if assistir.filmeSelecionado == 3:
            assistir.horarioFilme2()

            print('Escolha o horário desejado!')

            print(f'Digite 1: {assistir.horario2[0]}\n',
                  f'Digite 2: {assistir.horario2[1]}\n',
                  f'Digite 3: {assistir.horario2[2]}\n')
        # Fim if assistir.filmeSelecionado == 3
        
        if assistir.filmeSelecionado == 4:
            assistir.horarioFilme3()

            print('Escolha o horário desejado!')

            print(f'Digite 1: {assistir.horario3[0]}\n',
                  f'Digite 2: {assistir.horario3[1]}\n',
                  f'Digite 3: {assistir.horario3[2]}\n')
        # Fim if assistir.filmeSelecionado == 4
            
        if assistir.filmeSelecionado < 1 or assistir.filmeSelecionado > 4:
            print('Opção inválida! Tente novamente')
            break
        # Fim if assistir.filmeSelecionado < 1 or assistir.filmeSelecionado > 4
            
        assistir.horarioSelecionado = int(input())

        if assistir.horarioSelecionado == 1:
            assistir.assentoHorario0()

            print('Escolha o seu assento!')

            print(assistir.assento0[:])
        # Fim if assistir.horarioSelecionado == 1

        if assistir.horarioSelecionado == 2:
            assistir.assentoHorario1()

            print('Escolha o seu assento!')

            print(assistir.assento1[:])
        # Fim if assistir.horarioSelecionado == 2

        if assistir.horarioSelecionado == 3:
            assistir.assentoHorario2()

            print('Escolha o seu assento!')

            print(assistir.assento2[:])

            assistir.assentoSelecionado = input()
            assistir.assentoSelecionado = assistir.assentoSelecionado.upper()
        # Fim if assistir.horarioSelecionado == 3

        assistir.assentoSelecionado = input()
        assistir.assentoSelecionado = assistir.assentoSelecionado.upper()

        if assistir.horarioSelecionado < 1 or assistir.horarioSelecionado > 3:
            print('Opção inválida! Tente novamente')
            break
        # Fim if assistir.horarioSelecionado < 1 or assistir.horarioSelecionado > 3

        print(f'Você vai assistir o filme {assistir.filmeSelecionado} as {assistir.horarioSelecionado} no assento {assistir.assentoSelecionado}')
    # Fim if op == 1

    if op < 1 or op > 2:
        print('Opção inválida! Tente novamente')
    # Fim if op < 1 or op > 2
# Fim while op != 2