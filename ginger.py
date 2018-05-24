# -*- coding:utf-8 -*-
from app.app import create_app

__author__ = 'gjw'
__date__ = '2018/5/24 11:16'


app = create_app()


@app.route('/v1/user/get')
def get_user():
    return 'i am'


if __name__ == '__main__':
    app.run(debug=True)