# Importando o Pymongo para o programa
from pymongo import MongoClient

#criando conexão com Mongo
client = MongoClient("mongodb://localhost:27017/veiculos")

# objeto que referencia ao BD
database = client["veiculos"]

# objetvo que referencia aa collection
collection = database['carros']

new_car = {"Marca": "Ford", "Modelo": "Bronco", "Ano": 2023, "Preco": 125000}

collection.insert_one(new_car)

collection.find()