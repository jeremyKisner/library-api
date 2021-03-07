#!/usr/bin/env python3
from library import Library
from flask import Flask, render_template, request, url_for

app = Flask(__name__)
 
@app.route("/")
def get():
    return render_template("index.html", books=Library.get())

@app.route("/read")
def set_read():
	Library.update_book_read(request.args.get("name"))
	return request.args.get("name")

if __name__ == "__main__":
    app.run()
