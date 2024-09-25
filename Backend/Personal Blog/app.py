from flask import Flask, render_template 
import json
import os

app = Flask(__name__)

#ARTICLES_DIR = ""

@app.route("/profile/<name>")

def profile(name):
    return render_template("index.html", name=name)
  

if __name__ == "__main__":
    app.run(debug=True)