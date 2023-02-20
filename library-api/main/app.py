#!/usr/bin/env python3
import json
from library import Library
from flask_cors import CORS
from flask import Flask, request

app = Flask(__name__)
CORS(app)
library = Library()


@app.route('/books', methods=['GET'])
def get_books():
	return json.dumps(library.load_inventory())


# @app.route('/read', methods=['POST'])
# def post_read():
# 	print(f'Updating {request.form["book_name"]}')
# 	library.update_book_read(request.form['book_name'])
# 	return "Book Read"


# @app.route('/add')
# def add():
# 	library.add_book(request.args.get('name'))
# 	return "Book Added"


if __name__ == '__main__':
    app.run()
