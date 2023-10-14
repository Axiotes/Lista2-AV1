import ex08
calcular = ex08.CalculoIMC(imc = None,
                altura = None,
                peso = None)

op = 0

while op != 2:
   print('Digite 1: CALCULAR IMC\n',
          'Digite 2: SAIR')
   op = int(float(input()))

   if op == 1:
      calcular.altura = float(input('Altura (em metros): '))
      calcular.peso = float(input('Peso (em kg): '))

      calcular.calculo(calcular.altura, calcular.peso)

      print(f'Altura: {calcular.altura}\n',
            f'Peso: {calcular.peso}\n',
            f'IMC: {calcular.imc: .2f}')
      
      if calcular.imc <= 18.5:
         print('Abaixo do peso')
      if calcular.imc >= 18.6 and calcular.imc <= 24.9:
         print('Peso ideal')
      if calcular.imc >= 25 and calcular.imc <= 29.9:
         print('Levemente acima do peso')
      if calcular.imc >= 30 and calcular.imc <= 34.9:
         print('Obesidade grau 1')
      if calcular.imc >= 35 and calcular.imc <= 39.9:
         print('Obesidade grau 2 (Severa)')
      if calcular.imc >= 40:
         print('Obesidade grau 3 (Mórbida)')
      # Fim if tabela de grau do imc
   # Fim op == 1

   if op < 1 or op > 2:
      print('Opção inválida! Tente novamente')
# Fim while op != 2