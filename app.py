from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# In-memory data store as a dictionary
items = {}

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({'items': list(items.values())})

@app.route('/items', methods=['POST'])
def add_item():
    item_data = request.json

    item_id = str(uuid.uuid4())  # Generate a unique ID
    item = {**item_data, 'id': item_id}

    items[item_id] = item
    return jsonify(item), 201

@app.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    item = items.get(item_id)
    if item:
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404

@app.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    if item_id in items:
        item_data = request.json
        item = {**item_data, 'id': item_id}

        items[item_id] = item
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404

@app.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = items.pop(item_id, None)
    if item:
        return jsonify({item_id: item})
    else:
        return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
