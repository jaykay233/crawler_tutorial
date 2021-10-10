#coding:utf8
from flask import Flask

app=Flask(__name__)

@app.route('/sabo')
def index_1():
    return 'hello sabo!'

if __name__ == '__main__':
    app.run(debug=True)