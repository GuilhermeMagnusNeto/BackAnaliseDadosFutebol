import re
def criaListaJogos(lista, quantidadeJogos):
    listaJogos = []
    quantidade = int(quantidadeJogos)
    linhas = 0
    while linhas < len(lista) and quantidade > 0:
        if '"homeCompetitor"' in lista[linhas]:
            jogoInicio = linhas
        if '"isHomeAwayInverted"' in lista[linhas]:
            jogoFinal = linhas
            while jogoInicio < jogoFinal:
                listaJogos.append(lista[jogoInicio])
                jogoInicio += 1
            quantidade -= 1
        linhas += 1
    listaJogos = [re.sub(r'"', '', i) for i in listaJogos]
    return listaJogos
