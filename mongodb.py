import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# print(myclient.list_database_names())

mydb = myclient["sample_db"]
mycol = mydb["products"]

# print(mydb.list_collection_names())
for x in mycol.find({}, {"_id": 0, "__v":0}):
    print(x)