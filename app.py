from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    a = data.get('a', 0)
    b = data.get('b', 0)
    result = a * b
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(port=5002, debug=True)
