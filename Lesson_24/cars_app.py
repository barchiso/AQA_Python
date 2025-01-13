from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app = Flask(__name__)

# Конфігурація для JWT
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Змініть на свій секретний ключ
jwt = JWTManager(app)

# База даних автомобілів у вигляді словника Python
cars_db = {
    1: {"brand": "BMW", "year": 2018, "engine_volume": 2.0, "price": 50000},
    2: {"brand": "Audi", "year": 2020, "engine_volume": 1.8, "price": 45000},
    3: {"brand": "Mercedes", "year": 2019, "engine_volume": 2.5, "price": 55000},
    4: {"brand": "Toyota", "year": 2017, "engine_volume": 2.4, "price": 35000},
    5: {"brand": "Honda", "year": 2016, "engine_volume": 1.6, "price": 30000},
    6: {"brand": "Nissan", "year": 2021, "engine_volume": 1.5, "price": 40000},
    7: {"brand": "Ford", "year": 2015, "engine_volume": 2.2, "price": 32000},
    8: {"brand": "Chevrolet", "year": 2018, "engine_volume": 1.8, "price": 28000},
    9: {"brand": "Volkswagen", "year": 2019, "engine_volume": 2.0, "price": 33000},
    10: {"brand": "Hyundai", "year": 2020, "engine_volume": 1.6, "price": 29000},
    11: {"brand": "Kia", "year": 2019, "engine_volume": 2.0, "price": 31000},
    12: {"brand": "Subaru", "year": 2017, "engine_volume": 2.5, "price": 40000},
    13: {"brand": "Mazda", "year": 2018, "engine_volume": 2.0, "price": 32000},
    14: {"brand": "Lexus", "year": 2021, "engine_volume": 3.0, "price": 60000},
    15: {"brand": "Infiniti", "year": 2019, "engine_volume": 3.5, "price": 52000},
    16: {"brand": "Acura", "year": 2020, "engine_volume": 2.4, "price": 48000},
    17: {"brand": "Jeep", "year": 2018, "engine_volume": 3.6, "price": 45000},
    18: {"brand": "Land Rover", "year": 2020, "engine_volume": 2.0, "price": 55000},
    19: {"brand": "Volvo", "year": 2019, "engine_volume": 2.0, "price": 46000},
    20: {"brand": "Porsche", "year": 2021, "engine_volume": 3.0, "price": 70000},
    21: {"brand": "Tesla", "year": 2020, "engine_volume": 0.0, "price": 80000},
    22: {"brand": "Ferrari", "year": 2021, "engine_volume": 6.3, "price": 250000},
    23: {"brand": "Lamborghini", "year": 2020, "engine_volume": 6.5, "price": 300000},
    24: {"brand": "Bugatti", "year": 2019, "engine_volume": 8.0, "price": 350000},
    25: {"brand": "McLaren", "year": 2021, "engine_volume": 4.0, "price": 280000},
}

# Проста аутентифікація
users = {
    "test_user": "test_pass"
}

# Функція для автентифікації користувача
def authenticate(username, password):
    if username in users and users[username] ==  password:
        return username

# Функція для ідентифікації користувача за ідентифікатором
def identity(payload):
    username = payload['identity']
    return {"username": username}

# Ендпоінт для отримання токена доступу
@app.route('/auth', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({"message": "Аутентифікація не пройшла!"}), 401

    username = authenticate(auth.username, auth.password)
    if not username:
        return jsonify({"message": "Неправильне ім'я користувача або пароль!"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

# Ендпоінт для пошуку автомобілів
@app.route('/cars', methods=['GET'])
@jwt_required()
def get_cars():
    sort_by = request.args.get('sort_by')
    limit = request.args.get('limit')
    
    sorted_cars = sorted(cars_db.values(), key=lambda x: x.get(sort_by, 0) if sort_by else x['brand'])
    limited_cars = sorted_cars[:int(limit)] if limit else sorted_cars
    
    return jsonify(limited_cars), 200

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080
    app.run(host=host, port=port, debug=True)