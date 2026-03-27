from flask import Blueprint, render_template

main = Blueprint("main", __name__)

# Sample cars
cars = [
    {"name": "Tesla Model 3", "price": "$40,000", "image": "https://tesla-cdn.thron.com/delivery/public/image/tesla/Model3.jpg"},
    {"name": "BMW M3", "price": "$72,000", "image": "https://cdn.bmwblog.com/wp-content/uploads/2018/03/BMW-M3-F80-Competition-Review-7.jpg"},
    {"name": "Toyota Supra", "price": "$55,000", "image": "https://cdn.motor1.com/images/mgl/0ANPP/s1/2020-toyota-supra.jpg"}
]

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/cars")
def list_cars():
    return render_template("cars.html", cars=cars)