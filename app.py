# Importando o Pymongo para o programa
from pymongo import MongoClient
# Será necessário para excluir por ObjetcID --
from bson.objectid import ObjectId

#criando conexão com Mongo
client = MongoClient("mongodb://localhost:27017/veiculos")

# objeto que referencia ao BD
database = client["veiculos"]

# objetvo que referencia aa collection
collection = database['carros']

# criando instancia de um novo veiculo
new_car = {"Marca": "Ford", "Modelo": "Ranger", "Ano": 2022, "Preco": 135000}

# executando um INSERT_ONE do novo veiculo
collection.insert_one(new_car)

# atualizando um veículo com UPDATE_ONE:
#collection.update_one({"Marca": "Ford", "Modelo": "Bronco", "Ano": 2023, "Preco": 125000}, {"$set": {"Preco": 150000}} )

# removendo um documento da coleção pelo OBJECT_ID com DELETE_ONE
collection.delete_one({"_id": ObjectId("645d31c368a763a9ea3bac0f")})

# removento um documento da coleção pelo OBJECT_ID com DELETE_MANY
#ids_para_excluir = ["60a4db0f1d721d8e2385f1b5", "645d2e998a1069115de21551"]
#ids_objectid = [ObjectId(_id) for _id in ids_para_excluir]
#collection.delete_many({"_id": {"$in": ids_objectid}})

# collection.delete_one({"_id": ObjectId("645d31c368a763a9ea3bac0f")})

# executando um FIND na coleção veiculo
resultado = collection.find()
for documento in resultado:
    print(documento)
