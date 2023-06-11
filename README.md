######Flights Repository
This repository contains a flight management system project developed as part of a study program. The system allows users to search for flights, book flights, and perform other related operations.

Table of Contents
Installation
Usage
Endpoints
Authentication
Models
Contributing
License
Installation
To install and run the project locally, please follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/YaelBenYair/Flights.git
Install the project dependencies. It is recommended to use a virtual environment for this:

bash
Copy code
cd Flights
pip install -r requirements.txt
Set up the database by running migrations:

bash
Copy code
python manage.py migrate
Start the development server:

bash
Copy code
python manage.py runserver
The project should now be up and running locally on http://localhost:8000/.

Usage
You can interact with the flight management system using the provided API endpoints. The project provides various functionalities such as flight search, flight booking, user management, etc. Please refer to the Endpoints section for more details on available API endpoints.

Endpoints
The following endpoints are available in the API:

Authentication Endpoints:

POST /api/v1/auth/signup/ - Create a new user account.
POST /api/v1/auth/token/ - Obtain an access and refresh token.
POST /api/v1/auth/token/refresh/ - Refresh an access token.
GET /api/v1/auth/me/ - Get the details of the currently authenticated user.
Flight Endpoints:

GET /api/v1/flight/ - Retrieve a list of flights with optional filtering parameters.
POST /api/v1/flight/ - Create a new flight (requires staff authentication).
GET /api/v1/flight/{flight_id}/ - Retrieve details of a specific flight.
PUT /api/v1/flight/{flight_id}/ - Update details of a specific flight (requires staff authentication).
PATCH /api/v1/flight/{flight_id}/ - Partially update details of a specific flight (requires staff authentication).
Order Endpoints:

GET /api/v1/order/ - Retrieve a list of orders (requires staff authentication) or user-specific orders.
POST /api/v1/order/ - Create a new order.
GET /api/v1/order/{order_id}/ - Retrieve details of a specific order (requires staff authentication or owner access).
PUT /api/v1/order/{order_id}/ - Update details of a specific order (requires owner access).
PATCH /api/v1/order/{order_id}/ - Partially update details of a specific order (requires owner access).
Please note that some endpoints require authentication and certain operations are restricted to staff members.

Authentication
The project uses token-based authentication. To access authenticated endpoints, you need to include the access token in the request header. The access token can be obtained by making a POST request to the /api/v1/auth/token/ endpoint with valid user credentials. The response will include an access token and a refresh token.

To refresh an access token, make a POST request to the /api/v1/auth/token/refresh/ endpoint with a valid refresh token.

Please ensure that you include the Authorization header in the format: Bearer <access_token>. For example:

makefile
Copy code
Authorization: Bearer <access_token>
Models
The project includes the following models:

User - Represents a user account.
Flight - Represents a flight with various attributes such as flight number, origin, destination, price, etc.
Order - Represents a flight booking made by a user.
Please refer to the source code for more details on the attributes and relationships of each model.

Contributing
Contributions to this project are welcome. If you would like to contribute, please follow these steps:

Fork the repository.
Create a new branch for your contribution.
Make your changes and commit them.
Push your changes to your fork.
Submit a pull request.
Please ensure that your code adheres to the existing coding style and includes appropriate tests.

License
The project is released under the MIT License. Feel free to use, modify, and distribute the code as permitted by the license.
