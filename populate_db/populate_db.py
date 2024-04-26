
from pymongo import MongoClient
from Jeux import Jeux

client = MongoClient("mongodb://jeu-mongodb-1:27017/")
db = client["db_jeux"]
collection = db["col_jeux"]

def populate_db():
    jeu1 = Jeux(console_jeu="PS2", genre="RPG", prix=23, description="Un jeu de RPG", code_rayon="ABC.12.35.2021", id_jeu = "123")
    jeu2 = Jeux(console_jeu="XBOX", genre="Sport", prix=30, description="Un jeu de Sport", code_rayon="ABC.12.36.2019", id_jeu = "456")
    jeu3 = Jeux(console_jeu="PS5", genre="Simulation", prix=23, description="Un jeu de Simulation", code_rayon="ABC.12.35.2021",id_jeu="789") 


    collection.insert_one(jeu1.dict())
    collection.insert_one(jeu2.dict())
    collection.insert_one(jeu3.dict())

if __name__ == '__main__':
    populate_db()