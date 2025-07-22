from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Sample in-memory data for flights and orders
flights = [
    {
        "id": 1,
        "flight_no": "AT100",
        "origin": "PEK",
        "destination": "SHA",
        "date": "2024-12-01",
        "price": 800
    },
    {
        "id": 2,
        "flight_no": "AT200",
        "origin": "PEK",
        "destination": "CAN",
        "date": "2024-12-01",
        "price": 950
    }
]

orders = []

@app.route('/api/flights', methods=['GET'])
def search_flights():
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    date = request.args.get('date')
    results = [f for f in flights if (
        (not origin or f['origin'] == origin) and
        (not destination or f['destination'] == destination) and
        (not date or f['date'] == date)
    )]
    return jsonify(results)

@app.route('/api/orders', methods=['POST'])
def create_order():
    data = request.get_json(force=True)
    flight_id = data.get('flight_id')
    user = data.get('user')
    flight = next((f for f in flights if f['id'] == flight_id), None)
    if not flight:
        return jsonify({'error': 'flight not found'}), 404
    order_id = len(orders) + 1
    order = {
        'id': order_id,
        'flight': flight,
        'user': user,
        'created': datetime.utcnow().isoformat(),
        'paid': False
    }
    orders.append(order)
    return jsonify(order), 201

@app.route('/api/pay', methods=['POST'])
def pay_order():
    data = request.get_json(force=True)
    order_id = data.get('order_id')
    order = next((o for o in orders if o['id'] == order_id), None)
    if not order:
        return jsonify({'error': 'order not found'}), 404
    order['paid'] = True
    return jsonify({'status': 'success', 'order': order})

if __name__ == '__main__':
    app.run(debug=True)
