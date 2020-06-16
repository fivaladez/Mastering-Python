"""
Install flask:
    - pip3 install flask
Create venv:
    - pip3 install virtualenv
    - python3 -m venv Web/web_server/ or virtualenv Web/web_server
Init Flask(Linux)
    - export FLASK_APP=server.py
    - flask run

    (Debug mode On) - For modifying in real time
    - export FLASK_ENV=development
    - flask run
Pay attention:
    - You can add {{}} in html to inject Python code.
      Whit this, you can pass parameters to make your website dynamically
    - Pasing parameters: /<username>/<int:post_id>
"""

from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>.html')
def html_page(page_name='index.html'):
    return render_template(f'{page_name}.html')
