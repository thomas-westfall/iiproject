from flask import Flask, render_template, redirect, url_for
from flask import request
import random

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def homepage():
    if request.method == "POST":
        genre = request.form['genre']
        return redirect(url_for("result", genre = genre))
    return render_template("homepage.html")

@app.route("/result/<string:genre>")
def result(genre):
    book_genre = genre
    book_list = ["hello","it's","me"]
    list_size = len(book_list)
    return render_template('result.html', genre = book_genre, book_list = book_list, list_size=list_size)


app.run(debug=True, port=8000)