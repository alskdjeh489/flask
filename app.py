# http://btu.pythonanywhere.com

# Required libraries
from flask import Flask, render_template, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# Configuration for app
app.config['SECRET_KEY'] = 'cf813a23dfe7472f9a1e2b9d8f1c7a59'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Define Product model
class Products(db.Model):
    # Define columns for Product table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    price = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(100), nullable=False)

    # Define string representation of Product
    def __str__(self):
        return f'{self.name} {self.category} {self.price}'


# Mapping of categories to colors
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


# Login route
@app.route('/login', methods=['POST', 'GET'])
def login():
    # Handle login form submission
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        session['email'] = email
        return redirect('/home')
    return render_template('login.html')


# Logout route
@app.route('/logout')
def logout():
    # Clear session and display logout message
    session.pop('email', None)
    flash('Logged out successfully', 'info')
    return render_template('login.html')


# Shop route
@app.route('/shop')
def shop():
    all_products = Products.query.all()
    return render_template('shop.html', all_products=all_products,
                           category_mapping=category_mapping)


# User-specific category route
@app.route('/<category>')
def user(category):
    # Retrieve products for a specific category
    products = Products.query.filter_by(category=category).all()
    if not products:
        return render_template('404.html'), 404  # Render 404 page if no products found
    return render_template('products.html', products=products, category_mapping=category_mapping)


# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found():
    return render_template("404.html")


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
