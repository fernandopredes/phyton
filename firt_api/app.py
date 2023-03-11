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
    if count == 1:
        return render_template('deletado.html', produto_id = produto_id), 200
    else:
        error_msg = 'Produto não existe'
        return render_template('error.html', error_code = 404, error_msg = error_msg), 404

@app.route('/add_comentario/<produto_id>', methods = ['POST'])
def add_comentario(produto_id):
    session = Session()
    produto = session.query(Produto).filter(Produto.id == produto_id).first()
    if not produto:
         error_msg = "Produto não encontrado na base :/"
         return render_template("error.html", error_code= 404, error_msg=error_msg), 404

    autor = request.form.get('autor')
    texto = request.form.get('texto')
    n_estrelas = request.form.get('estrelas')
    if n_estrelas:
        n_estrelas = int(n_estrelas)

    comentario = Comentario(autor, texto, n_estrelas)
    produto.adiciona_comentario(comentario)
    session.commit()
    return render_template('produto.html', produto = produto), 200
