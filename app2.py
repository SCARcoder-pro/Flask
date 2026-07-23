from flask import Flask, render_template, redirect, url_for, session, flash, request
from products import products


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

app.route("/add", methods=["GET", "POST"])
def add_book():
    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":
        book = Book(
            title=request.form["title"],
            author=request.form["author"],
            category=request.form["category"],
            price=float(request.form["price"]),
            quantity=int(request.form["quantity"])
        )

        db.session.add(book)
        db.session.commit()

        return redirect("/")

    return render_template("add_book.html")