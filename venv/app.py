# import das bibliotecas necessárias
from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient

# criando o app Flask
app = Flask(__name__)

# conectando ao mongodb
client = MongoClient("localhost", 27017)
db = client['veiculos']

# criando primeira rota
@app.route("/", methods=['GET'])
def index():
    carros = db.carros.find()

    return render_template("index.html", carros = carros)

@app.route("/carros", methods=['GET', 'POST'])
def list_carro():
    carros = db.carros.find()
    return render_template("carros.html", carros = carros)

@app.route("/add", methods=['GET', 'POST'])
def add_carro():
    if request.method == "GET":
        return render_template("addcarro.html")
    else:
        # obtendo carros
        Marca = request.form['marca']
        Modelo = request.form['modelo']
        Preco = request.form['preco']
        Ano = request.form['ano']
        Categoria = request.form['categoria']
        Cambio = request.form['cambio']

        carro = {
            'marca': Marca,
            'modelo': Modelo,
            'preco': Preco,
            'ano': Ano,
            'categoria': Categoria,
            'cambio': Cambio
        }

        db.carros.insert_one(carro)

        return redirect(url_for('index'))

# rodando o app
if __name__ == "__main__":
    app.run(debug = True)