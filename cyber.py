import tracery
from tracery.modifiers import base_english

import json
import random

from flask import Flask, render_template

app = Flask(__name__)

def get_magic_snippet():
    with open('magic.json') as m:
        magic_rules = json.load(m)

    magic = tracery.Grammar(magic_rules)
    magic.add_modifiers(base_english)
    return magic.flatten('#origin#')

def get_snippet():
    with open('cyber_snippets') as c:
        return random.choice(c.readlines()).strip()

@app.route('/snippet')
def hello():
    return get_snippet()

@app.route('/magic')
def magic_tome():
    return render_template('magic.html', snippet=get_magic_snippet())

@app.route('/magic/snippet')
def magic_snippet():
    return get_magic_snippet()

@app.route('/')
def about():
    return render_template('about.html', snippet=get_snippet())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
