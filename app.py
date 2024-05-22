from flask import Flask, request, jsonify
from threading import Thread
import json
import pizza_service
import time

app = Flask(__name__)


@app.route('/order/<count>', methods=['POST'])
def order_pizzas(count):
    """
    Endpoint for placing an order for pizzas.
    """
    order_id = pizza_service.order_pizzas(int(count))
    return json.dumps({"order_id": order_id})


@app.route('/order/<order_id>', methods=['GET'])
def get_order(order_id):
    """
    Endpoint for retrieving a specific order by its ID.
    """
    return pizza_service.get_order(order_id)


@app.route('/add_order', methods=['POST'])
def add_order():  # Define count parameter with default None
    """
    Endpoint for adding a new order to the database.

    Args:
        count (int, optional): The number of pizzas to order. Defaults to None.

    Returns:
        str: Response from the pizza_service.order_pizzas() function.
    """
    start_time = time.monotonic()

    try:
        data = request.json
        count = data.get('count')  # Get count from the request data
        while((time.monotonic() - start_time) < 30):
            pizza_service.order_pizzas(count)  # Pass count to the function
            break
        return jsonify({"message": "Order added successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})


@app.route('/', methods=['GET'])
def home():
    """
    Endpoint for checking the health of the Flask application.
    """
    print("Healthy Flask App *******************************************")
    return json.dumps({"Status": 200, "Message": "Healthy Flask App"})


if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', debug=True)


# Launch the consumer thread
@app.before_first_request
def launch_consumer():
    """
    Launches the consumer thread to process pizza orders.
    """
    print("Consumer is starting **************************************")
    t = Thread(target=pizza_service.load_orders)
    t.start()
