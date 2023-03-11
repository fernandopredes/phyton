from flask import Flask, request, send_from_directory, render_template, jsonify, make_response
from sqlalchemy.exc import IntegrityError

from model import Session, Produto
from model.comentario import Comentario


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html'), 200

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/x-icon')

@app.route('/add_produto', methods=['POST'])
def add_produto():
    session = Session()
    produto = Produto(
        nome = request.form.get("nome"),
        quantidade = request.form.get('quantidade'),
        valor = request.form.get('valor')
    )
    try:
        #para adicionar o produto
        session.add(produto)
        #efetivar o comando de adição na tabela
        session.commit()

        response = {
            'message': 'Produto adicionado com sucesso',
            'produto': {
                'id': produto.id,
                'nome': produto.nome,
                'quantidade': produto.quantidade,
                'valor': produto.valor
            }
        }
        return make_response(jsonify(response), 200)
    except IntegrityError as e:
        error_msg = 'Produto de mesmo nome já salvo na base.'
        response = {
            'message': error_msg
        }
        return make_response(jsonify(response), 409)
    except Exception as e:
        error_msg = 'Não foi possível adicionar o item.'
        print(str(e))
        response = {
            'message': error_msg
        }
        return make_response(jsonify(response), 400)

@app.route('/get_produto/<produto_id>', methods=['GET'])
def get_produto(produto_id):
    session = Session()
    produto = session.query(Produto).filter(Produto.id == produto_id).first()
    if not produto:
        error_msg = 'Produto não encontrado'
        response =  make_response(jsonify({'error': error_msg}, 404))
    else:
        response_data = {
            'id': produto.id,
            'nome':produto.nome,
            'valor':produto.valor,
            'quantidade':produto.quantidade
            }
        response = make_response(jsonify(response_data), 200)
    session.close()
    response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/delete_produto/<produto_id>', methods=['DELETE'])
def delete_produto(produto_id):
    session = Session()
    count = session.query(Produto).filter(Produto.id == produto_id).delete()
    session.commit()
    print(count)
    if count == 1:
        msg = 'Produto deletado'
        response =  make_response(jsonify({'msg': msg}, 200))
        return response
    else:
        error_msg = 'Produto não existe'
        response =  make_response(jsonify({'error': error_msg}, 404))
        return response

@app.route('/add_comentario/<produto_id>', methods = ['POST'])
def add_comentario(produto_id):
    session = Session()
    produto = session.query(Produto).filter(Produto.id == produto_id).first()
    if not produto:
         error_msg = "Produto não encontrado na base :/"
         response =  make_response(jsonify({'error': error_msg}, 404))
         return response

    autor = request.form.get('autor')
    texto = request.form.get('texto')
    n_estrelas = request.form.get('estrelas')
    if n_estrelas:
        n_estrelas = int(n_estrelas)

    comentario = Comentario(texto, n_estrelas, autor)
    produto.adiciona_comentario(comentario)
    session.commit()
    response = {
            'message': 'Comentário adicionado com sucesso',
            'comentário': {
                'id': comentario.id,
                'data_insercao': comentario.data_insercao,
                'estrelas': comentario.n_estrelas,
                'texto': comentario.texto,
                'autor': comentario.autor
            }
        }
    return make_response(jsonify(response), 200)
