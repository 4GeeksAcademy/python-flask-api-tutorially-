from flask import Flask, jsonify, request
app = Flask(__name__)



todos = [
    { "label": "Sample Todo 1", "done": True }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True) or {}
    print("Incoming request with the following body", request_body)

    if "label" in request_body and "done" in request_body:
        todos.append(request_body)
        return jsonify(todos), 200
    else:
        return jsonify({"error": "Missing keys"}), 200


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    deleted = todos.pop(position)
    print("deleted todo", deleted)
    return jsonify(todos), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)