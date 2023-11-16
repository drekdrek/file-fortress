from app import app
from flask import request, jsonify, render_template

@app.route('/', methods=['GET'])
def web_root():
    return render_template('index.html')

@app.route('/<short_link>', methods=['GET'])
def web_get_file(short_link):
    return render_template('file.html', short_link=short_link)