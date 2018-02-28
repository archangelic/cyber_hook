import random

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    with open('cyber_snippets') as c:
        out = random.choice(c.readlines()).strip()
    return out

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
