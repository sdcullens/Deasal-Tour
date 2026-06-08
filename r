from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Deasal Tour and Travel</h1>"

if __name__ == "__main__":
    app.run()