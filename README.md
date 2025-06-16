# 🍕 Pizza Restaurant API

A RESTful API for managing pizza restaurants, their menus, and pizza offerings built with Flask and SQLAlchemy.

## 📦 Setup Instructions
### 1. Clone the repository
git clone <repo-url>
cd pizza-api-challenge

### 2. Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Configure environment variables
Create a .env file in the project root with the following (edit as needed):

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///pizza_restaurant.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

### 5. Set up the database
#### Create the database in PostgreSQL:
sql -U sqlite3 -h localhost
CREATE DATABASE pizza_db;

#### Run migrations:
export FLASK_APP=server/app.py
flask db init                   # Only if not already initialized
flask db migrate -m "Initial migration"
flask db upgrade

### 6. Seed the database (optional)
python -m server.seed

### 7. Run the application
python server/app.py
The API will be available at http://localhost:5555/.

### Prerequisites
- Python 3
- pipenv (install with `pip install pipenv`)

### Dependencies
Install all the dependencies:

pipenv install
pipenv shell

### Database Setup
Initialize the database:
export FLASK_APP=server/app.py
flask db init

### Run migrations
flask db migrate -m "Initial migration"
flask db upgrade

### Seed the database with sample data
python server/seed.py

### Running the Server
python server/app.py

The API will be available at http://localhost:5555

### 🌐 API Endpoints
Endpoint: GET /restaurants
Response:

json
[
  {
    "id": 1,
    "name": "Pizza Palace",
    "address": "123 Main St"
  },
  {
    "id": 2,
    "name": "Mario's Pizza",
    "address": "456 Oak Ave"
  }
]

Endpoint: GET /restaurants/<int:id>

Success Response:

json
{
  "id": 1,
  "name": "Pizza Palace",
  "address": "123 Main St",
  "pizzas": [
    {
      "id": 1,
      "name": "Margherita",
      "ingredients": "Tomato sauce, mozzarella, basil",
      "price": 10
    }
  ]
}

Error Response (404):

json
{
  "error": "Restaurant not found"
}

🏗 Project Structure
.
├── server/
│   ├── __init__.py
│   ├── app.py                # App setup
│   ├── config.py             # DB configuration
│   ├── models/               # Database models
│   │   ├── __init__.py
│   │   ├── restaurant.py
│   │   ├── pizza.py
│   │   └── restaurant_pizza.py
│   ├── controllers/           # Route handlers
│   │   ├── __init__.py
│   │   ├── restaurant_controller.py
│   │   ├── pizza_controller.py
│   │   └── restaurant_pizza_controller.py
│   ├── seed.py               # Database seeder
├── migrations/               # Database migration files
└── README.md