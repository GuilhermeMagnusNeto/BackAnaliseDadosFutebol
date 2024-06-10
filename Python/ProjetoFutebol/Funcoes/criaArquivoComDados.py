def criaArquivo(listaTimes, quantidadeJogos):
    contador=0;

    with open('dados.txt', 'w', encoding="utf-8") as arquivo:
        for item in listaTimes:
            if (contador==(39*int(quantidadeJogos))):
                break
            elif (contador==0):
                print(item, file=arquivo)
            elif (contador%39 == 0):
                print(("\n")+item, file=arquivo)
            else:
                print(item, file=arquivo)
            contador=contador+1
    arquivo.close();
