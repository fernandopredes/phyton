from flask import jsonify, make_response

def resposta_sucesso(data, code):
    response = make_response(jsonify(data), code)
    response.headers["Content-Type"] = "application/json"
    return response
