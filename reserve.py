import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory


# Initialize the Flask application
app = Flask(__name__)

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def home():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("80"),
        debug=True
    )
