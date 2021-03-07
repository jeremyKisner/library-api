#!/usr/bin/env python3
import json
from flask import Flask, render_template, request

app = Flask(__name__)
with open('data/data.json', 'r') as data_file:
	data = data_file.read()

books = []
for book in json.loads(data):
	books.append((book['name'], book['read']))
 
@app.route("/get")
def get():
    return render_template('index.html', books=books)

if __name__ == "__main__":
    app.run()