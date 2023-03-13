from flask import jsonify, make_response

def resposta_erro(msg, code):
    response = make_response(jsonify({"message": msg}), code,)
    response.headers["Content-Type"] = "application/json"
    return response
