from flask import Blueprint, render_template

main = Blueprint("main", __name__)

cars = [
    {"name": "Tesla Model 3", "price": "$40,000"},
    {"name": "BMW M3", "price": "$72,000"},
    {"name": "Toyota Supra", "price": "$55,000"},
]

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/cars")
def list_cars():
    return render_template("cars.html", cars=cars)