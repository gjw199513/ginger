# -*- coding:utf-8 -*-
from flask import jsonify
from sqlalchemy import or_

from app.libs.redprint import Redprint
from app.models.book import Book
from app.validators.forms import BookSearchForm

__author__ = 'gjw'
__date__ = '2018/5/24 11:54'

# redprint
api = Redprint('book')


@api.route('/search')
def search():
    # url http://localhost:5000/v1/book/search?q={}
    form = BookSearchForm().validate_for_api()
    q = '%' + form.q.data + '%'
    books = Book.query.filter(
        or_(Book.title.like(q), Book.publisher.like(q))).all()
    # 隐藏字段
    books = [book.hide('summary', 'id') for book in books]
    return jsonify(books)


@api.route('/<isbn>/detail')
def detail(isbn):
    book = Book.query.filter_by(isbn=isbn).first_or_404()
    return jsonify(book)
