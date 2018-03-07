import random

from flask import Flask, render_template

app = Flask(__name__)

def get_snippet():
    with open('cyber_snippets') as c:
        return random.choice(c.readlines()).strip()

@app.route('/snippet')
def hello():
    return get_snippet()

@app.route('/')
def about():
    return render_template('about.html', snippet=get_snippet())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
