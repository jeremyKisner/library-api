#!/usr/bin/env python3
import json

from flask_cors import CORS
from flask import Flask, request

from library import Library

app = Flask(__name__)
CORS(app)
library = Library()


@app.route('/books', methods=['GET'])
def get_books():
    print("retrieving inventory")
    return json.dumps(library.get_books(), indent=2)


@app.route('/books/get', methods=['GET'])
def get_book_by_key():
    response = None
    if request.is_json:
        response = library.get_matching_books(request.json)
    if not response:
        return "no books found matching criteria"
    return json.dumps(response, indent=2)


@app.route('/books/add', methods=["POST"])
def add():
    if request.is_json and library.add_books(request.json):
        return "book added"
    print(f"failed to add book for payload {request.data}")
    return "failed to add book, check request!"


@app.route('/books/checkout', methods=["POST"])
def check_out_book():
    if request.is_json and library.check_out(request.json):
        return "book checked out"
    print(f"failed to check out book for payload {request.data}")
    return "failed to check out book, check request!"


@app.route('/books/delete', methods=['POST'])
def delete_book():
    if request.is_json and library.delete_book(request.json):
        return "book deleted"
    print(f"failed to delete book, either book not found or bad request: {request.data}")
    return "failed to delete book, either book not found or bad request"


if __name__ == '__main__':
    app.run()
