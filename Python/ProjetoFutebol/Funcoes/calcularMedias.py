def calcularMedias(timePesquisado, listaTotal):
    #variáveis das médias
    mediaGolsCasa = 0
    mediaGolsFora = 0
    mediaGolsTotal = 0
    mediaGolsSofridosCasa = 0
    mediaGolsSofridosFora = 0
    mediaGolsSofridosTotal = 0
    #variáveis total de gols feitos
    totalGolsCasa = 0
    totalGolsFora = 0
    totalGols = 0
    #variáveis total de gols sofridos
    totalGolsSofridosCasa = 0
    totalGolsSofridosFora = 0
    totalGolsSofridos = 0

    #variável para quantidade de jogos em casa e fora
    quantidadeJogosCasa = 0
    quantidadeJogosFora = 0
    quantidadeJogosTotal = 0

    quantidadeJogosPosseCasa = 0
    quantidadeJogosPosseFora = 0
    quantidadeJogosPosseTotal = 0

    #variáveis das médias escanteios
    mediaEscanteiosCasa = 0
    mediaEscanteiosFora = 0
    mediaEscanteiosTotal = 0
    mediaEscanteiosSofridosCasa = 0
    mediaEscanteiosSofridosFora = 0
    mediaEscanteiosSofridosTotal = 0
    #variáveis total de escanteios feitos
    totalEscanteiosCasa = 0
    totalEscanteiosFora = 0
    totalEscanteios = 0
    #variáveis total de escanteios sofridos
    totalEscanteiosSofridosCasa = 0
    totalEscanteiosSofridosFora = 0
    totalEscanteiosSofridos = 0

    #variáveis das médias de cartões
    mediaCartoesCasa = 0
    mediaCartoesFora = 0
    mediaCartoesTotal = 0
    mediaCartoesSofridosCasa = 0
    mediaCartoesSofridosFora = 0
    mediaCartoesSofridosTotal = 0
    #variáveis total de Cartoes feitos
    totalCartoesCasa = 0
    totalCartoesFora = 0
    totalCartoes = 0
    #variáveis total de Cartoes sofridos
    totalCartoesSofridosCasa = 0
    totalCartoesSofridosFora = 0
    totalCartoesSofridos = 0

    #variáveis das média
    mediaPosseCasa = 0
    mediaPosseFora = 0
    mediaPosseTotal = 0
    mediaPosseSofridosCasa = 0
    mediaPosseSofridosFora = 0
    mediaPosseSofridosTotal = 0
    #variáveis total de Posse feitos
    totalPosseCasa = 0
    totalPosseFora = 0
    totalPosse = 0
    #variáveis total de Posse sofridos
    totalPosseSofridosCasa = 0
    totalPosseSofridosFora = 0
    totalPosseSofridos = 0

    #variáveis das média chutes no gol
    mediaChutesNoGolCasa = 0
    mediaChutesNoGolFora = 0
    mediaChutesNoGolTotal = 0
    mediaChutesNoGolSofridosCasa = 0
    mediaChutesNoGolSofridosFora = 0
    mediaChutesNoGolSofridosTotal = 0
    #variáveis total de mediaChutesNoGol feitos
    totalChutesNoGolCasa = 0
    totalChutesNoGolFora = 0
    totalChutesNoGol = 0
    #variáveis total de mediaChutesNoGol sofridos
    totalChutesNoGolSofridosCasa = 0
    totalChutesNoGolSofridosFora = 0
    totalChutesNoGolSofridos = 0

    #variáveis das média chutes para Fora
    mediaChutesParaForaCasa = 0
    mediaChutesParaForaFora = 0
    mediaChutesParaForaTotal = 0
    mediaChutesParaForaSofridosCasa = 0
    mediaChutesParaForaSofridosFora = 0
    mediaChutesParaForaSofridosTotal = 0
    #variáveis total de mediaChutesParaFora feitos
    totalChutesParaForaCasa = 0
    totalChutesParaForaFora = 0
    totalChutesParaFora = 0
    #variáveis total de mediaChutesParaFora sofridos
    totalChutesParaForaSofridosCasa = 0
    totalChutesParaForaSofridosFora = 0
    totalChutesParaForaSofridos = 0

    #variáveis das média impedimentos
    mediaimpedimentosCasa = 0
    mediaimpedimentosFora = 0
    mediaimpedimentosTotal = 0
    mediaimpedimentosSofridosCasa = 0
    mediaimpedimentosSofridosFora = 0
    mediaimpedimentosSofridosTotal = 0
    #variáveis total de impedimentos feitos
    totalimpedimentosCasa = 0
    totalimpedimentosFora = 0
    totalimpedimentos = 0
    #variáveis total de impedimentos sofridos
    totalimpedimentosSofridosCasa = 0
    totalimpedimentosSofridosFora = 0
    totalimpedimentosSofridos = 0

    #variáveis das média chutes para Fora
    mediaChutesLivresCasa = 0
    mediaChutesLivresFora = 0
    mediaChutesLivresTotal = 0
    mediaChutesLivresSofridosCasa = 0
    mediaChutesLivresSofridosFora = 0
    mediaChutesLivresSofridosTotal = 0
    #variáveis total de mediaChutesLivres feitos
    totalChutesLivresCasa = 0
    totalChutesLivresFora = 0
    totalChutesLivres = 0
    #variáveis total de mediaChutesLivres sofridos
    totalChutesLivresSofridosCasa = 0
    totalChutesLivresSofridosFora = 0
    totalChutesLivresSofridos = 0

    #variáveis das média ataques
    mediaAtaquesCasa = 0
    mediaAtaquesFora = 0
    mediaAtaquesTotal = 0
    mediaAtaquesSofridosCasa = 0
    mediaAtaquesSofridosFora = 0
    mediaAtaquesSofridosTotal = 0
    #variáveis total de mediaAtaques feitos
    totalAtaquesCasa = 0
    totalAtaquesFora = 0
    totalAtaques = 0
    #variáveis total de mediaAtaques sofridos
    totalAtaquesSofridosCasa = 0
    totalAtaquesSofridosFora = 0
    totalAtaquesSofridos = 0

    #variáveis das média laterais
    mediaLateraisCasa = 0
    mediaLateraisFora = 0
    mediaLateraisTotal = 0
    mediaLateraisSofridosCasa = 0
    mediaLateraisSofridosFora = 0
    mediaLateraisSofridosTotal = 0
    #variáveis total de mediaLaterais feitos
    totalLateraisCasa = 0
    totalLateraisFora = 0
    totalLaterais = 0
    #variáveis total de mediaLaterais sofridos
    totalLateraisSofridosCasa = 0
    totalLateraisSofridosFora = 0
    totalLateraisSofridos = 0

    #variáveis das média tiros de meta
    mediaTirosDeMetaCasa = 0
    mediaTirosDeMetaFora = 0
    mediaTirosDeMetaTotal = 0
    mediaTirosDeMetaSofridosCasa = 0
    mediaTirosDeMetaSofridosFora = 0
    mediaTirosDeMetaSofridosTotal = 0
    #variáveis total de mediaTirosDeMeta feitos
    totalTirosDeMetaCasa = 0
    totalTirosDeMetaFora = 0
    totalTirosDeMeta = 0
    #variáveis total de mediaTirosDeMeta sofridos
    totalTirosDeMetaSofridosCasa = 0
    totalTirosDeMetaSofridosFora = 0
    totalTirosDeMetaSofridos = 0

    #variáveis das média cartões vermelhos
    mediaCartoesVermelhosCasa = 0
    mediaCartoesVermelhosFora = 0
    mediaCartoesVermelhosTotal = 0
    mediaCartoesVermelhosSofridosCasa = 0
    mediaCartoesVermelhosSofridosFora = 0
    mediaCartoesVermelhosSofridosTotal = 0
    #variáveis total de mediaCartoesVermelhos feitos
    totalCartoesVermelhosCasa = 0
    totalCartoesVermelhosFora = 0
    totalCartoesVermelhos = 0
    #variáveis total de mediaCartoesVermelhos sofridos
    totalCartoesVermelhosSofridosCasa = 0
    totalCartoesVermelhosSofridosFora = 0
    totalCartoesVermelhosSofridos = 0


    # descobrindo o nome do time que foi pesquisado
    if timePesquisado == 0:
        nomeTimePesquisado = listaTotal[1]
    elif timePesquisado == 1:
        nomeTimePesquisado = listaTotal[5]
        
    for contador in range(0, len(listaTotal), 39):
        if contador + 1 < len(listaTotal):
            if listaTotal[contador+1] == nomeTimePesquisado:
                if listaTotal[contador+2] == "-1.0" or listaTotal[contador+4] == "-1.0":
                    continue
                else:
                    totalGolsCasa = totalGolsCasa + float(listaTotal[contador+2])
                    totalGolsSofridosCasa = totalGolsSofridosCasa + float(listaTotal[contador+4])
                    totalEscanteiosCasa += float(listaTotal[contador+7])
                    totalEscanteiosSofridosCasa += float(listaTotal[contador+8])
                    totalCartoesCasa = totalCartoesCasa+float(listaTotal[contador+10])
                    totalCartoesSofridosCasa = totalCartoesSofridosCasa+float(listaTotal[contador+11])
                    if listaTotal[contador + 13] != '0%' and listaTotal[contador + 13] != '100%':
                        totalPosseCasa = totalPosseCasa+float(listaTotal[contador+13].strip('%'))
                        totalPosseSofridosCasa = totalPosseSofridosCasa+float(listaTotal[contador+14].strip('%'))
                        quantidadeJogosPosseCasa += 1
                        print("Posse Casa", totalPosseCasa, totalPosseSofridosCasa)
                    totalChutesNoGolCasa = totalChutesNoGolCasa+float(listaTotal[contador+16])
                    totalChutesNoGolSofridosCasa = totalChutesNoGolSofridosCasa+float(listaTotal[contador+17])
                    totalChutesParaForaCasa = totalChutesParaForaCasa+float(listaTotal[contador+19])
                    totalChutesParaForaSofridosCasa = totalChutesParaForaSofridosCasa+float(listaTotal[contador+20])
                    totalimpedimentosCasa = totalimpedimentosCasa+float(listaTotal[contador+22])
                    totalimpedimentosSofridosCasa = totalimpedimentosSofridosCasa+float(listaTotal[contador+23])
                    totalChutesLivresCasa = totalChutesLivresCasa+float(listaTotal[contador+25])
                    totalChutesLivresSofridosCasa = totalChutesLivresSofridosCasa+float(listaTotal[contador+26])
                    totalAtaquesCasa = totalAtaquesCasa+float(listaTotal[contador+28])
                    totalAtaquesSofridosCasa = totalAtaquesSofridosCasa+float(listaTotal[contador+29])
                    totalLateraisCasa = totalLateraisCasa+float(listaTotal[contador+31])
                    totalLateraisSofridosCasa = totalLateraisSofridosCasa+float(listaTotal[contador+32])
                    totalTirosDeMetaCasa = totalTirosDeMetaCasa+float(listaTotal[contador+34])
                    totalTirosDeMetaSofridosCasa = totalTirosDeMetaSofridosCasa+float(listaTotal[contador+35])
                    totalCartoesVermelhosCasa = totalCartoesVermelhosCasa+float(listaTotal[contador+37])
                    totalCartoesVermelhosSofridosCasa = totalCartoesVermelhosSofridosCasa+float(listaTotal[contador+38])
                    quantidadeJogosCasa += 1
                    
            else:
                if listaTotal[contador+2] == "-1.0" or listaTotal[contador+4] == "-1.0":
                    continue
                else:
                    if contador + 4 < len(listaTotal):
                        totalGolsFora = totalGolsFora + float(listaTotal[contador+4])
                        totalGolsSofridosFora = totalGolsSofridosFora + float(listaTotal[contador+2])
                        quantidadeJogosFora += 1

                    if contador + 8 < len(listaTotal):
                        totalEscanteiosFora += float(listaTotal[contador+8])
                        totalEscanteiosSofridosFora += float(listaTotal[contador+7])

                    if contador + 11 < len(listaTotal):
                        totalCartoesFora = totalCartoesFora+float(listaTotal[contador+11])
                        totalCartoesSofridosFora = totalCartoesSofridosFora+float(listaTotal[contador+10])

                    if contador + 14 < len(listaTotal):
                        if listaTotal[contador + 13] != '0%' and listaTotal[contador + 13] != '100%':
                            totalPosseFora = totalPosseCasa+float(listaTotal[contador+14].strip('%'))
                            totalPosseSofridosFora = totalPosseSofridosCasa+float(listaTotal[contador+13].strip('%'))
                            quantidadeJogosPosseFora += 1
                            print("Posse Fora", totalPosseFora, totalPosseSofridosFora)

                    if contador + 17 < len(listaTotal):
                        totalChutesNoGolFora = totalChutesNoGolFora+float(listaTotal[contador+17])
                        totalChutesNoGolSofridosFora = totalChutesNoGolSofridosFora+float(listaTotal[contador+16])

                    if contador + 20 < len(listaTotal):
                        totalChutesParaForaFora = totalChutesParaForaFora+float(listaTotal[contador+20])
                        totalChutesParaForaSofridosFora = totalChutesParaForaSofridosFora+float(listaTotal[contador+19])

                    if contador + 23 < len(listaTotal):
                        totalimpedimentosFora = totalimpedimentosFora+float(listaTotal[contador+23])
                        totalimpedimentosSofridosFora = totalimpedimentosSofridosFora+float(listaTotal[contador+22])

                    if contador + 26 < len(listaTotal):
                        totalChutesLivresFora = totalChutesLivresFora+float(listaTotal[contador+26])
                        totalChutesLivresSofridosFora = totalChutesLivresSofridosFora+float(listaTotal[contador+25])

                    if contador + 29 < len(listaTotal):
                        totalAtaquesFora = totalAtaquesFora+float(listaTotal[contador+28])
                        totalAtaquesSofridosFora = totalAtaquesSofridosFora+float(listaTotal[contador+29])

                    if contador + 32 < len(listaTotal):
                        totalLateraisFora = totalLateraisFora+float(listaTotal[contador+32])
                        totalLateraisSofridosFora = totalLateraisSofridosFora+float(listaTotal[contador+31])

                    if contador + 35 < len(listaTotal):
                        totalTirosDeMetaFora = totalTirosDeMetaFora+float(listaTotal[contador+35])
                        totalTirosDeMetaSofridosFora = totalTirosDeMetaSofridosFora+float(listaTotal[contador+34])

                    if contador + 38 < len(listaTotal):
                        totalCartoesVermelhosFora = totalCartoesVermelhosFora+float(listaTotal[contador+38])
                        totalCartoesVermelhosSofridosFora = totalCartoesVermelhosSofridosFora+float(listaTotal[contador+37])

    #calculo dos totais de escanteios
    totalEscanteios = totalEscanteiosFora + totalEscanteiosCasa
    totalEscanteiosSofridos = totalEscanteiosSofridosFora + totalEscanteiosSofridosCasa
    quantidadeJogosTotal = quantidadeJogosFora + quantidadeJogosCasa
    quantidadeJogosPosseTotal = quantidadeJogosPosseCasa + quantidadeJogosPosseFora
    print("Quantidade jogos posse total ", quantidadeJogosPosseTotal)

    #Calcuo média escanteios
    if quantidadeJogosCasa > 0:
        mediaEscanteiosCasa = totalEscanteiosCasa/quantidadeJogosCasa
        mediaEscanteiosSofridosCasa = totalEscanteiosSofridosCasa/quantidadeJogosCasa
    if quantidadeJogosFora > 0:
        mediaEscanteiosFora = totalEscanteiosFora/quantidadeJogosFora
        mediaEscanteiosSofridosFora = totalEscanteiosSofridosFora/quantidadeJogosFora
    if quantidadeJogosTotal > 0:
        mediaEscanteiosTotal = totalEscanteios/quantidadeJogosTotal
        mediaEscanteiosSofridosTotal = totalEscanteiosSofridos/quantidadeJogosTotal

    mediaEscanteios = [round(mediaEscanteiosCasa,2), round(mediaEscanteiosSofridosCasa,2), round(mediaEscanteiosTotal,2), round(mediaEscanteiosFora,2), round(mediaEscanteiosSofridosFora,2), round(mediaEscanteiosSofridosTotal,2)]        

    #calculo dos totais de gols
    totalGols = totalGolsFora + totalGolsCasa
    totalGolsSofridos = totalGolsSofridosFora + totalGolsSofridosCasa

    #calculo da media de gols
    if quantidadeJogosCasa > 0:
        mediaGolsCasa = totalGolsCasa/quantidadeJogosCasa
        mediaGolsSofridosCasa = totalGolsSofridosCasa/quantidadeJogosCasa
 
    if quantidadeJogosFora > 0:
        mediaGolsFora = totalGolsFora/quantidadeJogosFora
        mediaGolsSofridosFora = totalGolsSofridosFora/quantidadeJogosFora

    if quantidadeJogosTotal > 0:
        mediaGolsTotal = totalGols/quantidadeJogosTotal
        mediaGolsSofridosTotal = totalGolsSofridos/quantidadeJogosTotal

    mediaGols = [round(mediaGolsCasa,2), round(mediaGolsSofridosCasa,2), round(mediaGolsTotal,2), round(mediaGolsFora,2), round(mediaGolsSofridosFora,2), round(mediaGolsSofridosTotal,2)]

    #calculo dos totais de Cartoes
    totalCartoes = totalCartoesFora + totalCartoesCasa
    totalCartoesSofridos = totalCartoesSofridosFora + totalCartoesSofridosCasa

    #Calculo de Cartões
    if quantidadeJogosCasa>0:
        mediaCartoesCasa = totalCartoesCasa/quantidadeJogosCasa
        mediaCartoesSofridosCasa = totalCartoesSofridosCasa/quantidadeJogosCasa
    if quantidadeJogosFora>0:
        mediaCartoesFora = totalCartoesFora/quantidadeJogosFora
        mediaCartoesSofridosFora = totalCartoesSofridosFora/quantidadeJogosFora
    if quantidadeJogosTotal>0:
        mediaCartoesTotal = totalCartoes/quantidadeJogosTotal
        mediaCartoesSofridosTotal = totalCartoesSofridos/quantidadeJogosTotal 

    mediaCartoes = [round(mediaCartoesCasa,2), round(mediaCartoesSofridosCasa,2), round(mediaCartoesTotal,2), round(mediaCartoesFora,2), round(mediaCartoesSofridosFora,2), round(mediaCartoesSofridosTotal,2)]

    #calculo dos total de Posse
    totalPosse = totalPosseFora + totalPosseCasa
    totalPosseSofridos = totalPosseSofridosFora + totalPosseSofridosCasa

    #calculo da media da posse de bola
    if quantidadeJogosPosseCasa>0: 
        mediaPosseCasa = totalPosseCasa/quantidadeJogosPosseCasa
        mediaPosseSofridosCasa = totalPosseSofridosCasa/quantidadeJogosPosseCasa 
    if quantidadeJogosPosseFora>0:
        mediaPosseFora = totalPosseFora/quantidadeJogosPosseFora
        mediaPosseSofridosFora = totalPosseSofridosFora/quantidadeJogosPosseFora
    if quantidadeJogosPosseTotal>0:
        mediaPosseTotal = totalPosse/quantidadeJogosPosseTotal
        mediaPosseSofridosTotal = totalPosseSofridos/quantidadeJogosPosseTotal
    
    print("Médias ", mediaPosseCasa, mediaPosseSofridosCasa, mediaPosseFora, mediaPosseSofridosFora, mediaPosseTotal, mediaPosseSofridosTotal)

    mediaPosseDeBola = [round(mediaPosseCasa,2), round(mediaPosseSofridosCasa,2), round(mediaPosseTotal,2), round(mediaPosseFora,2), round(mediaPosseSofridosFora,2), round(mediaPosseSofridosTotal,2)]



    #calculo dos totais de chutes no gol
    totalChutesNoGol = totalChutesNoGolFora + totalChutesNoGolCasa
    totalChutesNoGolSofridos = totalChutesNoGolSofridosFora + totalChutesNoGolSofridosCasa

    #Calculo de Chutes no Gol
    if quantidadeJogosCasa>0:
        mediaChutesNoGolCasa = totalChutesNoGolCasa/quantidadeJogosCasa
        mediaChutesNoGolSofridosCasa = totalChutesNoGolSofridosCasa/quantidadeJogosCasa
    if quantidadeJogosFora>0:
        mediaChutesNoGolFora = totalChutesNoGolFora/quantidadeJogosFora
        mediaChutesNoGolSofridosFora = totalChutesNoGolSofridosFora/quantidadeJogosFora
    if quantidadeJogosTotal>0:
        mediaChutesNoGolTotal = totalChutesNoGol/quantidadeJogosTotal
        mediaChutesNoGolSofridosTotal = totalChutesNoGolSofridos/quantidadeJogosTotal 
    
    mediaChutesNoGol = [round(mediaChutesNoGolCasa,2), round(mediaChutesNoGolSofridosCasa,2), round(mediaChutesNoGolTotal,2), round(mediaChutesNoGolFora,2), round(mediaChutesNoGolSofridosFora,2), round(mediaChutesNoGolSofridosTotal,2)]
    
    #calculo dos totais de chutes para fora
    totalChutesParaFora = totalChutesParaForaFora + totalChutesParaForaCasa
    totalChutesParaForaSofridos = totalChutesParaForaSofridosFora + totalChutesParaForaSofridosCasa
    
    #Calculo de Chutes para fora
    if quantidadeJogosCasa>0:
        mediaChutesParaForaCasa = totalChutesParaForaCasa/quantidadeJogosCasa
        mediaChutesParaForaSofridosCasa = totalChutesParaForaSofridosCasa/quantidadeJogosCasa
    if quantidadeJogosFora>0:
        mediaChutesParaForaFora = totalChutesParaForaFora/quantidadeJogosFora
        mediaChutesParaForaSofridosFora = totalChutesParaForaSofridosFora/quantidadeJogosFora
    if quantidadeJogosTotal>0:
        mediaChutesParaForaTotal = totalChutesParaFora/quantidadeJogosTotal
        mediaChutesParaForaSofridosTotal = totalChutesParaForaSofridos/quantidadeJogosTotal 

    mediaChutesParaFora = [round(mediaChutesParaForaCasa,2), round(mediaChutesParaForaSofridosCasa,2), round(mediaChutesParaForaTotal,2), round(mediaChutesParaForaFora,2), round(mediaChutesParaForaSofridosFora,2), round(mediaChutesParaForaSofridosTotal,2)]

    #calculo dos totais de chutes para fora
    totalimpedimentos= totalimpedimentosFora + totalimpedimentosCasa
    totalimpedimentosSofridos = totalimpedimentosSofridosFora + totalimpedimentosSofridosCasa
    
    #Calculo de Chutes para fora
    if quantidadeJogosCasa>0:
        mediaimpedimentosCasa = totalimpedimentosCasa/quantidadeJogosCasa
        mediaimpedimentosSofridosCasa = totalimpedimentosSofridosCasa/quantidadeJogosCasa
    if quantidadeJogosFora>0:
        mediaimpedimentosFora = totalimpedimentosFora/quantidadeJogosFora
        mediaimpedimentosSofridosFora = totalimpedimentosSofridosFora/quantidadeJogosFora
    if quantidadeJogosTotal>0:
        mediaimpedimentosTotal = totalimpedimentos/quantidadeJogosTotal
        mediaimpedimentosSofridosTotal = totalimpedimentosSofridos/quantidadeJogosTotal 

    mediaimpedimentos = [round(mediaimpedimentosCasa,2), round(mediaimpedimentosSofridosCasa,2), round(mediaimpedimentosTotal,2), round(mediaimpedimentosFora,2), round(mediaimpedimentosSofridosFora,2), round(mediaimpedimentosSofridosTotal,2)]
    
    #calculo dos totais de chutes para fora
    totalChutesLivres = totalChutesLivresFora + totalChutesLivresCasa
    totalChutesLivresSofridos = totalChutesLivresSofridosFora + totalChutesLivresSofridosCasa
    
    #Calculo de Chutes para fora
    if quantidadeJogosCasa>0:
        mediaChutesLivresCasa = totalChutesLivresCasa/quantidadeJogosCasa
        mediaChutesLivresSofridosCasa = totalChutesLivresSofridosCasa/quantidadeJogosCasa
    if quantidadeJogosFora>0:
        mediaChutesLivresFora = totalChutesLivresFora/quantidadeJogosFora
        mediaChutesLivresSofridosFora = totalChutesLivresSofridosFora/quantidadeJogosFora
    if quantidadeJogosTotal>0:
        mediaChutesLivresTotal = totalChutesLivres/quantidadeJogosTotal
        mediaChutesLivresSofridosTotal = totalChutesLivresSofridos/quantidadeJogosTotal 

    mediaChutesLivres = [round(mediaChutesLivresCasa,2), round(mediaChutesLivresSofridosCasa,2), round(mediaChutesLivresTotal,2), round(mediaChutesLivresFora,2), round(mediaChutesLivresSofridosFora,2), round(mediaChutesLivresSofridosTotal,2)]

    #calculo dos totais de chutes para fora
    totalAtaques = totalAtaquesFora + totalAtaquesCasa
    totalAtaquesSofridos = totalAtaquesSofridosFora + totalAtaquesSofridosCasa
    
    #Calculo de Chutes para fora
    if quantidadeJogosCasa>0:
        mediaAtaquesCasa = totalAtaquesCasa/quantidadeJogosCasa
        mediaAtaquesSofridosCasa = totalAtaquesSofridosCasa/quantidadeJogosCasa
    if quantidadeJogosFora>0:
        mediaAtaquesFora = totalAtaquesFora/quantidadeJogosFora
        mediaAtaquesSofridosFora = totalAtaquesSofridosFora/quantidadeJogosFora
    if quantidadeJogosTotal>0:
        mediaAtaquesTotal = totalAtaques/quantidadeJogosTotal
        mediaAtaquesSofridosTotal = totalAtaquesSofridos/quantidadeJogosTotal 

    mediaAtaques = [round(mediaAtaquesCasa,2), round(mediaAtaquesSofridosCasa,2), round(mediaAtaquesTotal,2), round(mediaAtaquesFora,2), round(mediaAtaquesSofridosFora,2), round(mediaAtaquesSofridosTotal,2)]

    #calculo dos totais de chutes para fora
    totalLaterais = totalLateraisFora + totalLateraisCasa
    totalLateraisSofridos = totalLateraisSofridosFora + totalLateraisSofridosCasa
    
    #Calculo de Chutes para fora
    if quantidadeJogosCasa>0:
        mediaLateraisCasa = totalLateraisCasa/quantidadeJogosCasa
        mediaLateraisSofridosCasa = totalLateraisSofridosCasa/quantidadeJogosCasa
    if quantidadeJogosFora>0:
        mediaLateraisFora = totalLateraisFora/quantidadeJogosFora
        mediaLateraisSofridosFora = totalLateraisSofridosFora/quantidadeJogosFora
    if quantidadeJogosTotal>0:
        mediaLateraisTotal = totalLaterais/quantidadeJogosTotal
        mediaLateraisSofridosTotal = totalLateraisSofridos/quantidadeJogosTotal 

    mediaLaterais = [round(mediaLateraisCasa,2), round(mediaLateraisSofridosCasa,2), round(mediaLateraisTotal,2), round(mediaLateraisFora,2), round(mediaLateraisSofridosFora,2), round(mediaLateraisSofridosTotal,2)]

    #calculo dos totais de chutes para fora
    totalTirosDeMeta = totalTirosDeMetaFora + totalTirosDeMetaCasa
    totalTirosDeMetaSofridos = totalTirosDeMetaSofridosFora + totalTirosDeMetaSofridosCasa
    
    #Calculo de Chutes para fora
    if quantidadeJogosCasa>0:
        mediaTirosDeMetaCasa = totalTirosDeMetaCasa/quantidadeJogosCasa
        mediaTirosDeMetaSofridosCasa = totalTirosDeMetaSofridosCasa/quantidadeJogosCasa
    if quantidadeJogosFora>0:
        mediaTirosDeMetaFora = totalTirosDeMetaFora/quantidadeJogosFora
        mediaTirosDeMetaSofridosFora = totalTirosDeMetaSofridosFora/quantidadeJogosFora
    if quantidadeJogosTotal>0:
        mediaTirosDeMetaTotal = totalTirosDeMeta/quantidadeJogosTotal
        mediaTirosDeMetaSofridosTotal = totalTirosDeMetaSofridos/quantidadeJogosTotal 

    mediaTirosDeMeta = [round(mediaTirosDeMetaCasa,2), round(mediaTirosDeMetaSofridosCasa,2), round(mediaTirosDeMetaTotal,2), round(mediaTirosDeMetaFora,2), round(mediaTirosDeMetaSofridosFora,2), round(mediaTirosDeMetaSofridosTotal,2)]

    #calculo dos totais de chutes para fora
    totalCartoesVermelhos = totalCartoesVermelhosFora + totalCartoesVermelhosCasa
    totalCartoesVermelhosSofridos = totalCartoesVermelhosSofridosFora + totalCartoesVermelhosSofridosCasa
    
    #Calculo de Chutes para fora
    if quantidadeJogosCasa>0:
        mediaCartoesVermelhosCasa = totalCartoesVermelhosCasa/quantidadeJogosCasa
        mediaCartoesVermelhosSofridosCasa = totalCartoesVermelhosSofridosCasa/quantidadeJogosCasa
    if quantidadeJogosFora>0:
        mediaCartoesVermelhosFora = totalCartoesVermelhosFora/quantidadeJogosFora
        mediaCartoesVermelhosSofridosFora = totalCartoesVermelhosSofridosFora/quantidadeJogosFora
    if quantidadeJogosTotal>0:
        mediaCartoesVermelhosTotal = totalCartoesVermelhos/quantidadeJogosTotal
        mediaCartoesVermelhosSofridosTotal = totalCartoesVermelhosSofridos/quantidadeJogosTotal 

    mediaCartoesVermelhos = [round(mediaCartoesVermelhosCasa,2), round(mediaCartoesVermelhosSofridosCasa,2), round(mediaCartoesVermelhosTotal,2), round(mediaCartoesVermelhosFora,2), round(mediaCartoesVermelhosSofridosFora,2), round(mediaCartoesVermelhosSofridosTotal,2)]

    return(mediaGols, mediaEscanteios, mediaCartoes, mediaPosseDeBola, mediaChutesNoGol, mediaChutesParaFora, mediaimpedimentos, mediaChutesLivres, mediaAtaques, mediaLaterais, mediaTirosDeMeta, mediaCartoesVermelhos);