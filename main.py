# importando as bibliotecas
from pymongo import MongoClient
import pandas as pd
import os

# Conectando com o Mongo DB

mongo_client = MongoClient(os.environ.get("DB_STRING"))
mydb = mongo_client["escola"]
mycol = mydb["alunos"]

mydict = { "nome": "Ricardinho", "ano": "sexto" }
x = mycol.insert_one(mydict)

cursor = mycol.find({})
for document in cursor:
    print(document)

