def valorMedias(idPartidas): 
    import requests
    import re

    #Faz a raspagem de dados e pega os valores dos escanteios e cartões
    contador = 0
    chutesGol = []
    chutesFora = []
    chutesLivres = []
    escanteios = []
    cartoes = []
    cartoesVermelhos = []
    posseDeBola = []
    impedimentos = []
    ataques = []
    lateraisCobrados = []
    tirosDeMeta = []
    encontrouPosse = 0
    encontrouEscanteio = 0
    encontrouCartao = 0
    encontrouCartaoVermelho = 0
    encontrouChutesGol = 0
    encontrouChutesFora = 0
    encontrouImpedimento = 0
    encontrouChutesLivres = 0
    encontrouAtaques = 0
    encontrouLaterais = 0
    encontrouTirosDeMeta = 0

    while(contador < len(idPartidas)):
        url = "https://webws.365scores.com/web/game/stats/?"
        # https://webws.365scores.com/web/game/stats/?appTypeId=5&langId=31&timezoneName=America/Sao_Paulo&userCountryId=21&games=4063395

        querystring = {"appTypeId":"5","langId":"31","timezoneName":"America/Sao_Paulo","userCountryId":"21","games":idPartidas[contador]}

        payload = ""
        response = requests.request("GET", url, data=payload, params=querystring)
        lista = []
        lista = re.split('[,:=&]', response.text)

        #DEVO PEGAR AS DEMAIS INFORMAÇÕES AQUII

        for item in range(len(lista)):
            if '"Posse de bola"' == lista[item]:
                print("ACHOUUU: ", lista[item], lista[item+9], lista[item+10])
                if '"Posse de bola"' == lista[item] and lista[item+9] == '"value"':                    
                    encontrouPosse = 1
                    posseDeBola.append(lista[item+10])

            if '"Escanteios"' == lista[item] and lista[item+9] == '"value"':
                encontrouEscanteio = 1
                escanteios.append(lista[item+10])

            if '"Cartões amarelos"' == lista[item] and lista[item+9] == '"value"':
                encontrouCartao = 1
                cartoes.append(lista[item+10])

            if '"Cartões vermelhos"' == lista[item] and lista[item+9] == '"value"':
                encontrouCartaoVermelho = 1
                cartoesVermelhos.append(lista[item+10])

            if '"Chutes no gol"' == lista[item] and lista[item+9] == '"value"':
                encontrouChutesGol = 1
                chutesGol.append(lista[item+10])

            if '"Chutes para fora"' == lista[item] and lista[item+9] == '"value"':
                encontrouChutesFora = 1
                chutesFora.append(lista[item+10])

            if '"Impedimentos"' == lista[item] and lista[item+9] == '"value"':
                encontrouImpedimento = 1
                impedimentos.append(lista[item+10])

            if '"Chutes livres"' == lista[item] and lista[item+9] == '"value"':
                encontrouChutesLivres = 1
                chutesLivres.append(lista[item+10])

            if '11' == lista[item] and '"Ataque"' == lista[item+2] and lista[item+11] == '"value"':
                encontrouAtaques = 1
                ataques.append(lista[item+12])

            if '"Laterais cobrados"' == lista[item] and lista[item+9] == '"value"':
                encontrouLaterais = 1
                lateraisCobrados.append(lista[item+10])

            if '"Tiros de meta"' == lista[item] and lista[item+9] == '"value"':
                encontrouTirosDeMeta = 1
                tirosDeMeta.append(lista[item+10])
        
    
        if encontrouPosse == 0:
            posseDeBola.append('"0%"')
            posseDeBola.append('"0%"')
        else:
            encontrouPosse = 0

        if encontrouEscanteio == 0:
            escanteios.append('"0"')
            escanteios.append('"0"')
        else:
            encontrouEscanteio = 0

        if encontrouCartao == 0:
            cartoes.append('"0"')
            cartoes.append('"0"')
        else:
            encontrouCartao = 0

        if encontrouCartaoVermelho == 0:
            cartoesVermelhos.append('"0"')
            cartoesVermelhos.append('"0"')
        else:
            encontrouCartaoVermelho = 0

        if encontrouChutesGol == 0:
            chutesGol.append('"0"')
            chutesGol.append('"0"')
        else:
            encontrouChutesGol = 0

        if encontrouChutesFora == 0:
            chutesFora.append('"0"')
            chutesFora.append('"0"')
        else:
            encontrouChutesFora = 0

        if encontrouImpedimento == 0:
            impedimentos.append('"0"')
            impedimentos.append('"0"')
        else:
            encontrouImpedimento = 0

        if encontrouChutesLivres == 0:
            chutesLivres.append('"0"')
            chutesLivres.append('"0"')
        else:
            encontrouChutesLivres = 0

        if encontrouAtaques == 0:
            ataques.append('"0"')
            ataques.append('"0"')
        else:
            encontrouAtaques = 0

        if encontrouLaterais == 0:
            lateraisCobrados.append('"0"')
            lateraisCobrados.append('"0"')
        else:
            encontrouLaterais = 0

        if encontrouTirosDeMeta == 0:
            tirosDeMeta.append('"0"')
            tirosDeMeta.append('"0"')
        else:
            encontrouTirosDeMeta = 0

        contador = contador + 1

    return posseDeBola, escanteios, cartoes, chutesGol, chutesFora, impedimentos, chutesLivres, ataques, lateraisCobrados, tirosDeMeta, cartoesVermelhos
