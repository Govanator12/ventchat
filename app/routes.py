from app import app
from app.__init__ import  pusher_client
from app.forms import ContactForm, PostForm
from flask import render_template, url_for, redirect, request, jsonify


@app.route('/')
@app.route('/index')
def index():
    # pusher_client.trigger('my-channel', 'my-event', {'message': 'hello world'})

    return render_template('index.html', title="Home")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")

@app.route('/rooms')
def rooms():
    return render_template('rooms.html', title="Rooms")
