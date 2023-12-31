from flask import Flask, request, jsonify

app = Flask(__name__)
names_database = {}  # Dictionary to store names

@app.route('/names', methods=['GET'])
def get_names():
    return jsonify({"names": list(names_database.keys())})

@app.route('/names', methods=['POST'])
def add_name():
    data = request.get_json()

    if 'name' not in data:
        return jsonify({"error": "Name is required"}), 400

    name = data['name']

    if name in names_database:
        return jsonify({"error": f"Name '{name}' already exists"}), 409

    names_database[name] = True
    return jsonify({"message": f"Name '{name}' added successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
