from flask import Flask, request, jsonify
from flask_cors import CORS
from functools import wraps
import main as analise
import Funcoes.pesquisaTimes as pesquisa
import mysql.connector
import jwt
import datetime

SECRET_KEY = 'VerificaLoginPass'

app = Flask(__name__)
CORS(app, resources={
    r"/executaAnalise": {"origins": "*"},
    r"/pesquisaTimes": {"origins": "*"},
    r"/salvarAnotacao": {"origins": "*"},
    r"/carregarNotas": {"origins": "*"},
    r"/excluirNota/*": {"origins": "*"},
    r"/atualizarNota/*": {"origins": "*"},
    r"/inserirDadosGoogle*": {"origins": "*"},
    r"/verificarToken*": {"origins": "*"},
    r"/pesquisarTimesFavoritos*": {"origins": "*"},
    r"/timesFavoritos*": {"origins": "*"}            
}, methods=["GET", "POST", "PUT", "DELETE"])

# Configurações de conexão com o banco de dados
config = {
    'user': 'admin',
    'password': 'futviewpass',
    'host': 'mysqlserver.czi6aewaekiq.us-east-2.rds.amazonaws.com',
    'database': 'DbFutView'
}

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or not token.startswith('Bearer '):
            return jsonify({'message': 'Token is missing!'}), 403
        token = token.split(' ')[1]
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            current_user = data['sub']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token expired!'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid!'}), 403
        return f(current_user, *args, **kwargs)
    return decorated

# Função para executar a análise

@app.route('/executaAnalise')
def executaAnalise():
    try:
        time = request.args.get('time')
        quantidadeJogos = request.args.get('quantidadeJogos')

        # Conexão com o banco de dados
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        # Execute sua análise
        mediaGols, mediaEscanteios, mediaCartoes, mediaPosseDeBola, mediaChutesNoGol, mediaChutesParaFora, mediaImpedimentos, mediaChutesLivres, mediaAtaques, mediaLaterais, mediaTirosDeMeta, mediaCartoesVermelhos = analise.analisaDados(
            time, quantidadeJogos)

        cursor.close()
        conn.close()

        return jsonify({
            'Media Gols': mediaGols,
            'Media Escanteios': mediaEscanteios,
            'Media cartões': mediaCartoes,
            'Media posse de bola': mediaPosseDeBola,
            'Media chutes no gol': mediaChutesNoGol,
            'Media chutes para fora': mediaChutesParaFora,
            'Media impedimentos': mediaImpedimentos,
            'Media chutes livres': mediaChutesLivres,
            'Media ataques': mediaAtaques,
            'Media laterais': mediaLaterais,
            'Media tiros de meta': mediaTirosDeMeta,
            'Media cartões vermelhos': mediaCartoesVermelhos
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Função para pesquisar times


@app.route('/pesquisaTimes')
def pesquisaTimes():
    try:
        time = request.args.get('time')
        pais = request.args.get('pais')

        # Conexão com o banco de dados
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        if time is None and pais is not None:
            # Execute sua pesquisa aqui, substituindo a chamada para pesquisa.pesquisaTimes()
            times = pesquisa.pesquisaTimes(pais)
            # Feche o cursor e a conexão
            cursor.close()
            conn.close()
            return jsonify({'Dados': times}), 200

        if time is not None and pais is None:
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
@token_required
def salvarAnotacao(current_user):
    try:
        # Obtenha os dados enviados pelo cliente
        anotacao = request.json['anotacao']

        # Conexão com o banco de dados
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        # Execute a inserção de dados no banco de dados, incluindo o fkSub
        sql = "INSERT INTO tbnotas (texto, fkSub) VALUES (%s, %s)"
        cursor.execute(sql, (anotacao, current_user))
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
@token_required
def atualizarNota(current_user, id_nota):
    try:
        # Obtenha os dados enviados pelo cliente
        dados = request.get_json()
        texto_nota = dados['anotacao']

        # Conexão com o banco de dados usando context manager (with)
        with mysql.connector.connect(**config) as conn, conn.cursor() as cursor:
            # Execute a atualização de dados no banco de dados
            cursor.execute("UPDATE tbnotas SET texto = %s WHERE pkNotas = %s and fkSub = %s", (texto_nota, id_nota, current_user))
            conn.commit()

        return jsonify({'message': 'Nota atualizada com sucesso!'}), 200

    except mysql.connector.Error as e:
        return jsonify({'error': str(e)}), 500
    except KeyError as e:
        return jsonify({'error': f'Chave ausente no JSON: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/carregarNotas', methods=['GET'])
@token_required
def carregarNotas(current_user):
    try:
        # Conexão com o banco de dados
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        # Execute uma consulta para obter todas as notas do usuário logado
        sql = "SELECT pkNotas, texto FROM tbnotas WHERE fkSub = %s"
        cursor.execute(sql, (current_user,))
        notas = cursor.fetchall()

        # Feche o cursor e a conexão
        cursor.close()
        conn.close()

        # Converter as notas para um formato adequado (por exemplo, lista de dicionários)
        notas_formatadas = [
            {'id': nota[0], 'texto': nota[1]} for nota in notas]

        # Retorna as notas em formato JSON
        return jsonify({'notas': notas_formatadas}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/excluirNota/<int:id_nota>', methods=['DELETE'])
@token_required
def excluirNota(current_user, id_nota):
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
    
@app.route('/inserirDadosGoogle', methods=['POST'])
def inserirDadosGoogle():
    try:
        dados = request.json  # Recebe os dados do frontend

        # Verifica se já existe um registro com o mesmo 'sub'
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        sql_verifica = "SELECT COUNT(*) FROM tbusuario WHERE subUsuario = %s"
        cursor.execute(sql_verifica, (dados['sub'],))
        result = cursor.fetchone()[0]

        if result > 0:
            # Gera um token JWT
            token = jwt.encode({
                'sub': dados['sub'],
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }, SECRET_KEY, algorithm='HS256')

            return jsonify({'message': 'Usuário já existe no banco de dados.', 'token': token}), 200

        # Insere os dados apenas se 'sub' não existir no banco de dados
        sql_inserir = "INSERT INTO tbusuario (emailUsuario, subUsuario, nomeUsuario) VALUES (%s, %s, %s)"
        cursor.execute(sql_inserir, (dados['email'], dados['sub'], dados['name']))
        conn.commit()

        # Obtém o ID do usuário recém-inserido
        id_usuario = cursor.lastrowid

        # Fecha o cursor e a conexão
        cursor.close()
        conn.close()

        # Gera um token JWT
        token = jwt.encode({
            'sub': dados['sub'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, SECRET_KEY, algorithm='HS256')

        return jsonify({'message': 'Dados inseridos com sucesso!', 'id': id_usuario, 'token': token}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/verificarToken', methods=['POST'])
def verificarToken():
    token = request.json.get('token')
    if not token:
        return jsonify({'valid': False}), 400

    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return jsonify({'valid': True}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({'valid': False, 'error': 'Token expired'}), 400
    except jwt.InvalidTokenError:
        return jsonify({'valid': False, 'error': 'Invalid token'}), 400
    
@app.route('/pesquisarTimesFavoritos', methods=['GET'])
@token_required
def pesquisarTimesFavoritos(current_user):
    try:
        # Conexão com o banco de dados
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        # Execute a consulta para obter os nomes dos times favoritos do usuário logado
        sql = """
        SELECT t.nomeTimes 
        FROM tbtimefavorito tf
        INNER JOIN tbtimes t ON t.pkTimes = tf.fkTime
        WHERE tf.fkSub = %s
        """
        cursor.execute(sql, (current_user,))
        times_favoritos = cursor.fetchall()

        # Feche o cursor e a conexão
        cursor.close()
        conn.close()

        # Converter os resultados para uma lista simples de nomes de times
        times_formatados = [time[0] for time in times_favoritos]

        # Retorna os times em formato JSON
        return jsonify({'Dados': times_formatados}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/timesFavoritos', methods=['POST'])
@token_required
def timesFavoritos(current_user):
    try:
        data = request.json
        time = data.get('time')
        id = data.get('id')

        # Conexão com o banco de dados
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        lista = pesquisa.pegarCodigo(time)
        codigo = int(lista[0])

        # Verifique se é para adicionar ou remover o favorito
        if id == 0: 
            sql = "INSERT INTO tbtimefavorito (fkTime, fkSub) VALUES (%s, %s)"
            cursor.execute(sql, (codigo, current_user))
            message = 'Time favorito adicionado com sucesso!'
        elif id == 1:
            sql = "DELETE FROM tbtimefavorito WHERE fkTime = %s AND fkSub = %s"
            cursor.execute(sql, (codigo, current_user))
            message = 'Time favorito removido com sucesso!'
        else:
            raise ValueError("ID inválido. Deve ser 0 (adicionar) ou 1 (remover).")

        conn.commit()

        # Feche o cursor e a conexão
        cursor.close()
        conn.close()

        return jsonify({'message': message, 'time': time}), 200
    except Exception as e:
        print("Erro interno no servidor:", e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) #ssl_context=('cert.pem', 'key.pem'))
