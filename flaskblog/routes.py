from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author': 'Andrei',
        'title': 'Blog Post 1',
        'content': 'first post content',
        'date': 'April 22 2020'
    },
    {
        'author': 'Stink',
        'title': 'Blog Post 2',
        'content': 'first post content',
        'date': 'April 24 2020'
    }

]
# route: what we type into browser to get to pages
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/registration', methods = ['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for: {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('registration.html', title = 'Register', form = form)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccesful. Please check credentials', 'danger')

    return render_template('login.html', title = 'Login', form = form)