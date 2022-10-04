from cProfile import run
from email.policy import default
import dbhelper
import json
from flask import Flask


app = Flask(__name__)

@app.get('/api/books')
def get_all_books():
    books = dbhelper.run_statment('CALL book_info')
    if(type(books) == list):
        books_json = json.dumps(books, default=str)
        return books_json
    else:
        return "sorry"

@app.get('/api/books_written_by_author')
def get_books_by_author():
    books = dbhelper.run_statment('CALL order_authors_by_sale')
    if(type(books) == list):
        books_json = json.dumps(books, default=str)
        return books_json
    else:
        return "sorry"


@app.get('/api/best_selling_books')
def best_selling_books():
    books = dbhelper.run_statment('CALL best_selling_books')
    if(type(books) == list):
        books_json = json.dumps(books, default=str)
        return books_json
    else:
        return "sorry"


@app.get('/api/books_written')
def get_books_written():
    books = dbhelper.run_statment('CALL books_written')
    if(type(books) == list):
        books_json = json.dumps(books, default=str)
        return books_json
    else:
        return "sorry"


app.run(debug=True)