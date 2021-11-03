from pymongo import MongoClient

# Basic Setup
client = MongoClient()
db = client["db_person"]
collection = db["person"]

def person(number_id, name, age, job, traits):
    return {
        "_id" : number_id,
        "name" : name,
        "age" : age,
        "job" : job,
        "traits" : traits
    }
    
collection.insert_one(person(0, "Alex", 35, "unemployed", ["loyal", "humble", "patient"]))
collection.insert_one(person(1, "Bruna", 23, "engineer", ["resilient", "persistent", "honest", "flexible"]))
collection.insert_many([
    person(2, "Carlos", 42, "plumber", ["creative", "disciplined", "conscientious"]),
    person(3, "Diane", 26, "teacher", ["compassionate", "creative", "loyal"])
])

results = collection.find({"traits" : "loyal"})

for find_person in results:
    print(find_person["name"]) # Alex \n Diane
    

results = collection.find_one({"_id" : 2})
print(results["name"])

collection.insert_one(person(None, None, None, None, None))
collection.delete_one({"_id": None})

collection.update_one({"_id" : 3}, {"$set" : {"name" : "Diana"}})

collection.update_one({"_id" : 2}, {"$inc": {"age" : 1}})

doc_count = collection.count_documents({})
doc_count