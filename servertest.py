from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    login = data.get('login')
    senha = data.get('senha')
    return jsonify({"login": login, "senha": senha})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)