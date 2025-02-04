from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for Brazilian party snacks
snacks = [
    {"id": 1, "name": "Coxinha", "description": "Chicken-filled dough shaped like a teardrop."},
    {"id": 2, "name": "Pão de Queijo", "description": "Cheese bread made with tapioca flour."},
    {"id": 3, "name": "Brigadeiro", "description": "Chocolate truffle made with condensed milk."},
]

@app.route('/snacks', methods=['GET'])
def get_snacks():
    return jsonify(snacks)

@app.route('/snacks/<int:sack_id>', methods=['GET'])
def get_snack(sack_id):
    snack = next((snack for snack in snacks if snack['id'] == sack_id), None)
    if snack is not None:
        return jsonify(snack)
    return jsonify({"error": "Snack not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)