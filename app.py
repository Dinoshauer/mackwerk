# -*- coding: utf-8 -*-
from flask import Flask, g, render_template, request, flash, redirect, url_for, jsonify

app = Flask(__name__)
app.secret_key = 'mackwerk201'

# Home
@app.route('/')
@app.route('/home')
def home():
    return render_template('/home.htm')

# Work
@app.route('/work')
def work():
    return render_template('/cases.htm')

# Work - Single case
@app.route('/work/<slug>')
def workPost(slug):
    return render_template('/case.htm')

# Photography
@app.route('/photography')
def photography():
    return render_template('/index.htm')

# Photography - Single photo
@app.route('/photography/<slug>')
def photographyPost(slug):
    return render_template('/index.htm')

# Blog
@app.route('/blog')
def blog():
    return render_template('/blog.htm')

# Blog - Categories
@app.route('/blog/<category>')
def blogCategory(category):
    return render_template('/index.htm')

# Blog - Category - Post
@app.route('/blog/<category>/<slug>')
def blogPost(category, slug):
    return render_template('/blog-post.htm')


@app.route('/about-me')
def aboutMe():
    return render_template('/index.htm')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

#import logging
#file_handler = logging.FileHandler('thenestapp.log')
#file_handler.setLevel(logging.DEBUG)
#app.logger.addHandler(file_handler)