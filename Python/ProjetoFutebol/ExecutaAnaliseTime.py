from flask import Flask, request, jsonify
from flask_cors import CORS
import main as analise
import Funcoes.pesquisaTimes as pesquisa
import mysql.connector

app = Flask(__name__)
CORS(app, resources={
    r"/executaAnalise": {"origins": "*"},
    r"/pesquisaTimes": {"origins": "*"},
    r"/salvarAnotacao": {"origins": "*"},
    r"/carregarNotas": {"origins": "*"},
    r"/excluirNota/*": {"origins": "*"},
    r"/atualizarNota/*": {"origins": "*"}
})
# Configurações de conexão com o banco de dados
config = {
    'user': 'admin',
    'password': 'futviewpass',
    'host': 'database-futview.cz08g8ycqqvg.us-east-2.rds.amazonaws.com',
    'database': 'DbFutView'
}

# Função para executar a análise
@app.route('/executaAnalise')
def executaAnalise():
    try:
        time = request.args.get('time')
        quantidadeJogos = request.args.get('quantidadeJogos')

        print("Pesquisa no banco")
        # Conexão com o banco de dados
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        # Execute sua análise
        mediaGols, mediaEscanteios, mediaCartoes, mediaPosseDeBola, mediaChutesNoGol, mediaChutesParaFora, mediaImpedimentos, mediaChutesLivres, mediaAtaques, mediaLaterais, mediaTirosDeMeta, mediaCartoesVermelhos = analise.analisaDados(time, quantidadeJogos)

        print("Fez analise")
        # Feche o cursor e a conexão
        cursor.close()
        conn.close()

        print("Retorna dados")
        # Retorna os resultados da análise em formato JSON
        return jsonify({'Media Gols': mediaGols, 'Media Escanteios': mediaEscanteios, 'Media cartões': mediaCartoes, 'Media posse de bola': mediaPosseDeBola, 'Media chutes no gol': mediaChutesNoGol, 'Media chutes para fora': mediaChutesParaFora, 'Media impedimentos': mediaImpedimentos, 'Media chutes livres': mediaChutesLivres, 'Media ataques': mediaAtaques, 'Media laterais': mediaLaterais, 'Media tiros de meta': mediaTirosDeMeta, 'Media cartões vermelhos': mediaCartoesVermelhos}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Função para pesquisar times
@app.route('/pesquisaTimes')
def pesquisaTimes():
    try:
        time = request.args.get('time')
        pais = request.args.get('pais')

        if time is None and pais is not None:
            # Conexão com o banco de dados
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()

            # Execute sua pesquisa aqui, substituindo a chamada para pesquisa.pesquisaTimes()
            times = pesquisa.pesquisaTimes(pais)

            # Feche o cursor e a conexão
            cursor.close()
            conn.close()

            return jsonify({'Dados': times}), 200
        
        if time is not None and pais is None:
            # Conexão com o banco de dados
            conn = mysql.connector.connect(**config)
            cursor = conn.cursor()

            # Execute sua pesquisa aqui, substituindo a chamada para pesquisa.pegarCodigo()
            lista = pesquisa.pegarCodigo(time)
            codigo = int(lista[0])

            # Feche o cursor e a conexão
            cursor.close()
            conn.close()

            return jsonify(codigo), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/salvarAnotacao', methods=['POST'])
def salvarAnotacao():
    try:
        # Obtenha os dados enviados pelo cliente
        anotacao = request.json['anotacao']

        # Conexão com o banco de dados
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        # Execute a inserção de dados no banco de dados
        sql = "INSERT INTO tbnotas (texto) VALUES (%s)"
        cursor.execute(sql, (anotacao,))
        conn.commit()

        # Obtenha o ID da nota recém-inserida
        id_nota = cursor.lastrowid

        # Feche o cursor e a conexão
        cursor.close()
        conn.close()

        return jsonify({'message': 'Anotação salva com sucesso!', 'id': id_nota}), 200
    except Exception as e:
        print("Erro interno no servidor:", e)
        return jsonify({'error': str(e)}), 500
    
@app.route('/atualizarNota/<int:id_nota>', methods=['PUT'])
def atualizarNota(id_nota):
    try:
        # Obtenha os dados enviados pelo cliente
        dados = request.get_json()
        texto_nota = dados['anotacao']

        # Conexão com o banco de dados
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        # Execute a atualização de dados no banco de dados
        cursor.execute("UPDATE tbnotas SET texto = %s WHERE pkNotas = %s", (texto_nota, id_nota))
        conn.commit()

        # Feche o cursor e a conexão
        cursor.close()
        conn.close()

        return jsonify({'message': 'Nota atualizada com sucesso!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/carregarNotas', methods=['GET'])
def carregarNotas():
    try:
        # Conexão com o banco de dados
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        # Execute uma consulta para obter todas as notas do banco de dados
        cursor.execute("SELECT * FROM tbnotas")
        notas = cursor.fetchall()

        # Feche o cursor e a conexão
        cursor.close()
        conn.close()

        # Converter as notas para um formato adequado (por exemplo, lista de dicionários)
        notas_formatadas = [{'id': nota[0], 'texto': nota[1], 'cor': nota[2]} for nota in notas]

        # Retorna as notas em formato JSON
        return jsonify({'notas': notas_formatadas}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/excluirNota/<int:id_nota>', methods=['DELETE'])    
def excluirNota(id_nota):
    try:
        # Conexão com o banco de dados
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        # Execute uma consulta para excluir a nota do banco de dados
        cursor.execute("DELETE FROM tbnotas WHERE pkNotas = %s", (id_nota,))
        conn.commit()

        # Feche o cursor e a conexão
        cursor.close()
        conn.close()

        return jsonify({'message': 'Nota excluída com sucesso!'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)