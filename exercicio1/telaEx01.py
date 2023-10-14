import ex01
calculadora = ex01.CalculadoraDeNotas(nota1 = None,
                                      nota2 = None ,
                                      media = None)

op = 0

while op != 2:
    print('Digite 1: CALCULAR MÉDIA\n',
          'Digite 2: SAIR')
    op = int(input())

    if op == 1:
        calculadora.nota1 = float(input('1º Nota: '))
        calculadora.nota2 = float(input('2º Nota: '))

        calculadora.calculoMedia(calculadora.nota1, calculadora.nota2)

        calculadora.nota1 = '{:.2f}'.format(calculadora.nota1)
        calculadora.nota2 = '{:.2f}'.format(calculadora.nota2)
        calculadora.media = '{:.2f}'.format(calculadora.media)

        print(f'1º Nota: {calculadora.nota1}\n',
              f'2º Nota: {calculadora.nota2}\n',
              f'Média: {calculadora.media}')
    # Fim if op == 1
    
    if op < 1 or op > 2:
        print('Opção inválida! Tente novamente')
    # Fim if op < 1 or op > 2
# Fim while op != 2