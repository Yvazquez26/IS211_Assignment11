#!/usr/bin/env python
# coding: utf-8

# Week 11 Assignment - Web Development with Flask (1/2)


from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)

todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/submit', method=['post'])
def submit():
    task = request.form['Task Name']
    priority = request.form['Priority']
    email = request.form['Email Address']

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return redirect('/')
    elif not task:
        return redirect('/')
    elif priority == 'Priority Level':
        return redirect('/')
    else:
        todos.append((task, priority, email))

    print(todos)
    return redirect('/')


@app.route('/clear', method=['post'])
def clear():
    del todos[:]
    return redirect('/')


if __name__ == '__main__':
    app.run()

