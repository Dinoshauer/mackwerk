# -*- coding: utf-8 -*-
from flask import Flask, g, render_template, request, flash, redirect, url_for, jsonify

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.secret_key = 'mackwerk201'

# Home
@app.route('/')
@app.route('/home')
def home():
    work = []
    workI = 0
    while workI < 2:
        case = {
            'img':None,
            'summary':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sit amet tellus odio. Fusce lacinia, nisi et dignissim tempor, neque turpis convallis dui, eleifend luctus lorem risus ac lectus. Praesent aliquet gravida condimentum. Aenean luctus, enim sed placerat pellentesque, orci orci semper quam, sed posuere ligula turpis ut libero. Ut molestie nisl eu lorem tempor in egestas tortor rhoncus. Sed accumsan volutpat fringilla. Pellentesque vehicula ultrices nibh, at facilisis lorem tincidunt ac. In interdum sodales nulla nec hendrerit. Morbi rutrum, purus venenatis aliquam sollicitudin, mauris libero sollicitudin erat, ac fermentum sem enim eu augue. Vivamus pretium, quam id faucibus feugiat, libero elit elementum dolor, eget molestie leo libero id sem.',
            'slug':'some-case-{0}'.format(workI)
        }
        work.append(case)
        workI += 1

    blog = []
    blogI = 0
    while blogI < 3:
        post = {
            'img':None,
            'header':'Some blog post {0}'.format(blogI),
            'summary':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sit amet tellus odio. Fusce lacinia, nisi et dignissim tempor, neque turpis convallis dui, eleifend luctus lorem risus ac lectus. Praesent aliquet gravida condimentum. Aenean luctus, enim sed placerat pellentesque, orci orci semper quam, sed posuere ligula turpis ut libero. Ut molestie nisl eu lorem tempor in egestas tortor rhoncus. Sed accumsan volutpat fringilla. Pellentesque vehicula ultrices nibh, at facilisis lorem tincidunt ac. In interdum sodales nulla nec hendrerit. Morbi rutrum, purus venenatis aliquam sollicitudin, mauris libero sollicitudin erat, ac fermentum sem enim eu augue. Vivamus pretium, quam id faucibus feugiat, libero elit elementum dolor, eget molestie leo libero id sem.',
            'slug':'some-blog-post-{0}'.format(blogI)
        }
        blog.append(post)
        blogI += 1

    photography = []
    photoI = 0
    while photoI < 7:
        photo = {
            'img':None,
            'slug':'photo-{0}'.format(photoI)
        }
        photography.append(photo)
        photoI += 1
    return render_template('/home.htm', work = work, blog = blog, photography = photography)

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