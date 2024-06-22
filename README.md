# **RoidRage Fitness Shop**
This project is a Flask web application that serves as an online shop for Lion Labs Fitness products. It includes functionality for users to browse products, log in, log out, and view products by category.

### **Features**

## **Home Page**

URL: / or /home

Description: The home page provides an introduction to the RoidRage Fitness shop.

Template: index.html

## **User Authentication**

### **Login**

URL: /login

Description: Allows users to log in to the website. Users provide their email and password. Upon successful login, users are redirected to the home page.

Template: login.html

### **Logout**

URL: /logout

Description: Logs the user out of the website, clears the session, and displays a logout success message. Users are redirected to the login page.

Template: login.html

## **Shop**

### **All Products**

URL: /shop
Description: Displays all products available in the shop. Each product is displayed as a card with its image, name, category, and price. The category color mapping is used to differentiate product categories visually.

Template: shop.html

### **Category-Specific Products**

URL: / < category >

Description: Displays products belonging to a specific category. If no products are found for the given category, a 404 error page is shown.

Template: products.html for valid categories, 404.html for invalid categories

## **Error Handling**

### **404 Not Found**

URL: N/A

Description: Renders a custom 404 error page when a requested page or resource is not found.

Template: 404.html

## **Database**

The application uses an SQLite database named products.db to store product information. The database is populated using web scraping from the Lion Labs Fitness website.

### **Database Schema**

The products table schema includes the following columns - id: Primary key; name: Product name; category: Product category; price: Product price; image: URL of the product image; link: URL of the product details page.

### **Database Population**

A script (database.py) is used to scrape product data from the Lion Labs Fitness website and populate the products table in the SQLite database. The script uses the requests library to fetch web pages and BeautifulSoup to parse the HTML content.
