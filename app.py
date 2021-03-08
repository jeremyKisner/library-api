#!/usr/bin/env python3
from library import Library
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
library = Library()
 
@app.route("/")
def get():
    return render_template("index.html", books=library.get_books())

@app.route("/read")
def set_read():
	library.update_book_read(request.args.get("name"))
	return redirect(url_for('get'))

if __name__ == "__main__":
    app.run()
