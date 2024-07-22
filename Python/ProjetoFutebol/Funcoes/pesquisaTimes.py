import Funcoes.conexao as conexaoBanco


def pesquisaTimes(pais):
    if pais != 'padrao':
        try:
            conexao = conexaoBanco.conectarBanco(
                "mysqlserver.czi6aewaekiq.us-east-2.rds.amazonaws.com", "admin", "futviewpass", "DbFutView")
            cursor = conexao.cursor()

            consulta = "SELECT p.pkPais FROM tbpais p where upper(p.nomePais) = upper(%s)"
            cursor.execute(consulta, (pais,))

            resultados = cursor.fetchall()

            consulta = "SELECT t.nomeTimes, p.nomePais FROM tbtimes t INNER JOIN tbpais p ON p.pkPais = t.fkPais WHERE t.fkPais = %s ORDER BY p.pkPais, t.nomeTimes"
            cursor.execute(consulta, (resultados[0][0],))

            resultados = cursor.fetchall()
            times = []
            for linha in resultados:
                times.append(linha[0])

            cursor.close()
            conexao.close()

            return times
        except Exception as e:
            raise e
    else:
        try:
            conexao = conexaoBanco.conectarBanco(
                "mysqlserver.czi6aewaekiq.us-east-2.rds.amazonaws.com", "admin", "futviewpass", "DbFutView")
            cursor = conexao.cursor()

            consulta = "SELECT p.nomePais FROM tbpais p where p.pkPais IN (select t.fkPais from tbtimes t)"
            cursor.execute(consulta)

            resultados = cursor.fetchall()

            paises = []
            for linha in resultados:
                paises.append(linha[0])

            cursor.close()
            conexao.close()

            return paises
        except Exception as e:
            raise e


def pegarCodigo(time):
    conexao = conexaoBanco.conectarBanco(
        "mysqlserver.czi6aewaekiq.us-east-2.rds.amazonaws.com", "admin", "futviewpass", "DbFutView")
    cursor = conexao.cursor()

    consulta = "SELECT t.pkTimes FROM tbtimes t where upper(t.nomeTimes) = upper(%s)"
    cursor.execute(consulta, (time,))

    resultados = cursor.fetchall()

    times = []
    for linha in resultados:
        times.append(linha[0])

    cursor.close()
    conexao.close()

    return times
