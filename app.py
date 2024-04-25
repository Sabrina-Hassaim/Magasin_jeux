from pymongo import MongoClient
from fastapi import FastAPI
from Jeux import Jeux
from typing import List


app = FastAPI()

client = MongoClient("mongodb://jeu-mongodb-1:27017/")
db = client["db_jeux"]
collection = db["col_jeux"]

@app.get("/jeux", response_model=List[Jeux])
def read_root():
    jeux = list(collection.find()) 
    return jeux

@app.post("/add_jeux", response_model=Jeux)
def add_jeux(jeu: Jeux):
    collection.insert_one(jeu.dict())
    return jeu


@app.get("/jeu_by_id/{id_jeu}", response_model=Jeux)
def jeu_by_id(id_jeu : str):
    jeu = collection.find_one({"id_jeu": id_jeu})
    return jeu

@app.get("/jeu_by_prix/{prixmin}/{prixmax}", response_model=List[Jeux])
def jeu_by_prix(prixmax : int, prixmin : int):
    jeu = list(collection.find({"prix": {"$gt": prixmin, "$lt": prixmax}}))
    return jeu


@app.put('/modifier_jeu/{id_jeu}', response_model=Jeux)
def modifier_jeu(id_jeu : str, jeu_modifie : Jeux):
    jeu = collection.update_one(
        {"id_jeu": id_jeu},  # Filtre : le document à mettre à jour
        {"$set": jeu_modifie.dict()}  # Nouvelle valeur pour le champ 'age'
    )
    return jeu

@app.delete("/delete_jeu/{id_jeu}", response_model=dict)
def delete_jeu(id_jeu : str):
    var = collection.delete_one({"id_jeu": id_jeu})
    if (var == None):
        raise Exception("Le jeu n'existe pas")
    return {"message": "Jeu deleted"}
    