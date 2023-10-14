import random

op = 0

while op != 2:
    print('Digite 1: ADIVINHAR NÚMERO\n',
          'Digite 2: SAIR')
    op = int(input())

    if op == 1:
        numeroMaquina = random.randint(0, 100)

        numeroUsuario = int(input('Digite um número: '))

        while numeroUsuario != numeroMaquina:
            if numeroUsuario > numeroMaquina:
                print(f'O número correto é menor que {numeroUsuario}')
            if numeroUsuario < numeroMaquina:
                print(f'O número correto é maior que {numeroUsuario}')
            # Fim if dica maior ou menor

            numeroUsuario = int(input('Digite um número: '))
        # Fim while numeroUsuario != numeroMaquina

        print('ACERTOU')
    # fim if op == 1

    if op < 1 or op > 2:
        print('Opção inválida! Tente novamente')
    # Fim if op < 1 or op > 2
# Fim if op == 1