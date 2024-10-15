import certifi
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Modify the credentials to make connection to the MongoDB
uri = "mongodb+srv://nithinvasireddy:<DB_password>@cluster0.iqkc1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile=certifi.where())

products_collection = client["restaurant_pos"]["products"]

product_data = [{"_id": "650de6f935c7024b8a6a957a","product_id": "MENU1001","name": "Margherita Pizza","description": "Classic pizza with tomato sauce, mozzarella, and basil","category": "Main Course","price": 12.99,"stock_quantity": 50,"supplier": "Fresh Farms Ltd.","created_at": "2024-09-15T10:00:00Z","updated_at": "2024-09-20T10:00:00Z"},{"_id": "650de6f935c7024b8a6a957b","product_id": "MENU1002","name": "Caesar Salad","description": "Romaine lettuce, croutons, Parmesan cheese, and Caesar dressing","category": "Salads","price": 8.50,"stock_quantity": 100,"supplier": "Greens Organic","created_at": "2024-08-10T12:00:00Z","updated_at": "2024-09-21T14:00:00Z"},{"_id": "650de6f935c7024b8a6a957c","product_id": "MENU1003","name": "Spaghetti Carbonara","description": "Pasta with eggs, cheese, pancetta, and pepper","category": "Main Course","price": 14.99,"stock_quantity": 80,"supplier": "Pasta World","created_at": "2024-07-25T09:00:00Z","updated_at": "2024-09-12T10:30:00Z"},{"_id": "650de6f935c7024b8a6a957d","product_id": "MENU1004","name": "Chocolate Lava Cake","description": "Warm chocolate cake with a molten center","category": "Desserts","price": 6.50,"stock_quantity": 40,"supplier": "Sweet Treats Co.","created_at": "2024-08-30T11:00:00Z","updated_at": "2024-09-21T10:00:00Z"},{"_id": "650de6f935c7024b8a6a957e","product_id": "MENU1005","name": "Espresso","description": "Rich espresso shot with a bold flavor","category": "Beverages","price": 3.00,"stock_quantity": 200,"supplier": "Coffee Bean Co.","created_at": "2024-09-01T08:00:00Z","updated_at": "2024-09-21T11:00:00Z"}]

result = products_collection.insert_many(product_data)

print(result.inserted_ids)
