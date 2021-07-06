from flask import render_template

def hello_world():
    return "Hello, MVC框架!"

def index():
    title = "Jinja 示範"
    big_word = "SHOW ME JINJA"
    return render_template('index.html', title=title, big_word=big_word) 