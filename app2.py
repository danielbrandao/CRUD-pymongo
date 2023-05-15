from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/veiculos"
mongo = PyMongo(app)

cars = mongo.db.cars

@app.route("/")
def index():
  cars = cars.find()
  return render_template("index.html", cars=cars)

@app.route("/add", methods=["POST"])
def add():
  car_data = request.form.to_dict()
  cars.insert_one(car_data)
  return redirect("/")

@app.route("/edit", methods=["POST"])
def edit():
  car_id = request.form["car_id"]
  car_data = request.form.to_dict()
  cars.update_one({"_id": car_id}, {"$set": car_data})
  return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
  car_id = request.form["car_id"]
  cars.delete_one({"_id": car_id})
  return redirect("/")

if __name__ == "__main__":
  app.run(debug=True)
