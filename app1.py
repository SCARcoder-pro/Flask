from flask import Flask, render_template, redirect, url_for, session, flash, request
from products import products

app = Flask(__name__)
app.secret_key = "secret123"

def get_product(product_id):
    for product in products:
        if product['id'] == product_id:
            return product
    return None

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/products")
def product_list():
    return render_template("products.html", products=products)

@app.route("/add/<int::id>")
def add_to_cart(id):
    cart = session.get('cart', [])
    item= str(id)
    if item in cart:
        cart[item] += 1
    else:
        cart[item] = 1
    
    session["cart"] = cart
    flash("Product added successfully", "success")
    return redirect(url_for("product_list"))

@app.route("/cart")
def view_cart():
    cart = session.get('cart', {})
    cart_items = []
    grand_total = 0

    for pid, qty in cart.items():
        product = get_product(int(pid))
        total = product["price"] * qty
        grand_total += total
        cart_items.append({
            "product": product,
            "quantitu": qty,
            "total": total
        })