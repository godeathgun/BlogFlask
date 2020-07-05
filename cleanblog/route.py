from flask import render_template, url_for, flash, redirect

from cleanblog import app
from cleanblog import db
from cleanblog.form import RegistrationForm, LoginForm
from flask_login import login_user, current_user

from cleanblog.models import User, Post

posts = [
    {
        'author': 'Phat Pham',
        'title': 'Blog Post',
        'content': 'First post content',
        'date_posted': '11-11-11'
    },
    {
        'author': 'Phat Pham 2',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': '12-12-12'
    }
]


@app.route('/')
@app.route("/home")
def home():
    return render_template('Index.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        db.execute("insert into User (id,email,password,username) values (uuid(),'" +
                   form.email.data + "','" + form.password.data + "','" + form.username.data + "')")
        flash('Account created. You are now able to login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        users = db.execute("select * from User where email='" + form.email.data + "' LIMIT 1 ALLOW FILTERING;")
        flag = 0
        user_1 = User()

        for user in users:
            if user.email == form.email.data and user.password == form.password.data:
                flag = 1
                user_1 = user

        if flag == 1:
            flash('Logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Wrong information', 'danger')
    return render_template('login.html', title='Login', form=form)

# @app.route("/logout")
# def logout():
