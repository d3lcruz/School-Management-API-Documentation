from pymongo import MongoClient

#db_client = MongoClient(
 #    "mongodb+srv://Delacruz:machera@practica.26jbxza.mongodb.net/?retryWrites=true&w=majority&appName=Practica").school2

uri = "mongodb+srv://Delacruz:machera@practica.26jbxza.mongodb.net/?retryWrites=true&w=majority&appName=Practica"
#.School_Managament
# Create a new client and connect to the server
client = MongoClient(uri)
#collection
db = client.School_Managament
collection = db["students"]
collection_course = db["courses"]
collection_enrollment = db["enrollment"]
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)