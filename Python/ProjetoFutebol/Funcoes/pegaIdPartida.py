def idPartida(lista, quantidadeJogos):
    idPartidas = []
    quantidade = int(quantidadeJogos)
    linhas = 0
    while linhas < len(lista) and quantidade > 0:
        if ('[{"id"' in lista[linhas] and '"sportId"' in lista[linhas+2]) or ('{"id"' in lista[linhas] and '"sportId"' in lista[linhas+2]):
            idPartidas.append(lista[linhas+1])
            quantidade = quantidade - 1
        linhas += 1
    return idPartidas
