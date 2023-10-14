import ex10
app = ex10.PrevisaoDoTempo(previsao = [],
                           tempo = None,
                           data = None,
                           umidade = None,
                           velocidadeVento = None)

op = 0

while op != 2:
    print('Digite 1: VER PREVISÃO DO TEMPO DE SÃO PAULO\n',
          'Digite 2: SAIR')
    op = int(input())

    if op == 1:
        app.previsaoDoTempoSP()
        app.tempoEmSP(app.previsao)
        app.dia(app.previsao)
        app.umidadeSP(app.previsao)
        app.velocidadeDoVento(app.previsao)

        print(f'Data: {app.data}\n',
              f'Tempo: {app.tempo}\n',
              f'Umidade: {app.umidade} %\n',
              f'Velocidade do vento: {app.velocidadeVento}')
    # Fim if op == 1
    
    if op < 1 or op > 2:
        print('Opção inválida! Tente novamente')
    # Fim if op < 1 or op > 2
# Fim while op != 2