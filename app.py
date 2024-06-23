# http://btu.pythonanywhere.com
# pythonanywhere-ზე ცვლელები (რეგისტრაცია და make_response) ასახული არაა, ვეღარ ჩავამატე.

# Required libraries
from flask import Flask, render_template, request, redirect, session, flash, make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Configuration for app
app.config['SECRET_KEY'] = 'cf813a23dfe7472f9a1e2b9d8f1c7a59'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Define Product model
class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(100), nullable=False)

    def __str__(self):
        return f'{self.name} {self.category} {self.price}'


# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.email}>'


# Mapping of categories to colors (for design)
category_mapping = {
    'testosterones': 'blue',
    'trenbolones': 'green',
    'nandrolones': 'yellow',
    'post cycle therapy': 'yellow',
    'miscellaneous': 'green',
    'mixes': 'pink',
    'orals': 'pink',
    'human growth hormone': 'blue'
}


# Home page route
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')


# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        account = User.query.filter_by(email=email).first()
        if account is None:
            user = User(email=email, password=password)
            db.session.add(user)
            db.session.commit()
            flash('Registration successful', 'success')
            return redirect('/login')
        else:
            flash('Email already registered', 'error')
    return render_template('register.html')


# Login route
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            session['email'] = email
            flash('Login successful', 'success')
            return redirect('/home')
        else:
            flash('Invalid email or password', 'error')
    return render_template('login.html')


# Logout route
@app.route('/logout')
def logout():
    session.pop('email', None)
    flash('Logged out successfully', 'info')
    return redirect('/login')


# Shop route
@app.route('/shop')
def shop():
    all_products = Products.query.all()
    return render_template('shop.html', all_products=all_products, category_mapping=category_mapping)


# User-specific category route
@app.route('/<category>')
def user(category):
    products = Products.query.filter_by(category=category).all()
    if not products:
        return render_template('404.html'), 404
    return render_template('products.html', products=products, category_mapping=category_mapping)


# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


# Route to set a cookie
@app.route('/setcookie')
def set_cookie():
    resp = make_response("Cookie is set")
    resp.set_cookie('example_cookie', 'cookie_value')
    return resp


# Route to get a cookie
@app.route('/getcookie')
def get_cookie():
    cookie_value = request.cookies.get('example_cookie')
    return f'The value of the cookie is: {cookie_value}'


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
