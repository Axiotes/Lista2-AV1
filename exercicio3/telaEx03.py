import ex03
jogo = ex03.JogoDaForca(futebol = ['F', 'U', 'T', 'E', 'B', 'O', 'L'],
                        volei = ['V', 'Ô', 'L', 'E', 'I'],
                        judo = ['J', 'U', 'D', 'Ô'],
                        maca = ['M', 'A', 'Ç', 'Ã'],
                        biscoito = ['B', 'I', 'S', 'C', 'O', 'I', 'T', 'O'],
                        melancia = ['M', 'E', 'L', 'A', 'N', 'C', 'I', 'A'],
                        faca = ['F', 'A', 'C', 'A'],
                        controle = ['C', 'O', 'N', 'T', 'R', 'O', 'L', 'E'],
                        cadeira = ['C', 'A', 'D', 'E', 'I', 'R', 'A'],
                        palavras = [],
                        palavraSelecionada = None,
                        numeroPalavra = None,
                        letras = None,
                        letraUsuario = None,
                        conjuntoLetras = [])

op = 0

while op !=2:
    print('Digite 1: JOGAR JOGO DA FORCA\n',
          'Digite 2: SAIR')
    op = int(input())

    if op == 1:
            jogo.palavrasTotal(jogo.palavras)
            jogo.selecionarPalavra(jogo.palavraSelecionada)
            jogo.quantidadeDeLetras(jogo.palavraSelecionada)
      
            print(f'A palavra tem {jogo.letras} letras\n',
                  'Você tem 5 tentativas para acertar todas as letras')
            
            print(jogo.palavraSelecionada)

            tentativa = 0

            while tentativa < 5:
                  jogo.letraUsuario = input('Digite uma letra: ')
                  jogo.letraUsuario = jogo.letraUsuario.upper()

                  if jogo.letraUsuario in jogo.palavraSelecionada:
                        jogo.conjuntoLetras.append(jogo.letraUsuario)
                        print(f'A letra {jogo.letraUsuario} está correta!')

                        for jogo.letraUsuario in jogo.conjuntoLetras and jogo.letraUsuario in jogo.palavraSelecionada:
                              jogo.conjuntoLetras = True

                        if jogo.conjuntoLetras == True:
                              print(f'Você acertou a palavra {jogo.palavraSelecionada}')
                              break
                  else:
                        print(f'A letra {jogo.letraUsuario} está incorreta! Tente novamente')
                        tentativa = tentativa + 1

                        if tentativa == 5:
                              print('Você perdeu! Tente novamente')
      