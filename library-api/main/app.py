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
	return json.dumps(library.get_inventory(), indent=2)


@app.route('/books/add', methods=["POST"])
def add():
    if request.is_json and library.add_inventory(request.json):
        return "book added"
    else:
        print(f"failed to add book for payload {request.data}")
        return "failed to add book, check request"


@app.route('/books/get', methods=['GET'])
def get_book_by_name():
    response = None
    if request.is_json:
        response = library.get_book(request.json)
    if not response:
        return "no books found matching criteria"
    return json.dumps(response, indent=2)


@app.route('/books/delete', methods=['POST'])
def delete_book():
    if request.is_json and library.delete_book(request.json):
        return "book deleted"
    else:
        print(f"failed to delete book, either book not found or bad request: {request.data}")
        return "failed to delete book, either book not found or bad request"


if __name__ == '__main__':
    app.run()
