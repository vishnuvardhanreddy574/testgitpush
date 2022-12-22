import pymongo
client = pymongo.MongoClient("mongodb+srv://ineuron:Vishnu123@vish.bihq0sh.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "sundhanshu",
    "email": "sudhanshu@ineuron.ai",
    "surname":"kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)