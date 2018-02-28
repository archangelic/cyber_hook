import random

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    with open('cyber_snippets') as c:
        out = random.choice(c.readlines()).strip()
    return out

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
