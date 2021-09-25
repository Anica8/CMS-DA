from flask import Flask,render_template,request,Response
import os

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html",template_folder='templates')

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True,port="5000")