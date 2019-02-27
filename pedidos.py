

from datetime import datetime
from flask import jsonify, make_response, abort

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

PEDIDOS = {
    "1": {
        "pedido": "1",
        "name": "Fernando",
        "timestamp": get_timestamp(),
    },
    "2": {
        "pedido": "2",
        "name": "Ricardo",
        "timestamp": get_timestamp(),
    },
    "3": {
        "pedido": "3",
        "name": "Claudia",
        "timestamp": get_timestamp(),
    },
}

def read_all():
    dict_pedidos = [PEDIDOS[key] for key in sorted(PEDIDOS.keys())]
    alunos = jsonify(dict_pedidos)
    qtd = len(dict_pedidos)
    content_range = "pedidos 0-"+str(qtd)+"/"+str(qtd)
    # Configura headers
    pedidoss.headers['Access-Control-Allow-Origin'] = '*'
    pedidoss.headers['Access-Control-Expose-Headers'] = 'Content-Range'
    pedidods.headers['Content-Range'] = content_range
    return pedidos

 
def read_one(name):
    if name in PEDIDOS:
        person = PEDIDOS.get(name)
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )
    return person
 
 
def create(pedido):
    name = pedido.get("name", None)
    pedido = pedido.get("pedido", None)
 
    if name not in PEDIDOS and name is not None:
        PEDIDOS[name] = {
            "name": name,
            "pedido": pedido,
            "timestamp": get_timestamp(),
        }
        return make_response(
            "{lname} successfully created".format(lname=lname), 201
        )
    else:
        abort(
            406,
            "Person with last name {lname} already exists".format(lname=lname),
        )
 
 
def update(name, pedido):
    if name in PEDIDOS:
        PEDIDOS[lname]["name"] = pedidos.get("name")
        PEDIDOS[pedido]["timestamp"] = get_timestamp()
 
        return PEOPLE[lname]
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )
 
def delete(name):
    if name in PEDIDOS:
        del PEDIDOS[name]
        return make_response(
            "{lname} successfully deleted".format(pedido=pedido), 200
        )
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )
 



