from pymongo import MongoClient

client = MongoClient()

db = client["restaurant"]

db.create_collection("food")
db.create_collection("employees")

food_collection = db.get_collection("food")
employees_collection = db.get_collection("employees")

def order(number_id, name, price, ingredients):
    return {
        "_id" : number_id,
        "name" : name,
        "price" : price,
        "ingredients" : ingredients
    }

def employee(number_id, name, salary, job):
    return {
        "_id" : number_id,
        "name" : name,
        "salary" : salary,
        "job" : job
    }
    
# All names, values, ingredients are fictional.

food_collection.insert_many([
    order(0, "Beef Taco", 80.45, ["pepper", "oil", "garlic", "onion", "salt", "rice", "egg", "cheese", "tortilla chips", "beef"]),
    order(1, "Steak", 94.50, ["onion", "egg", "ketchup", "beef", "black pepper", "butter", "mushroom"]),
    order(2, "Hamburguer", 71.30, ["oil", "onion", "pepper", "garlic", "oregano", "beef", "hamburger bun", "tomato paste", "buttler"])
])

employees_collection.insert_many([
    employee(0, "John", 1800, "fast food cook"),
    employee(1, "Rebeca", 3400, "kitchen manager"),
    employee(2, "Louis", 2700, "prep cook")
]) 

results = food_collection.find({
    "price" : {"$gt" : 72.00}
})

for r in results:
    print(f"{r['name']} : R${r['price']}")

results = food_collection.find({
    "ingredients" : {"$in" : ["pepper", "egg"]}
})

for r in results:
    print(f"{r['name']}")
    
results = employees_collection.find({
    "job" : {"$eq": "fast food cook"}
})

for r in results:
    print(f"{r['name']}")
    
results = employees_collection.find({
    "salary" : {"$lt" : 3000}
})

for r in results:
    print(f"Name: {r['name']}. Salary: R$ {r['salary']}.00")