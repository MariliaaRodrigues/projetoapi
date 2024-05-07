from flask import Blueprint

bp = Blueprint("api", __name__)

#Daqui para baixo as rotas

@bp.route('/')
def index():
    return jsonify({"status": 200, "message": "API da Marilia da Silva Rodrigues"})
@bp.route("/aleatorios")
def aleatorios():
    import random
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a})

@bp.route("/argumentos/<string:nome>")
def argumentos(nome: str):
    return jsonify({"status": 200, "data": nome})
# Dados das pessoas