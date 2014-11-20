import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory


# Initialize the Flask application
app = Flask(__name__)
server_date = {
'server_date':"2014-11-21"
}

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
def home():
    return render_template('main.html',**server_date)


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("80"),
        debug=True
    )
