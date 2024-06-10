def criaListaTimes(listaJogos, idPartidas, escanteios, cartoes, posseDeBola, chutesGol, chutesFora, impedimentos, chutesLivres, ataques, lateraisCobrados, tirosDeMeta, cartoesVermelhos):
    listaTimes = []
    time = 0
    nomeTime2 = ""
    contador = 0
    contadorPosicao = 0

    for item in range(len(escanteios)):
        escanteios[item] = escanteios[item].replace('"', "")

    for item in range(len(cartoes)):
        cartoes[item] = cartoes[item].replace('"', "")

    for item in range(len(posseDeBola)):
        posseDeBola[item] = posseDeBola[item].replace('"', "")

    for item in range(len(chutesGol)):
        chutesGol[item] = chutesGol[item].replace('"', "")

    for item in range(len(chutesFora)):
        chutesFora[item] = chutesFora[item].replace('"', "")

    for item in range(len(impedimentos)):
        impedimentos[item] = impedimentos[item].replace('"', "")

    for item in range(len(chutesLivres)):
        chutesLivres[item] = chutesLivres[item].replace('"', "")

    for item in range(len(ataques)):
        ataques[item] = ataques[item].replace('"', "")

    for item in range(len(lateraisCobrados)):
        lateraisCobrados[item] = lateraisCobrados[item].replace('"', "")

    for item in range(len(tirosDeMeta)):
        tirosDeMeta[item] = tirosDeMeta[item].replace('"', "")

    for item in range(len(cartoesVermelhos)):
        cartoesVermelhos[item] = cartoesVermelhos[item].replace('"', "")

    for linhas in range (len(listaJogos)):
        if 'name' == listaJogos[linhas]:
            if time==0:
                listaTimes.append(idPartidas[contador])
                listaTimes.append(listaJogos[linhas+1])
                time = 1
            else:
                nomeTime2 = listaJogos[linhas+1]
                time=0
        if 'score' == listaJogos[linhas]:
            if time==1:
                listaTimes.append(listaJogos[linhas+1])
            else:
                listaTimes.append("X")
                listaTimes.append(listaJogos[linhas+1])
                listaTimes.append(nomeTime2)
                if (contador < len(escanteios)/2) and (contador< len(cartoes)/2) and (contador< len(posseDeBola)/2) and (contador< len(chutesGol)/2) and (contador< len(chutesFora)/2) and (contador< len(impedimentos)/2) and (contador< len(chutesLivres)/2) and (contador< len(ataques)/2) and (contador< len(lateraisCobrados)/2) and (contador< len(tirosDeMeta)/2) and (contador< len(cartoesVermelhos)/2) :
                    listaTimes.append("Escanteios:".lstrip())
                    listaTimes.append(escanteios[contadorPosicao])
                    listaTimes.append(escanteios[contadorPosicao+1])
                    listaTimes.append("Cartões:".lstrip())
                    listaTimes.append(cartoes[contadorPosicao])
                    listaTimes.append(cartoes[contadorPosicao+1])
                    listaTimes.append("Posse de Bola:".lstrip())
                    listaTimes.append(posseDeBola[contadorPosicao])
                    listaTimes.append(posseDeBola[contadorPosicao+1])
                    listaTimes.append("Chutes no Gol:".lstrip())
                    listaTimes.append(chutesGol[contadorPosicao])
                    listaTimes.append(chutesGol[contadorPosicao+1])
                    listaTimes.append("Chutes para Fora:".lstrip())
                    listaTimes.append(chutesFora[contadorPosicao])
                    listaTimes.append(chutesFora[contadorPosicao+1])
                    listaTimes.append("Impedimentos:".lstrip())
                    listaTimes.append(impedimentos[contadorPosicao])
                    listaTimes.append(impedimentos[contadorPosicao+1])
                    listaTimes.append("Chutes livres:".lstrip())
                    listaTimes.append(chutesLivres[contadorPosicao])
                    listaTimes.append(chutesLivres[contadorPosicao+1])
                    listaTimes.append("Ataques:".lstrip())
                    listaTimes.append(ataques[contadorPosicao])
                    listaTimes.append(ataques[contadorPosicao+1])
                    listaTimes.append("Laterais cobrados:".lstrip())
                    listaTimes.append(lateraisCobrados[contadorPosicao])
                    listaTimes.append(lateraisCobrados[contadorPosicao+1])
                    listaTimes.append("Tiros de Meta:".lstrip())
                    listaTimes.append(tirosDeMeta[contadorPosicao])
                    listaTimes.append(tirosDeMeta[contadorPosicao+1])
                    listaTimes.append("Cartões Vermelhos:".lstrip())
                    listaTimes.append(cartoesVermelhos[contadorPosicao])
                    listaTimes.append(cartoesVermelhos[contadorPosicao+1])
                else:
                    listaTimes.append("Escanteios:".lstrip())
                    listaTimes.append(0)
                    listaTimes.append(0)
                    listaTimes.append("Cartões:".lstrip())
                    listaTimes.append(0)
                    listaTimes.append(0)
                    listaTimes.append("Posse de Bola:".lstrip())
                    listaTimes.append(0)
                    listaTimes.append(0)
                    listaTimes.append("Chutes no Gol:".lstrip())
                    listaTimes.append(0)
                    listaTimes.append(0)
                    listaTimes.append("Chutes para Fora:".lstrip())
                    listaTimes.append(0)
                    listaTimes.append(0)
                    listaTimes.append("Impedimentos:".lstrip())
                    listaTimes.append(0)
                    listaTimes.append(0)
                    listaTimes.append("Chutes livres:".lstrip())
                    listaTimes.append(0)
                    listaTimes.append(0)
                    listaTimes.append("Ataques:".lstrip())
                    listaTimes.append(0)
                    listaTimes.append(0)
                    listaTimes.append("Laterais cobrados:".lstrip())
                    listaTimes.append(0)
                    listaTimes.append(0)
                    listaTimes.append("Tiros de Meta:".lstrip())
                    listaTimes.append(0)
                    listaTimes.append(0)
                    listaTimes.append("Cartões Vermelhos:".lstrip())
                    listaTimes.append(0)
                    listaTimes.append(0)
                contadorPosicao = contadorPosicao + 2
                contador = contador + 1
    return listaTimes