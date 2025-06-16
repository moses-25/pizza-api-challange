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

