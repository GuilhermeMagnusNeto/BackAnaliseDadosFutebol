def conectarBanco(host, usuario, senha, nome_banco):
    import mysql.connector

    # Estabeleça a conexão com o banco de dados
    conexao = mysql.connector.connect(
        host=host,  # Endereço do servidor MySQL
        user=usuario,  # Nome de usuário do MySQL
        password=senha,  # Senha do MySQL
        database=nome_banco  # Nome do banco de dados que você deseja conectar
    )

    # Verifique se a conexão foi estabelecida com sucesso
    if conexao.is_connected():
        return conexao
    else:
        print("Erro ao conectar-se com o banco de dados!")