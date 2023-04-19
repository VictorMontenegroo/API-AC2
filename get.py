from flask import Flask, jsonify

app = Flask(__name__)

semi_final = [
        {'id': 1, 'nome': 'Real Madrid', 'titulos':14},
        {'id': 2, 'nome': 'Milan', 'titulos':7},
        {'id': 3, 'nome': 'Inter de Milao', 'titulos':3},
        {'id': 4, 'nome': 'Manchester City', 'titulos':0},
    ]

@app.route('/semi', methods=['GET'])
def champions_league():  
    return jsonify(semi_final, 201)

if __name__ == '__main__':
    app.run(debug=True, port=501)