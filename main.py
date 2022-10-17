# importando as bibliotecas
from pymongo import MongoClient
import pandas as pd

# Conectando com o Mongo DB
mongo_client = MongoClient("mongodb://admin:password@localhost:27017")
mydb = mongo_client["escola"]
mycol = mydb["alunos"]

mydict = { "nome": "Ricardinho", "ano": "sexto" }
x = mycol.insert_one(mydict)

cursor = mycol.find({})
for document in cursor:
    print(document)

