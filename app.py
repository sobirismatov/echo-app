from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST', 'GET'])
def api():

    data = request.get_json(force=True)

    a = data.get('a', 0)
    b = data.get('b', 0)
    
    return jsonify({
        'sum': a+b
    })


@app.route('/api/<username>')
def login(username: str):
    print(username)
    return f'hi, {username}'


if __name__ == '__main__':
    app.run(debug=True)