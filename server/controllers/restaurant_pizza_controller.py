from flask import Blueprint, jsonify, request
from server.models.restaurant_pizza import RestaurantPizza
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server import db

restaurant_pizzas_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizzas_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    
    # Validate required fields
    required_fields = ['price', 'pizza_id', 'restaurant_id']
    if not all(field in data for field in required_fields):
        return jsonify({"errors": ["Missing required fields"]}), 400
    
    # Validate price range
    price = data['price']
    if not isinstance(price, int) or price < 1 or price > 30:
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400
    
    # Check if restaurant exists
    restaurant = Restaurant.query.get(data['restaurant_id'])
    if not restaurant:
        return jsonify({"errors": ["Restaurant not found"]}), 404
    
    # Check if pizza exists
    pizza = Pizza.query.get(data['pizza_id'])
    if not pizza:
        return jsonify({"errors": ["Pizza not found"]}), 404
    
    # Create new RestaurantPizza
    try:
        restaurant_pizza = RestaurantPizza(
            price=price,
            pizza_id=pizza.id,
            restaurant_id=restaurant.id
        )
        db.session.add(restaurant_pizza)
        db.session.commit()
        return jsonify(restaurant_pizza.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400