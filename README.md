Flask Kafka Zookeeper Docker application for pizza ordering, incorporating library context and API details:

# Pizza Ordering Docker Application with Flask, Kafka, and Zookeeper

This application simulates a pizza ordering system using Flask, Kafka, and Zookeeper. Here's an overview of the technologies used:

* **Flask:** A lightweight web framework for building Python web applications. ([https://flask.palletsprojects.com/](https://flask.palletsprojects.com/))
* **Kafka:** A distributed streaming platform for handling real-time data feeds. ([https://kafka.apache.org/](https://kafka.apache.org/))
* **Zookeeper:** A distributed coordination service for distributed applications. ([https://zookeeper.apache.org/](https://zookeeper.apache.org/))

**Docker Integration**

The application utilizes Docker containers to package and deploy the services:

* **zookeeper:** Runs a Zookeeper instance for service discovery and coordination.
* **kafka:** Builds a Kafka container using a Dockerfile (Dockerfile_kafka) to handle message processing.
* **flask-app:** Builds a Flask application container using a Dockerfile (Dockerfile_flask) to expose the pizza ordering API.

**API Endpoints**

The Flask application provides the following API endpoints:

1. **/order/<count> (POST):** Places an order for a specified number of pizzas.
    - **Request:**
        - JSON body with a `count` field indicating the number of pizzas.
    - **Response:**
        - JSON object containing the generated `order_id`.
2. **/order/<order_id> (GET):** Retrieves details of a specific order using its ID.
    - **Request:**
        - The `order_id` in the URL path.
    - **Response:**
        - JSON object containing the order details (implementation details in `pizza_service.py`).
3. **/add_order (POST):** Adds a new order to the database (simulated behavior).
    - **Request:**
        - Optional JSON body with a `count` field indicating the number of pizzas. Defaults to `None`.
    - **Response:**
        - JSON message indicating successful order addition or error details.
4. **/ (GET):** Checks the health of the Flask application.
    - **Response:**
        - JSON object with a status code (`200`) and a success message.

**Library Context**

* **flask:** Used for creating the web application and handling API requests.
* **json:** Used for encoding and decoding JSON data between the application and the client.
* **threading:** Used for launching a consumer thread to process pizza orders asynchronously.

**Running the Application**

1. Build the Docker images:
   ```bash
   docker-compose build
   ```
2. Run the application with Docker Compose:
   ```bash
   docker-compose up
   ```

This will start all the necessary services (Zookeeper, Kafka, and the Flask application) in detached mode.

**Further Considerations**

* The `pizza_service.py` file is not included in this example. It likely contains functions for processing pizza orders, such as `order_pizzas` and `get_order`, and might interact with a database or other backend system.
* The provided configuration simulates placing an order repeatedly within 30 seconds using a loop in the `add_order` endpoint. This might not be the desired behavior for a real-world application.

**Getting Started with Development**

1. Clone this repository to your local machine.
2. Modify the code in the relevant Python files (e.g., `app.py`, `pizza_service.py`) to fit your specific requirements.
3. Rebuild the Docker images using `docker-compose build`.
4. Restart the application containers using `docker-compose up -d`.

This README provides a comprehensive overview of the application's functionality, dependencies, and API details. Feel free to customize it further as needed.