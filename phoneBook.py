#!/usr/bin/env python3

from flask import Flask, url_for, request, session, render_template

app = Flask(__name__)


@app.route('/')
def index():
    if 'user' in session:
        url_for('view')
    else:
        url_for('login')


@app.route('/login')
def login():
    if 'user' in session:
        url_for('index')
    elif request.method == 'POST':
        pass
    elif request.method == 'GET':
        return render_template('templates/login.html')


@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop(session['user'])
    url_for('login')


def view():
    return render_template('templates/view.html')
