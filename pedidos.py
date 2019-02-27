

from datetime import datetime
from flask import jsonify, make_response, abort

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

PEDIDOS = {
    "1": {
        "pedido": "1",
        "name": "Fernando",
        "timestamp": get_timestamp(),
        "produto": "Produto",
        "quantidade": "1",
    },
    "2": {
        "pedido": "2",
        "name": "Ricardo",
        "timestamp": get_timestamp(),
        "produto": "Produto",
        "quantidade": "1",
    },
    "3": {
        "pedido": "3",
        "name": "Claudia",
        "timestamp": get_timestamp(),
        "produto": "Produto",
        "quantidade": "1",
    },
}

def read_all():
    dict_pedidos = [PEDIDOS[key] for key in sorted(PEDIDOS.keys())]
    pedidos = jsonify(dict_pedidos)
    qtd = len(dict_pedidos)
    content_range = "pedidos 0-"+str(qtd)+"/"+str(qtd)
    # Configura headers
    pedidos.headers['Access-Control-Allow-Origin'] = '*'
    pedidos.headers['Access-Control-Expose-Headers'] = 'Content-Range'
    pedidos.headers['Content-Range'] = content_range
    return pedidos

 
def read_one(name):
    if name in PEDIDOS:
        person = PEDIDOS.get(name)
    else:
        abort(
            404, "Pedido numero {name} nao encontrado".format(name=name)
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
            "{name} Criado com Sucesso".format(name=name), 201
        )
    else:
        abort(
            406,
            "Person with last name {lname} already exists".format(name=name),
        )
 
 
def update(name, cliente):
    if name in PEDIDOS:
        PEDIDOS[name]["name"] = cliente.get("name")
        #PEDIDOS[quantidade]["quantidade"] = person.get("quantidade")
        #PEDIDOS[pedido]["timestamp"] = get_timestamp()
 
        return PEDIDOS[name]
    else:
        abort(
            404, "Pedido nao encontrado {name} ".format(name=name)
        )

 
def delete(name):
    if name in PEDIDOS:
        del PEDIDOS[name]
        return make_response(
            "{name} successfully deleted".format(pedido=pedido), 200
        )
    else:
        abort(
            404, "Person with last name {lname} not found".format(lname=lname)
        )
 



