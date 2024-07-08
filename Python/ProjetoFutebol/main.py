def analisaDados(time, quantidadeJogos):
    import sys
    sys.path.append('/home/ubuntu/BackAnaliseDadosFutebol/Python/ProjetoFutebol')
    import Funcoes.raspagemDadosTime as raspagem
    import Funcoes.criaListaJogos as listaJogos
    import Funcoes.criaListaTimes as listaTimes
    import Funcoes.criaArquivoComDados as arquivo
    import Funcoes.calcularMedias as calcularMedias
    import Funcoes.descobrirTimePesquisado as descobrirTime
    import Funcoes.pegaIdPartida as pegarIdPartida
    import Escanteios.valorMedias as valorMedias
    import re

    response = raspagem.raspagemDados(time)

    # cria uma lista dessa raspagem de dados
    lista = []
    lista = re.split('[,:=&]', response.text)

    # pega o Id da partida
    idPartidas = pegarIdPartida.idPartida(lista, quantidadeJogos)

    # pega o ID do time que foi pesquisado
    idTimePesquisado = time

    # descobre o time pesquisado
    timePesquisado = descobrirTime.descobreTimePesquisado(lista, idTimePesquisado)

    # separa dados e deixa apenas informações do time da casa e de fora
    listaJogos = listaJogos.criaListaJogos(lista, quantidadeJogos)

    # pega valores dos atributos
    posseDeBola, escanteios, cartoes, chutesGol, chutesFora, impedimentos, chutesLivres, ataques, lateraisCobrados, tirosDeMeta, cartoesVermelhos = valorMedias.valorMedias(idPartidas)

    print(posseDeBola)

    # pega o resultado dos ultimos jogos com o nome dos times e placar
    listaTotal = listaTimes.criaListaTimes(listaJogos, idPartidas, escanteios, cartoes, posseDeBola, chutesGol, chutesFora, impedimentos, chutesLivres, ataques, lateraisCobrados, tirosDeMeta, cartoesVermelhos)

    # coloca as informações dentro de um txt
    arquivo.criaArquivo(listaTotal, quantidadeJogos)
    print("Processo concluido!!!\n")

    mediaGols, mediaEscanteios, mediaCartoes, mediaPosseDeBola, mediaChutesNoGol, mediaChutesParaFora, mediaImpedimentos, mediaChutesLivres, mediaAtaques, mediaLaterais, mediaTirosDeMeta, mediaCartoesVermelhos = calcularMedias.calcularMedias(timePesquisado, listaTotal)
    
    print("Ultimo", mediaPosseDeBola)

    return (mediaGols, mediaEscanteios, mediaCartoes, mediaPosseDeBola, mediaChutesNoGol, mediaChutesParaFora, mediaImpedimentos, mediaChutesLivres, mediaAtaques, mediaLaterais, mediaTirosDeMeta, mediaCartoesVermelhos) 
